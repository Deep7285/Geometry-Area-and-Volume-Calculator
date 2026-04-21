from flask import Flask, render_template, request, jsonify
import sys
import cv2
import numpy as np 
from dotenv import load_dotenv
import os

load_dotenv() # Load environment variables from .env file

# We only import the VLM function now. The others are safely stored in the core module but not loaded here.
from core.vision_pipeline import analyze_with_vlm

# Import the math logic from math_engine.py
from core.math_engine import calculate_area_web

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print(f"Request method: {request.method}", file=sys.stderr)

    result = None
    shape_type = None

    if request.method == 'POST':
        form_dict = request.form.to_dict()
        print(f"Form data: {form_dict}", file=sys.stderr)

        shape_type = form_dict.get('shape_type')
        unit = form_dict.get('unit_type', 'units')

        params = dict(form_dict)
        params.pop('shape_type', None)
        params.pop('unit_type', None)

        result = calculate_area_web(shape_type, unit=unit, **params)
        print(f"Result to template: {result}", file=sys.stderr)

    return render_template('index.html', result=result, shape_type=shape_type)

@app.route('/analyze', methods=['POST'])
def analyze_sketch():
    if 'image' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "Empty file"}), 400

    # 1. Read the raw bytes
    file_bytes = file.read() 

    # 2. Briefly decode with OpenCV just to get the dimensions for the frontend UI
    np_bytes = np.frombuffer(file_bytes, np.uint8)
    img = cv2.imdecode(np_bytes, cv2.IMREAD_COLOR)
    
    if img is None:
        return jsonify({"error": "Invalid image format"}), 400
        
    height, width, _ = img.shape

    # 3. Send the raw bytes directly to Hugging Face
    vlm_result = analyze_with_vlm(file_bytes)

    if "error" in vlm_result:
        return jsonify({"error": vlm_result["error"]}), 400

    # 4. Return the dimensions AND the VLM data
    return jsonify({
        "status": "success",
        "message": "Sketch analyzed by VLM!",
        "dimensions": {"width": width, "height": height},
        "vlm_data": vlm_result
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)