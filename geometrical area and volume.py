
import math
pi = 3.141592 # You can keep this or use math.pi directly

def calculate_area():


        # Define all available geometry types
        available_geometries = [
        "circle", "quadrilateral", "triangle", "sphere", "cylinder",
        "trapezium", "parallelogram", "pentagon", "hexagon", "cuboid",
        "cone", "pyramid", "rhombus", "ellipse", "sector"
        ]

        while True: 
            print("\n Select a Geometry Type")
            for i, geo_type in enumerate(available_geometries):
                print(f"{i+1}. {geo_type.replace('_', ' ').title()}") # Display with 1-based indexing and nice formatting
            print("Type 'exit' to quit the program.")
            
            user_input = input("Enter your choice (number or 'exit'): ").lower()

            if user_input == 'exit':
                print("Exiting the program. Goodbye! 👋")
                break # Exit the while loop

            try:
                choice_index = int(user_input) - 1 # Convert to 0-based index
                if 0 <= choice_index < len(available_geometries):
                    geometry_type = available_geometries[choice_index]
                    print(f"\nYou selected: {geometry_type.replace('_', ' ').title()}")
                else:
                    print(" Invalid number. Please enter a number from the list or 'exit'.")
                    continue # Skip to the next iteration of the loop
            except ValueError:
                print(" Invalid input. Please enter a number or 'exit'.")
                continue # Skip to the next iteration of the loop

        
            # Area of circle
            if geometry_type== "circle":
                radius=float(input("Enter the radius of the circle: "))
                area= radius**2 * pi
                print(f"Area of the circle is {area} square units")
            
            # Area of quadrilateral
            if geometry_type== "quadrilateral":
                length=float(input("Enter the length of the quadrilateral: "))
                width=float(input("Enter the width of the quadrilateral: "))
                area= length * width
                if length> width or length< width:
                    print("its a rectangle")
                if length == width:
                    print("its a square")
                print(f"The area is {area} square units")

            #area of triangle
            if geometry_type== "triangle":
                triangle_type = input("Enter the type of triangle (right angle/isosceles/equilateral/scalene, Two sides and one angle): ").lower()
                if triangle_type== "right angle":
                        base= float(input("Enter the base of the triangle: "))
                        height= float(input("Enter the hight of the triangle: "))
                        area= (base*height)/2
                        print(f"The area right angle triangle is {area} square units")
                elif triangle_type== "equilateral":
                        side= float(input("Enter the side of the triangle: "))
                        area= ((3**0.5)*side**2)/4
                        print(f"The area equilateral triangle is {area} square units")
                elif triangle_type== "isosceles":
                        side1= float(input("Enter the side1 of the triangle: "))
                        side2= float(input("Enter the side2 of the triangle: "))
                        area= (side2* ((4*side1**2)- side2**2)**0.5)/4
                        print(f"The area isosceles triangle is {area} square units")
                elif triangle_type== "scalene":
                        side1= float(input("Enter the side1 of the triangle: "))
                        side2= float(input("Enter the side2 of the triangle: "))
                        side3= float(input("Enter the side3 of the triangle: "))
                        s = (side1+ side2+ side3)/2
                        area= (s*(s-side1)*(s-side2)*(s-side3))**0.5
                        print(f"The area scalene triangle is {area} square units")
                elif triangle_type== "two sides and one angle":
                        side1= float(input("Enter the side1 of the triangle: "))
                        side2= float(input("Enter the side2 of the triangle: "))
                        angle= float(input("Enter the angle in degrees: "))
                        area= (side1*side2*math.sin(math.radians(angle)))/2
                        print(f"The area two sides and one angle triangle is {area} square units")

            # Surface Area and volume of Sphere
            if geometry_type== "sphere":
                radius= float(input("Enter the radius of the sphere: "))
                area= 4 * pi * radius**2
                volume= (4/3) * pi * radius**3
                print(f"The surface area of the sphere is {area} square units and volume is {volume} cubic units")
            
            #surface area and volume of cylinder
            if geometry_type== "cylinder":
                radius= float(input("Enter the radius of the cylinder: "))
                height= float(input("Enter the height of the cylinder: "))
                surface_area= 2 * pi * radius * height + 2 * pi * radius**2
                volume= pi * radius**2 * height
                print(f"The surface area of the cylinder is {surface_area} square units and volume is {volume} cubic units")
            
            # area of trapezium
            if geometry_type== "trapezium":
                base1= float(input("Enter the length of the first base of the trapezium: "))
                base2= float(input("Enter the length of the second base of the trapezium: "))
                height= float(input("Enter the height of the trapezium: "))
                area= ((base1 + base2) * height) / 2
                print(f"The area of the trapezium is {area} square units")
            
            #area of parallelogram
            if geometry_type== "parallelogram":
                base= float(input("Enter the base of the parallelogram: "))
                height= float(input("Enter the height of the parallelogram: "))
                area= base * height
                print(f"The area of the parallelogram is {area} square units")  

            #area of pentagon
            if geometry_type== "pentagon":
                side= float(input("Enter the length of a side of the pentagon: "))
                area= (5/4) * (side**2) / math.tan(math.pi/5)
                print(f"The area of the pentagon is {area} square units")
            
            #area of hexagon
            if geometry_type== "hexagon":
                side= float(input("Enter the length of a side of the hexagon: "))
                area= (3 * math.sqrt(3) * side**2) / 2
                print(f"The area of the hexagon is {area} square units")
            
            # surface area and volume of cuboid
            if geometry_type== "cuboid":
                length= float(input("Enter the length of the cuboid: "))
                width= float(input("Enter the width of the cuboid: "))
                height= float(input("Enter the height of the cuboid: "))
                surface_area= 2 * (length * width + width * height + height * length)
                volume= length * width * height
                print(f"The surface area of the cuboid is {surface_area} square units and volume is {volume} cubic units")
            
            # Surface area and volume of cone
            if geometry_type== "cone":
                radius= float(input("Enter the radius of the cone: "))
                height= float(input("Enter the height of the cone: "))
                slant_height= (radius**2 + height**2)**0.5
                surface_area= pi * radius * slant_height + pi * radius**2
                volume= (1/3) * pi * radius**2 * height
                print(f"The surface area of the cone is {surface_area} square units and volume is {volume} cubic units")

            # Surface area and volume of pyramid
            if geometry_type== "pyramid":
                base_length= float(input("Enter the length of the base of the pyramid: "))
                height= float(input("Enter the height of the pyramid: "))
                slant_height= (base_length**2 + height**2)**0.5
                surface_area= base_length**2 + 2 * base_length * slant_height
                volume= (1/3) * base_length**2 * height
                print(f"The surface area of the pyramid is {surface_area} square units and volume is {volume} cubic units")
            
            # area of rhombus or kite
            if geometry_type== "rhombus":   
                diagonal1= float(input("Enter the length of the first diagonal of the rhombus: "))
                diagonal2= float(input("Enter the length of the second diagonal of the rhombus: "))
                area= (diagonal1 * diagonal2) / 2
                print(f"The area of the rhombus is {area} square units")        

            # area of ellipse
            if geometry_type== "ellipse":   
                semi_major_axis= float(input("Enter the length of the semi-major axis of the ellipse: "))
                semi_minor_axis= float(input("Enter the length of the semi-minor axis of the ellipse: "))
                area= pi * semi_major_axis * semi_minor_axis
                print(f"The area of the ellipse is {area} square units")
            
            # area of sector
            if geometry_type== "sector":
                radius= float(input("Enter the radius of the sector: "))
                angle= float(input("Enter the angle of the sector (in degrees): "))
                area= (angle / 360) * pi * radius**2
                print(f"The area of the sector is {area} square units")


calculate_area()
    



