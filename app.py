from flask import Flask, render_template, request
import math
import sys  # keep debug to stderr

app = Flask(__name__)

# ---------- helpers ----------
def _num(value, label, *, min_value=0.0):
    """Parse a float with a min-value guard and friendly errors."""
    if value is None or (isinstance(value, str) and value.strip() == ""):
        raise ValueError(f"{label} is required.")
    try:
        v = float(value)
    except Exception:
        raise ValueError(f"{label} must be a valid number.")
    if v < min_value:
        raise ValueError(f"{label} must be \u2265 {min_value}.")
    return v


def _units(unit):
    """Return (area_unit, volume_unit) based on selected unit string."""
    area_unit = f"sq {unit}"
    volume_unit = f"cubic {unit}"

    if unit == "meters":
        area_unit, volume_unit = "m\u00b2", "m\u00b3"
    elif unit == "centimeters":
        area_unit, volume_unit = "cm\u00b2", "cm\u00b3"
    elif unit == "millimeters":
        area_unit, volume_unit = "mm\u00b2", "mm\u00b3"
    elif unit == "inches":
        area_unit, volume_unit = "in\u00b2", "in\u00b3"
    elif unit == "feet":
        area_unit, volume_unit = "ft\u00b2", "ft\u00b3"

    return area_unit, volume_unit


# ---------- core ----------
def calculate_area_web(shape_type, unit="units", **kwargs):
    """
    Compute a result string for display. Returns user-friendly error text on any invalid input.
    """
    try:
        area_unit, volume_unit = _units(unit)

        if shape_type == "circle":
            radius = _num(kwargs.get("radius"), "Radius")
            area = math.pi * (radius ** 2)
            return f"Area of the circle is {area:.2f} {area_unit}"

        elif shape_type == "quadrilateral":
            length = _num(kwargs.get("length"), "Length")
            width = _num(kwargs.get("width"), "Width")
            area = length * width
            if abs(length - width) < 1e-12:
                return f"The area is {area:.2f} {area_unit} (a Square)"
            else:
                return f"The area is {area:.2f} {area_unit} (a Rectangle)"

        elif shape_type == "triangle":
            triangle_type = (kwargs.get("triangle_type") or "right_angle").strip()

            if triangle_type == "right_angle":
                base = _num(kwargs.get("base"), "Base")
                height = _num(kwargs.get("height"), "Height")
                area = 0.5 * base * height
                return f"The area of the right angle triangle is {area:.2f} {area_unit}"

            elif triangle_type == "equilateral":
                side = _num(kwargs.get("side"), "Side")
                area = (math.sqrt(3) / 4) * (side ** 2)
                return f"The area of the equilateral triangle is {area:.2f} {area_unit}"

            elif triangle_type == "isosceles":
                base = _num(kwargs.get("base"), "Base")
                side = _num(kwargs.get("side"), "Equal Side")
                if side <= base / 2:
                    return "Invalid isosceles triangle: Equal side must be greater than half the base."
                height = math.sqrt(side**2 - (base/2)**2)
                area = 0.5 * base * height
                return f"The area of the isosceles triangle is {area:.2f} {area_unit}"

            elif triangle_type == "scalene":
                a = _num(kwargs.get("side_a"), "Side a")
                b = _num(kwargs.get("side_b"), "Side b")
                c = _num(kwargs.get("side_c"), "Side c")
                if not (a + b > c and a + c > b and b + c > a):
                    return "Invalid scalene triangle: Sides do not form a valid triangle."
                s = (a + b + c) / 2
                val = max(s * (s - a) * (s - b) * (s - c), 0.0)
                area = math.sqrt(val)
                return f"The area of the scalene triangle is {area:.2f} {area_unit}"

            elif triangle_type == "two_sides_one_angle":
                side1 = _num(kwargs.get("side1"), "Side 1")
                side2 = _num(kwargs.get("side2"), "Side 2")
                angle = _num(kwargs.get("angle"), "Angle (degrees)")
                if not (0 < angle < 180):
                    return "Invalid angle: Angle must be between 0 and 180 degrees."
                area = 0.5 * side1 * side2 * math.sin(math.radians(angle))
                return f"The area of the triangle is {area:.2f} {area_unit}"

            else:
                return "Unknown triangle type."

        elif shape_type == "pyramid":
            base_length = _num(kwargs.get("base_length"), "Base Length")
            height = _num(kwargs.get("height_py"), "Height")
            base_area = base_length * base_length
            slant_height_face = math.sqrt((base_length / 2)**2 + height**2)
            surface_area = base_area + 2 * base_length * slant_height_face
            volume = (1/3) * base_area * height
            return f"Pyramid: Surface Area = {surface_area:.2f} {area_unit}, Volume = {volume:.2f} {volume_unit}"

        elif shape_type == "sphere":
            radius = _num(kwargs.get("radius_sphere"), "Radius")
            area = 4 * math.pi * (radius ** 2)
            volume = (4/3) * math.pi * (radius ** 3)
            return f"Sphere: Surface Area = {area:.2f} {area_unit}, Volume = {volume:.2f} {volume_unit}"

        elif shape_type == "cylinder":
            radius = _num(kwargs.get("radius_cylinder"), "Radius")
            height = _num(kwargs.get("height_cylinder"), "Height")
            surface_area = 2 * math.pi * radius * (radius + height)
            volume = math.pi * (radius ** 2) * height
            return f"Cylinder: Surface Area = {surface_area:.2f} {area_unit}, Volume = {volume:.2f} {volume_unit}"

        elif shape_type == "trapezium":
            a = _num(kwargs.get("base1"), "Base 1")
            b = _num(kwargs.get("base2"), "Base 2")
            height = _num(kwargs.get("height_trapezium"), "Height")
            area = 0.5 * (a + b) * height
            return f"Trapezium: Area = {area:.2f} {area_unit}"

        elif shape_type == "parallelogram":
            base = _num(kwargs.get("base_para"), "Base")
            height = _num(kwargs.get("height_para"), "Height")
            area = base * height
            return f"Parallelogram: Area = {area:.2f} {area_unit}"

        elif shape_type == "pentagon":
            side = _num(kwargs.get("side_pentagon"), "Side")
            area = (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (side ** 2)
            return f"Pentagon: Area = {area:.2f} {area_unit}"

        elif shape_type == "hexagon":
            side = _num(kwargs.get("side_hexagon"), "Side")
            area = (3 * math.sqrt(3) / 2) * (side ** 2)
            return f"Hexagon: Area = {area:.2f} {area_unit}"

        elif shape_type == "cuboid":
            length = _num(kwargs.get("length_cuboid"), "Length")
            width = _num(kwargs.get("width_cuboid"), "Width")
            height = _num(kwargs.get("height_cuboid"), "Height")
            surface_area = 2 * (length * width + length * height + width * height)
            volume = length * width * height
            return f"Cuboid: Surface Area = {surface_area:.2f} {area_unit}, Volume = {volume:.2f} {volume_unit}"

        elif shape_type == "cone":
            radius = _num(kwargs.get("radius_cone"), "Radius")
            height = _num(kwargs.get("height_cone"), "Height")
            slant_height = math.sqrt(max(radius**2 + height**2, 0.0))
            surface_area = math.pi * radius * (radius + slant_height)
            volume = (1/3) * math.pi * (radius ** 2) * height
            return f"Cone: Surface Area = {surface_area:.2f} {area_unit}, Volume = {volume:.2f} {volume_unit}"

        elif shape_type == "rhombus":
            d1 = _num(kwargs.get("diagonal1"), "Diagonal 1")
            d2 = _num(kwargs.get("diagonal2"), "Diagonal 2")
            area = (d1 * d2) / 2
            return f"Rhombus: Area = {area:.2f} {area_unit}"

        elif shape_type == "ellipse":
            a = _num(kwargs.get("semi_major_axis"), "Semi-Major Axis")
            b = _num(kwargs.get("semi_minor_axis"), "Semi-Minor Axis")
            area = math.pi * a * b
            return f"Ellipse: Area = {area:.2f} {area_unit}"

        elif shape_type == "sector":
            radius = _num(kwargs.get("radius_sector"), "Radius")
            angle = _num(kwargs.get("angle_sector"), "Angle (degrees)")
            if angle < 0 or angle > 360:
                return "Invalid angle: Angle must be between 0 and 360 degrees."
            area = (angle / 360.0) * math.pi * (radius ** 2)
            return f"Sector: Area = {area:.2f} {area_unit}"

        else:
            return "Unknown shape."

    except ValueError as ve:
        return str(ve)
    except Exception as e:
        # Keep user-facing message generic; details are in logs
        print(f"[Internal Error] {e}", file=sys.stderr)
        return "An unexpected error occurred. Please check your inputs and try again."


@app.route('/', methods=['GET', 'POST'])
def index():
    print(f"Request method: {request.method}", file=sys.stderr)

    result = None
    shape_type = None  # ensure it always exists

    if request.method == 'POST':
        form_dict = request.form.to_dict()
        print(f"Form data: {form_dict}", file=sys.stderr)

        shape_type = form_dict.get('shape_type')
        unit = form_dict.get('unit_type', 'units')

        # Pass all params EXCEPT selectors
        params = dict(form_dict)
        params.pop('shape_type', None)
        params.pop('unit_type', None)

        result = calculate_area_web(shape_type, unit=unit, **params)
        print(f"Result to template: {result}", file=sys.stderr)

    return render_template('index.html', result=result, shape_type=shape_type)


if __name__ == '__main__':
    app.run(debug=True)
