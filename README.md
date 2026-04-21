# 📐 Geometry Area & Vision Calculator using GenAI 🤖

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Backend-green.svg)](https://flask.palletsprojects.com/)
[![Gemini](https://img.shields.io/badge/Google_Gemini-2.5_Flash-orange.svg)](https://aistudio.google.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)
[![Hosted on Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97-Hugging_Face-yellow)](https://huggingface.co/spaces)

# 📐 Geometry Area and Volume Calculator 📏
A user-friendly web application built with Flask that allows you to calculate the area and volume of various 2D and 3D geometric shapes with customizable units.
## ✨ Key Features
### 📏 Standard Geometric Calculations
* **2D Shapes:** Circle, Rectangle/Square, Triangle (Right, Equilateral, Isosceles, Scalene, ASA/SAS), Trapezium, Parallelogram, Pentagon, Hexagon, Rhombus, Ellipse, Sector.
* **3D Shapes:** Sphere, Cylinder, Cuboid, Cone, Pyramid (Surface Area & Volume).
* **Dynamic Conversions:** Native support for Meters, Centimeters, Millimeters, Inches, and Feet.
### 🤖 AI Vision Sketch Recognition (Flagship Feature)
* **Compound Geometry Parsing:** user can get answer for messy and hand-drawn complex and compound geometries by uploading/taking image of the sketch or printed shapes using the advanced **Vision-Language Model (VLM)**. (e.g., a rectangle with an attached semicircle).
* **Zero-Retention Architecture:** Images are processed strictly in memory using the `google-genai` SDK and are never stored on the server.
* **Interactive "Review & Correct" UI:** The frontend dynamically generates an input form based on the AI's JSON output, allowing the user to review detected measurements and manually input any missing dimensions before executing the final math.  
* Webpage screenshot ![image](https://github.com/user-attachments/assets/eac37000-aae2-4e4a-8972-54613f32b038)


**The calculator is live on Hugging Face Spaces:** 👉 **[Geometry Calculator](https://huggingface.co/spaces/Deep7285/Geometry-Calculator)**

## To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
   git clone [https://github.com/Deep7285/Geometry-Area-and-Volume-Calculator.git](https://github.com/Deep7285/Geometry-Area-and-Volume-Calculator.git)
   cd Geometry-Area-and-Volume-Calculator
    ```
2.  **Create and activate a virtual environment:**  
    ```bash
        # On Windows:
    python -m venv venv
    .\venv\Scripts\activate
    # On macOS/Linux:
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install dependencies:**  
    ```bash
    pip install -r requirements.txt
    ```
4.  **Setup Environment Variables:**  
    This app requires a Google Gemini API Key to process sketches.  
    i. This app requires a Google Gemini API Key to process sketches.  
    ii. Add your API key:
    ```bash
    GEMINI_API_KEY=your_actual_api_key_here
    ```  
    (Note: The .env file is included in .gitignore to prevent secret leakage).  
5. **Run the Flask application:**
   for testing run the following in the terminal   
    ```bash
    python app.py
    ```  
    this will open the localhost for test environment  
6.  Open your web browser and navigate to `http://127.0.0.1:5000/`.  
## 🐳 Docker Support  
   This project includes a production-ready Dockerfile. To run it containerized:  
   ```bash
   docker build -t geometry-calculator .
   docker run -p 7860:7860 -e GEMINI_API_KEY=your_key_here geometry-calculator  
   ```

## 🛠️ Technologies Used

* **Backend:** Python 3.11, Flask
* **AI Integration:** Google GenAI SDK (`gemini-2.5-flash`)
* **Computer Vision Processing:** OpenCV, Pillow, Numpy
* **Production Server:** Gunicorn
* **Frontend:** HTML5, CSS3 (Flexbox), Vanilla JavaScript (Dynamic DOM Manipulation)
* **Deployment:** Docker Containerized, hosted via Hugging Face Spaces

## Designed & Developed by Deep7285
