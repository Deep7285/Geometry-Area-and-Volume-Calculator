from flask import Flask, render_template, request
import math

app = Flask(__name__)

def calculate_area_web(shape_type, unit="units", **kwargs):
    try:
        # Define unit suffixes for area and volume
        area_unit = f"sq {unit}"
        volume_unit = f"cubic {unit}"
        
        # Adjust for special unit names with Unicode superscripts
        if unit == "meters":
            area_unit = "m\u00b2" # Unicode for m²
            volume_unit = "m\u00b3" # Unicode for m³
        elif unit == "centimeters":
            area_unit = "cm\u00b2"
            volume_unit = "cm\u00b3"
        elif unit == "millimeters":
            area_unit = "mm\u00b2"
            volume_unit = "mm\u00b3"
        elif unit == "inches":
            area_unit = "in\u00b2"
            volume_unit = "in\u00b3"
        elif unit == "feet":
            area_unit = "ft\u00b2"
            volume_unit = "ft\u00b3"

        if shape_type == "circle":
            radius = float(kwargs.get('radius'))
            area = math.pi * (radius ** 2)
            return f"Area of the circle is {area:.2f} {area_unit}"
        elif shape_type == "quadrilateral":
            length = float(kwargs.get('length'))
            width = float(kwargs.get('width'))
            area = length * width
            if length == width:
                return f"The area is {area:.2f} {area_unit} (a Square)"
            else:
                return f"The area is {area:.2f} {area_unit} (a Rectangle)"
        elif shape_type == "triangle":
            triangle_type = kwargs.get('triangle_type', 'right_angle')
            if triangle_type == 'right_angle':
                base = float(kwargs.get('base'))
                height = float(kwargs.get('height')) # Corrected from height_ra
                area = 0.5 * base * height
                return f"The area of the right angle triangle is {area:.2f} {area_unit}"
            elif triangle_type == 'equilateral':
                side = float(kwargs.get('side')) # Corrected from side_eq
                area = (math.sqrt(3) / 4) * (side ** 2)
                return f"The area of the equilateral triangle is {area:.2f} {area_unit}"
            elif triangle_type == 'isosceles':
                base = float(kwargs.get('base')) # Corrected from iso_base
                side = float(kwargs.get('side')) # Corrected from iso_side
                # Ensure side is greater than half base for a real triangle
                if side <= base / 2:
                    return "Invalid isosceles triangle: Equal side must be greater than half the base."
                height = math.sqrt(side**2 - (base/2)**2)
                area = 0.5 * base * height
                return f"The area of the isosceles triangle is {area:.2f} {area_unit}"
            elif triangle_type == 'scalene':
                a = float(kwargs.get('side_a'))
                b = float(kwargs.get('side_b'))
                c = float(kwargs.get('side_c'))
                # Check for valid triangle (triangle inequality theorem)
                if not (a + b > c and a + c > b and b + c > a):
                    return "Invalid scalene triangle sides: Sides do not form a valid triangle."
                s = (a + b + c) / 2
                area = math.sqrt(s * (s - a) * (s - b) * (s - c))
                return f"The area of the scalene triangle is {area:.2f} {area_unit}"
            elif triangle_type == 'two_sides_one_angle':
                side1 = float(kwargs.get('side1'))
                side2 = float(kwargs.get('side2'))
                angle = float(kwargs.get('angle'))
                # Angle must be between 0 and 180 (exclusive) for a valid triangle area calculation
                if not (0 < angle < 180):
                    return "Invalid angle: Angle must be between 0 and 180 degrees."
                area = 0.5 * side1 * side2 * math.sin(math.radians(angle))
                return f"The area of the triangle is {area:.2f} {area_unit}"
            else:
                return "Unknown triangle type."
        elif shape_type == "pyramid":
            # Assuming a square base pyramid for simplicity based on your HTML input names
            base_length = float(kwargs.get('base_length'))
            height = float(kwargs.get('height_py')) # Corrected from height
            base_area = base_length * base_length # For square base
            slant_height_face = math.sqrt((base_length / 2)**2 + height**2) # Slant height of a triangular face
            surface_area = base_area + 2 * base_length * slant_height_face # Base + 4 triangles
            volume = (1/3) * base_area * height
            return f"Pyramid: Surface Area = {surface_area:.2f} {area_unit}, Volume = {volume:.2f} {volume_unit}"
        elif shape_type == "sphere":
            radius = float(kwargs.get('radius_sphere'))
            area = 4 * math.pi * (radius ** 2)
            volume = (4/3) * math.pi * (radius ** 3)
            return f"Sphere: Surface Area = {area:.2f} {area_unit}, Volume = {volume:.2f} {volume_unit}"
        elif shape_type == "cylinder":
            radius = float(kwargs.get('radius_cylinder'))
            height = float(kwargs.get('height_cylinder'))
            surface_area = 2 * math.pi * radius * (radius + height) # Total surface area
            volume = math.pi * (radius ** 2) * height
            return f"Cylinder: Surface Area = {surface_area:.2f} {area_unit}, Volume = {volume:.2f} {volume_unit}"
        elif shape_type == "trapezium":
            a = float(kwargs.get('base1'))
            b = float(kwargs.get('base2'))
            height = float(kwargs.get('height_trapezium'))
            area = 0.5 * (a + b) * height
            return f"Trapezium: Area = {area:.2f} {area_unit}"
        elif shape_type == "parallelogram":
            base = float(kwargs.get('base_para'))
            height = float(kwargs.get('height_para'))
            area = base * height
            return f"Parallelogram: Area = {area:.2f} {area_unit}"
        elif shape_type == "pentagon":
            side = float(kwargs.get('side_pentagon'))
            area = (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (side ** 2)
            return f"Pentagon: Area = {area:.2f} {area_unit}"
        elif shape_type == "hexagon":
            side = float(kwargs.get('side_hexagon'))
            area = (3 * math.sqrt(3) / 2) * (side ** 2)
            return f"Hexagon: Area = {area:.2f} {area_unit}"
        elif shape_type == "cuboid":
            length = float(kwargs.get('length_cuboid'))
            width = float(kwargs.get('width_cuboid'))
            height = float(kwargs.get('height_cuboid'))
            surface_area = 2 * (length * width + length * height + width * height)
            volume = length * width * height
            return f"Cuboid: Surface Area = {surface_area:.2f} {area_unit}, Volume = {volume:.2f} {volume_unit}"
        elif shape_type == "cone":
            radius = float(kwargs.get('radius_cone'))
            height = float(kwargs.get('height_cone'))
            slant_height = math.sqrt(radius**2 + height**2)
            surface_area = math.pi * radius * (radius + slant_height)
            volume = (1/3) * math.pi * (radius ** 2) * height
            return f"Cone: Surface Area = {surface_area:.2f} {area_unit}, Volume = {volume:.2f} {volume_unit}"
        elif shape_type == "rhombus":
            d1 = float(kwargs.get('diagonal1'))
            d2 = float(kwargs.get('diagonal2'))
            area = (d1 * d2) / 2
            return f"Rhombus: Area = {area:.2f} {area_unit}"
        elif shape_type == "ellipse":
            a = float(kwargs.get('semi_major_axis'))
            b = float(kwargs.get('semi_minor_axis'))
            area = math.pi * a * b
            return f"Ellipse: Area = {area:.2f} {area_unit}"
        elif shape_type == "sector":
            radius = float(kwargs.get('radius_sector'))
            angle = float(kwargs.get('angle_sector')) # Assuming angle in degrees as per HTML placeholder
            area = (angle / 360) * math.pi * (radius ** 2)
            return f"Sector: Area = {area:.2f} {area_unit}"
        else:
            return "Unknown shape."
    except ValueError:
        return "Invalid input: Please enter valid numbers for all parameters."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        shape_type = request.form.get('shape_type')
        unit = request.form.get('unit_type', 'units') # Default to 'units' if not selected
        
        # Collect all form parameters into a dictionary
        params = request.form.to_dict()
        
        # Remove shape_type and unit_type from params as they are handled separately
        params.pop('shape_type', None)
        params.pop('unit_type', None)

        # Pass all collected parameters to the calculation function
        result = calculate_area_web(shape_type, unit=unit, **params)
        
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)