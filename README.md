# 📐 Geometry Area and Volume Calculator 📏
A user-friendly web application built with Flask that allows you to calculate the area and volume of various 2D and 3D geometric shapes with customizable units.
Features:
* Calculate area for 2D shapes: Circle, Quadrilateral (Rectangle/Square), Triangle (Right Angle, Equilateral, Isosceles, Scalene, Two Sides & One Angle), Trapezium, Parallelogram, Pentagon, Hexagon, Rhombus, Ellipse, Sector.
* Calculate surface area and volume for 3D shapes: Sphere, Cylinder, Cuboid, Cone, Pyramid.
* Select from various measurement units: Meters, Centimeters, Millimeters, Inches, Feet.
* Interactive and responsive web interface.
* Error handling for invalid inputs.
* Webpage screenshot ![image](https://github.com/user-attachments/assets/eac37000-aae2-4e4a-8972-54613f32b038) (path/to/your/screenshot.png) 


Experience the calculator live here: [https://geometrical-shape-calculator.onrender.com/)](https://geometrical-shape-calculator.onrender.com/)
usage instructions:
1.  Visit the [Live Demo link](https://your-geometry-calc.onrender.com).
2.  Select your desired measurement unit from the "Select Unit" dropdown.
3.  Choose a geometric shape from the "Select Shape" dropdown.
4.  Enter the required dimensions (e.g., Radius for Circle, Length & Width for Quadrilateral).
5.  Click the "Calculate Area" button.
6.  The calculated area/volume will be displayed below the form.


To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/geometry_calculator_web.git](https://github.com/yourusername/geometry_calculator_web.git)
    cd geometry_calculator_web
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Flask application:**
    ```bash
    python app.py
    ```
5.  Open your web browser and navigate to `http://127.0.0.1:5000/`.

Technologies Used

* **Backend:** Python 3, Flask
* **Frontend:** HTML5, CSS3, JavaScript
* **Deployment:** Render.com
