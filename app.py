from flask import Flask, render_template, request
import math

app = Flask(__name__)

def calculate_area_web(shape_type, unit="units", **kwargs):
    try:
        if shape_type == "circle":
            radius = float(kwargs.get('radius'))
            area = math.pi * (radius ** 2)
            return f"Area of the circle is {area:.2f} sq {unit}"
        elif shape_type == "quadrilateral":
            length = float(kwargs.get('length'))
            width = float(kwargs.get('width'))
            area = length * width
            if length == width:
                return f"The area is {area:.2f} sq {unit} (a Square)"
            else:
                return f"The area is {area:.2f} sq {unit} (a Rectangle)"
        elif shape_type == "triangle":
            triangle_type = kwargs.get('triangle_type', 'right_angle')
            if triangle_type == 'right_angle':
                base = float(kwargs.get('base'))
                height = float(kwargs.get('height'))
                area = 0.5 * base * height
                return f"The area of the right angle triangle is {area:.2f} sq {unit}"
            elif triangle_type == 'equilateral':
                side = float(kwargs.get('side'))
                area = (math.sqrt(3) / 4) * (side ** 2)
                return f"The area of the equilateral triangle is {area:.2f} sq {unit}"
            elif triangle_type == 'isosceles':
                base = float(kwargs.get('base'))
                side = float(kwargs.get('side'))
                height = math.sqrt(side**2 - (base/2)**2)
                area = 0.5 * base * height
                return f"The area of the isosceles triangle is {area:.2f} sq {unit}"
            elif triangle_type == 'scalene':
                a = float(kwargs.get('side_a'))
                b = float(kwargs.get('side_b'))
                c = float(kwargs.get('side_c'))
                s = (a + b + c) / 2
                area = math.sqrt(s * (s - a) * (s - b) * (s - c))
                return f"The area of the scalene triangle is {area:.2f} sq {unit}"
            elif triangle_type == 'two_sides_one_angle':
                side1 = float(kwargs.get('side1'))
                side2 = float(kwargs.get('side2'))
                angle = float(kwargs.get('angle'))
                area = 0.5 * side1 * side2 * math.sin(math.radians(angle))
                return f"The area of the triangle is {area:.2f} sq {unit}"
            else:
                return "Unknown triangle type."
        elif shape_type == "pyramid":
            base_length = float(kwargs.get('base_length'))
            base_width = float(kwargs.get('base_width'))
            height = float(kwargs.get('height'))
            base_area = base_length * base_width
            volume = (1/3) * base_area * height
            return f"Pyramid: Base Area = {base_area:.2f} sq {unit}, Volume = {volume:.2f} cubic {unit}"
        elif shape_type == "sphere":
            radius = float(kwargs.get('radius'))
            area = 4 * math.pi * (radius ** 2)
            volume = (4/3) * math.pi * (radius ** 3)
            return f"Sphere: Surface Area = {area:.2f} sq {unit}, Volume = {volume:.2f} cubic {unit}"
        elif shape_type == "cylinder":
            radius = float(kwargs.get('radius'))
            height = float(kwargs.get('height'))
            area = 2 * math.pi * radius * (radius + height)
            volume = math.pi * (radius ** 2) * height
            return f"Cylinder: Surface Area = {area:.2f} sq {unit}, Volume = {volume:.2f} cubic {unit}"
        elif shape_type == "trapezium":
            a = float(kwargs.get('a'))
            b = float(kwargs.get('b'))
            height = float(kwargs.get('height'))
            area = 0.5 * (a + b) * height
            return f"Trapezium: Area = {area:.2f} sq {unit}"
        elif shape_type == "parallelogram":
            base = float(kwargs.get('base'))
            height = float(kwargs.get('height'))
            area = base * height
            return f"Parallelogram: Area = {area:.2f} sq {unit}"
        elif shape_type == "pentagon":
            side = float(kwargs.get('side'))
            area = (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (side ** 2)
            return f"Pentagon: Area = {area:.2f} sq {unit}"
        elif shape_type == "hexagon":
            side = float(kwargs.get('side'))
            area = (3 * math.sqrt(3) / 2) * (side ** 2)
            return f"Hexagon: Area = {area:.2f} sq {unit}"
        elif shape_type == "cuboid":
            length = float(kwargs.get('length'))
            width = float(kwargs.get('width'))
            height = float(kwargs.get('height'))
            surface_area = 2 * (length * width + length * height + width * height)
            volume = length * width * height
            return f"Cuboid: Surface Area = {surface_area:.2f} sq {unit}, Volume = {volume:.2f} cubic {unit}"
        elif shape_type == "cone":
            radius = float(kwargs.get('radius'))
            height = float(kwargs.get('height'))
            slant_height = math.sqrt(radius**2 + height**2)
            surface_area = math.pi * radius * (radius + slant_height)
            volume = (1/3) * math.pi * (radius ** 2) * height
            return f"Cone: Surface Area = {surface_area:.2f} sq {unit}, Volume = {volume:.2f} cubic {unit}"
        elif shape_type == "rhombus":
            d1 = float(kwargs.get('d1'))
            d2 = float(kwargs.get('d2'))
            area = (d1 * d2) / 2
            return f"Rhombus: Area = {area:.2f} sq {unit}"
        elif shape_type == "ellipse":
            a = float(kwargs.get('a'))
            b = float(kwargs.get('b'))
            area = math.pi * a * b
            return f"Ellipse: Area = {area:.2f} sq {unit}"
        elif shape_type == "sector":
            radius = float(kwargs.get('radius'))
            angle = float(kwargs.get('angle'))
            area = (angle / 360) * math.pi * (radius ** 2)
            return f"Sector: Area = {area:.2f} sq {unit}"
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
        unit = request.form.get('unit_type', 'units')
        params = request.form.to_dict()
        # Required fields for each shape
        required_fields = {
            'circle': ['radius'],
            'quadrilateral': ['length', 'width'],
            'triangle': ['triangle_type'],  # triangle_type will determine further
            'pyramid': ['base_length', 'base_width', 'height'],
            'sphere': ['radius'],
            'cylinder': ['radius', 'height'],
            'trapezium': ['a', 'b', 'height'],
            'parallelogram': ['base', 'height'],
            'pentagon': ['side'],
            'hexagon': ['side'],
            'cuboid': ['length', 'width', 'height'],
            'cone': ['radius', 'height'],
            'rhombus': ['d1', 'd2'],
            'ellipse': ['a', 'b'],
            'sector': ['radius', 'angle'],
        }
        # For triangles, check sub-type
        if shape_type == 'triangle':
            triangle_type = params.get('triangle_type', 'right_angle')
            triangle_fields = {
                'right_angle': ['base', 'height'],
                'equilateral': ['side'],
                'isosceles': ['base', 'side'],
                'scalene': ['side_a', 'side_b', 'side_c'],
                'two_sides_one_angle': ['side1', 'side2', 'angle'],
            }
            required = ['triangle_type'] + triangle_fields.get(triangle_type, [])
        else:
            required = required_fields.get(shape_type, [])
        # Check for missing fields
        missing = [field for field in required if not params.get(field)]
        if missing:
            result = f"Please enter values for: {', '.join(missing)}"
        else:
            result = calculate_area_web(shape_type, unit=unit, **params)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)