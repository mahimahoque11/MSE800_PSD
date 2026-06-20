class RectangleLand:
    def __init__(self, length, width):
        # Initializes the object's attributes, similar to the Box class
        self.length = length
        self.width = width

    def area(self):
        # Returns the calculation based on instance attributes
        return self.length * self.width

    def perimeter(self):
        # Uses the 2D perimeter formula (2 * (L + W))
        return 2 * (self.length + self.width)
    
    def print_dimensions(self):
        # Prints the stored dimensions, matching the sample's print_dimensions
        print(f"Length: {self.length}, Width: {self.width}")