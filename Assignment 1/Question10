import turtle
import sys

def draw_square(side_length, color):
    """Draw a square with given side length and color"""
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)
    turtle.end_fill()

def draw_triangle(side_length, color):
    """Draw an equilateral triangle with given side length and color"""
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)
    turtle.end_fill()

def draw_circle(radius, color):
    """Draw a circle with given radius and color"""
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_rectangle(width, height, color):
    """Draw a rectangle with given width, height and color"""
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def get_color():
    """Get valid color input from user"""
    colors = ["red", "green", "blue", "yellow", "orange", "purple", "black", "pink"]
    while True:
        color = input("Enter fill color: ").lower()
        if color in colors:
            return color
        print(f"Available colors: {', '.join(colors)}")

def get_positive_number(prompt):
    """Get positive number input from user"""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    turtle.speed(1)
    turtle.title("Turtle Geometric Shapes Drawing Program")
    
    print("\nWelcome to the Turtle Geometric Shapes Drawing Program!")
    
    while True:
        print("\nSelect the shape to draw:")
        print("1 - Square")
        print("2 - Triangle")
        print("3 - Circle")
        print("4 - Rectangle")
        print("0 - Exit")
        
        choice = input("Enter your choice (or 0 to exit): ")
        
        if choice == '0':
            print("Thank you for using the program. Goodbye!")
            turtle.bye()
            sys.exit()
        elif choice == '1':
            size = get_positive_number("Enter side length for square: ")
            color = get_color()
            draw_square(size, color)
            print(f"Drew a {color} square with side length {size}")
        elif choice == '2':
            size = get_positive_number("Enter side length for triangle: ")
            color = get_color()
            draw_triangle(size, color)
            print(f"Drew a {color} equilateral triangle with side length {size}")
        elif choice == '3':
            radius = get_positive_number("Enter radius for circle: ")
            color = get_color()
            draw_circle(radius, color)
            print(f"Drew a {color} circle with radius {radius}")
        elif choice == '4':
            width = get_positive_number("Enter width for rectangle: ")
            height = get_positive_number("Enter height for rectangle: ")
            color = get_color()
            draw_rectangle(width, height, color)
            print(f"Drew a {color} rectangle with width {width} and height {height}")
        else:
            print("Invalid choice. Please enter a number between 0-4.")

if __name__ == "__main__":
    main()