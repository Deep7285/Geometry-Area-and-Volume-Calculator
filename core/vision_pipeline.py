# core/vision_pipeline.py
import cv2
import numpy as np
import base64
import requests
import os
import json
import io
from PIL import Image
import google.generativeai as genai

def clean_sketch(img):
    """
    Preprocesses a hand-drawn sketch to remove noise, shadows, and notebook lines.
    """
    # 1. Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. Adaptive Thresholding (handles uneven lighting from phone cameras better than standard Otsu)
    # Block size 31, C value 15 (good defaults for pencil/pen sketches)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 31, 15)
    
    # 3. Remove notebook grid lines (horizontal and vertical)
    # Find horizontal lines
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 1))
    detected_lines_h = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
    
    # Find vertical lines
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 25))
    detected_lines_v = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
    
    # Combine the detected notebook lines and subtract them from our sketch
    lines = cv2.add(detected_lines_h, detected_lines_v)
    cleaned = cv2.subtract(thresh, lines)
    
    # 4. Dilate slightly to reconnect any shape edges that got disconnected during line removal
    kernel = np.ones((3,3), np.uint8)
    cleaned = cv2.dilate(cleaned, kernel, iterations=1)
    
    # 5. Invert back so the background is white and shapes are black (best for OCR)
    final_img = cv2.bitwise_not(cleaned)
    
    return final_img


# API to use hugging face mode
def analyze_with_vlm(image_bytes):
    """
    Sends the raw image to Google's Gemini API to extract geometry data.
    """
    # API key
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return {"error": "GEMINI_API_KEY is missing. Check .env file."}

    try:
        # Configure the model flash 1.5, its fast and free
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-flash-latest')

        # Convert raw bytes into a format Gemini understands (PIL Image)
        image = Image.open(io.BytesIO(image_bytes))

        # The Prompt
        prompt = """
        Analyze this hand-drawn geometry sketch. 
        Identify the shapes and any written dimensions. 
        Return ONLY a clean JSON object in this exact format:
        {
          "shapes": ["rectangle", "semicircle"],
          "dimensions": {"height": 5, "unit": "m"}
        }
        Do not include any other text, markdown formatting, or code blocks. Just the raw JSON.
        """

        # Send the image and prompt to Gemini
        response = model.generate_content([prompt, image])
        
        # Clean up the response
        text_response = response.text.strip()
        if text_response.startswith('```json'):
            text_response = text_response[7:-3].strip()
        elif text_response.startswith('```'):
            text_response = text_response[3:-3].strip()

        # Convert the text into a real Python Dictionary
        return json.loads(text_response)

    except Exception as e:
        return {"error": f"Gemini API Call Failed: {str(e)}"}

def cv2_to_base64(img):
    """Converts an OpenCV image matrix to a base64 string so HTML can display it."""
    _, buffer = cv2.imencode('.jpg', img)
    img_str = base64.b64encode(buffer).decode('utf-8')
    return f"data:image/jpeg;base64,{img_str}"