from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Define geometry calculation functions (similar to your existing logic)

def calculate_area_web(shape_type, unit= "units", **kwargs):
    """Calculates area based on shape and dimensions provided via web."""
    try:
        if shape_type == "circle":
            radius = float(kwargs.get('radius'))
            area = math.pi * (radius ** 2)
            return f"Area of the circle is {area:.2f} square {unit}"
        elif shape_type == "quadrilateral":
            length = float(kwargs.get('length'))
            width = float(kwargs.get('width'))
            area = length * width
            if length == width:
                return f"The area is {area:.2f} square {unit} (a Square)"
            else:
                return f"The area is {area:.2f} square {unit} (a Rectangle)"
        elif shape_type == "triangle":
            triangle_type = kwargs.get('triangle_type')
            if triangle_type == "right_angle":
                base = float(kwargs.get('base'))
                height = float(kwargs.get('height_ra'))
                area = (base * height) / 2
                return f"The area of the right angle triangle is {area:.2f} square {unit}"
            elif triangle_type == "equilateral":
                side = float(kwargs.get('side_eq'))
                area = ((3**0.5) * side**2) / 4
                return f"The area of the equilateral triangle is {area:.2f} square {unit}"
            elif triangle_type == "isosceles":
                side1 = float(kwargs.get('side1_iso'))
                side2 = float(kwargs.get('side2_iso'))
                area = (side2 * ((4 * side1**2) - side2**2)**0.5) / 4
                return f"The area of the isosceles triangle is {area:.2f} square {unit}"
            elif triangle_type == "scalene":
                side1 = float(kwargs.get('side1_sc'))
                side2 = float(kwargs.get('side2_sc'))
                side3 = float(kwargs.get('side3_sc'))
                s = (side1 + side2 + side3) / 2
                area = (s * (s - side1) * (s - side2) * (s - side3))**0.5
                if area.imag != 0:
                    return "Invalid triangle sides provided. Area cannot be calculated."
                else:
                    return f"The area of the scalene triangle is {area.real:.2f} square {unit}"
            elif triangle_type == "two_sides_one_angle":
                side1 = float(kwargs.get('side1_tsa'))
                side2 = float(kwargs.get('side2_tsa'))
                angle = float(kwargs.get('angle_tsa'))
                area = (side1 * side2 * math.sin(math.radians(angle))) / 2
                return f"The area of the triangle (two sides and angle) is {area:.2f} square {unit}"
            else:
                return "Please select a valid triangle type."
        elif shape_type == "sphere":
            radius = float(kwargs.get('radius_s'))
            surface_area = 4 * math.pi * radius**2
            volume = (4/3) * math.pi * radius**3
            return f"Sphere: Surface Area = {surface_area:.2f} sq {unit}, Volume = {volume:.2f} cubic {unit}"
        elif shape_type == "cylinder":
            radius = float(kwargs.get('radius_c')) # Assuming you named it radius_c in HTML
            height = float(kwargs.get('height_c'))
            surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius**2
            volume = math.pi * radius**2 * height
            return f"Cylinder: Surface Area = {surface_area:.2f} sq {unit}, Volume = {volume:.2f} cubic {unit}"
        elif shape_type == "Trapezium":
            base1 = float(kwargs.get('base1_t'))
            base2 = float(kwargs.get('base2_t'))
            height = float(kwargs.get('height_t'))
            area = ((base1 + base2) / 2) * height
            return f"Trapezium: Area = {area:.2f} square {unit}"
        elif shape_type == "parallelogram":
            base = float(kwargs.get('base_p'))
            height = float(kwargs.get('height_p'))
            area = base * height
            return f"Parallelogram: Area = {area:.2f} square {unit}"
        elif shape_type == "pentagon":
            side = float(kwargs.get('side_p'))
            area = (5 * side**2) / (4 * math.tan(math.pi / 5))
            return f"Pentagon: Area = {area:.2f} square {unit}"
        elif shape_type == "hexagon":
            side = float(kwargs.get('side_h'))
            area = (3 * math.sqrt(3) * side**2) / 2
            return f"Hexagon: Area = {area:.2f} square {unit}"
        elif shape_type == "cuboid":
            side = float(kwargs.get('side_cb'))
            surface_area = 6 * (side ** 2)
            volume = side ** 3
            return f"Cuboid: Surface Area = {surface_area:.2f} sq {unit}, Volume = {volume:.2f} cubic {unit}"
        elif shape_type == "cone":
            radius = float(kwargs.get('radius_co'))
            height = float(kwargs.get('height_co'))
            slant_height = (radius**2 + height**2)**0.5
            surface_area = math.pi * radius * (radius + slant_height)
            volume = (1/3) * math.pi * radius**2 * height
            return f"Cone: Surface Area = {surface_area:.2f} sq {unit}, Volume = {volume:.2f} cubic {unit}"
        elif shape_type == "pyramid":
            base_length = float(kwargs.get('base_length_p'))
            base_width = float(kwargs.get('base_width_p'))
            height = float(kwargs.get('height_p'))
            base_area = base_length * base_width
            slant_height = ((base_length / 2)**2 + height**2)**0.5
            lateral_area = (base_length + base_width) * slant_height
            surface_area = base_area + lateral_area
            volume = (1/3) * base_area * height
            return f"Pyramid: Surface Area = {surface_area:.2f} sq {unit}, Volume = {volume:.2f} cubic {unit}"
        elif shape_type == "rhombus":
            diagonal1 = float(kwargs.get('diagonal1_r'))
            diagonal2 = float(kwargs.get('diagonal2_r'))
            area = (diagonal1 * diagonal2) / 2
            return f"Rhombus: Area = {area:.2f} square {unit}"
        elif shape_type == "ellipse":
            semi_major_axis = float(kwargs.get('semi_major_axis_e'))
            semi_minor_axis = float(kwargs.get('semi_minor_axis_e'))
            area = math.pi * semi_major_axis * semi_minor_axis
            return f"Ellipse: Area = {area:.2f} square {unit}"
        elif shape_type == "sector":
            radius = float(kwargs.get('radius_se'))
            angle = float(kwargs.get('angle_se'))
            area = (math.pi * radius**2 * angle) / 360
            return f"Sector: Area = {area:.2f} square {unit}"
        else:
            return "Invalid shape type selected."
    except ValueError:
        return "Error: Please enter valid numerical inputs."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
   

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        shape_type = request.form.get('shape_type')
        unit = request.form.get('unit_type', 'units')
        if shape_type == 'circle':
            radius = request.form.get('radius')
            result = calculate_area_web(shape_type, unit=unit, radius=radius)
        elif shape_type == 'quadrilateral':
            length = request.form.get('length')
            width = request.form.get('width')
            result = calculate_area_web(shape_type, unit=unit, length=length, width=width)
        elif shape_type == 'triangle':
            triangle_type = request.form.get('triangle_type')
            # Collect specific triangle inputs based on its type
            if triangle_type == "right_angle":
                base = request.form.get('base')
                height_ra = request.form.get('height_ra')
                result = calculate_area_web(shape_type, unit=unit, triangle_type=triangle_type, base=base, height_ra=height_ra)
            elif triangle_type == "equilateral":
                side_eq = request.form.get('side_eq')
                result = calculate_area_web(shape_type, unit=unit, triangle_type=triangle_type, side_eq=side_eq)
            elif triangle_type == "isosceles":
                side1_iso = request.form.get('side1_iso')
                side2_iso = request.form.get('side2_iso')
                result = calculate_area_web(shape_type, unit=unit, triangle_type=triangle_type, side1_iso=side1_iso, side2_iso=side2_iso)
            elif triangle_type == "scalene":
                side1_sc = request.form.get('side1_sc')
                side2_sc = request.form.get('side2_sc')
                side3_sc = request.form.get('side3_sc')
                result = calculate_area_web(shape_type, unit=unit, triangle_type=triangle_type, side1_sc=side1_sc, side2_sc=side2_sc, side3_sc=side3_sc)
            elif triangle_type == "two_sides_one_angle":
                side1_tsa = request.form.get('side1_tsa')
                side2_tsa = request.form.get('side2_tsa')
                angle_tsa = request.form.get('angle_tsa')
                result = calculate_area_web(shape_type, unit=unit, triangle_type=triangle_type, side1_tsa=side1_tsa, side2_tsa=side2_tsa, angle_tsa=angle_tsa)
            else:
                result = "Please select a valid triangle type."
        elif shape_type == 'sphere':
            radius_s = request.form.get('radius_s')
            result = calculate_area_web(shape_type, unit=unit, radius_s=radius_s)
        elif shape_type == 'cylinder':
            radius_c = request.form.get('radius_c')
            height_c = request.form.get('height_c')
            result = calculate_area_web(shape_type, unit=unit, radius_c=radius_c, height_c=height_c)
        elif shape_type == 'Trapezium':
            base1_t = request.form.get('base1_t')
            base2_t = request.form.get('base2_t')
            height_t = request.form.get('height_t')
            result = calculate_area_web(shape_type, unit=unit, base1_t=base1_t, base2_t=base2_t, height_t=height_t)
        elif shape_type == 'parallelogram':
            base_p = request.form.get('base_p')
            height_p = request.form.get('height_p')
            result = calculate_area_web(shape_type, unit=unit, base_p=base_p, height_p=height_p)
        elif shape_type == 'pentagon':
            side_p = request.form.get('side_p')
            result = calculate_area_web(shape_type, unit=unit, side_p=side_p)
        elif shape_type == 'hexagon':
            side_h = request.form.get('side_h')
            result = calculate_area_web(shape_type, unit=unit, side_h=side_h)
        elif shape_type == 'cuboid':
            side_cb = request.form.get('side_cb')
            result = calculate_area_web(shape_type, unit=unit, side_cb=side_cb)
        elif shape_type == 'cone':
            radius_co = request.form.get('radius_co')
            height_co = request.form.get('height_co')
            result = calculate_area_web(shape_type, unit=unit, radius_co=radius_co, height_co=height_co)
        elif shape_type == 'pyramid':
            base_length_p = request.form.get('base_length_p')
            base_width_p = request.form.get('base_width_p')
            height_p = request.form.get('height_p')
            result = calculate_area_web(shape_type, unit=unit, base_length_p=base_length_p, base_width_p=base_width_p, height_p=height_p)
        elif shape_type == 'rhombus':
            diagonal1_r = request.form.get('diagonal1_r')
            diagonal2_r = request.form.get('diagonal2_r')
            result = calculate_area_web(shape_type, unit=unit, diagonal1_r=diagonal1_r, diagonal2_r=diagonal2_r)
        elif shape_type == 'ellipse':
            semi_major_axis_e = request.form.get('semi_major_axis_e')
            semi_minor_axis_e = request.form.get('semi_minor_axis_e')
            result = calculate_area_web(shape_type, unit=unit, semi_major_axis_e=semi_major_axis_e, semi_minor_axis_e=semi_minor_axis_e)
        elif shape_type == 'sector':
            radius_se = request.form.get('radius_se')
            angle_se = request.form.get('angle_se')
            result = calculate_area_web(shape_type, unit=unit, radius_se=radius_se, angle_se=angle_se)

        else:
            result = "Please select a valid shape."

    # Render the HTML template, passing the result to it
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True) # debug=True allows auto-reloading and shows errors