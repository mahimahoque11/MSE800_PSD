# Import the specific class from your file name
from rectangleland import RectangleLand 

def main():
    print("Welcome to the Land Measurement System!")

    
    try:
        length = float(input("Enter the length of the land: "))
        width = float(input("Enter the width of the land: "))

        # Use the correct class name: RectangleLand
        my_land = RectangleLand(length, width)

        print("\nLand Details:")
        my_land.print_dimensions()
        print(f"Area: {my_land.area()}")
        print(f"Perimeter: {my_land.perimeter()}")

    except ValueError: 
        print("Invalid input. Please enter numeric values for length and width.")

if __name__ == "__main__": 
    main()