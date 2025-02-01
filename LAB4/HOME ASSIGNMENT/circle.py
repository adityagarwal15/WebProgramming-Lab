import math

class Circle:
    def __init__(self, radius):
        # Initialize the circle with a radius
        self.radius = radius
    
    def area(self):
        # Calculate the area of the circle: A = π * r^2
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        # Calculate the perimeter (circumference) of the circle: P = 2 * π * r
        return 2 * math.pi * self.radius

# Taking input from the user for the radius
radius = float(input("Enter the radius of the circle: "))

# Create an instance of the Circle class
circle = Circle(radius)

# Calculate and print the area and perimeter of the circle
print(f"The area of the circle is: {circle.area():.2f}")
print(f"The perimeter (circumference) of the circle is: {circle.perimeter():.2f}")
