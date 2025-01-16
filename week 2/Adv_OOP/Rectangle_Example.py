# # Rectangle Example:
class Rectangle:
# class Rectangle():
#     def __init__(what parameters might go here?):
    def __init__(self,width,height):
        self.width =width
        self.height=height
    # What else does the constructor need?

    # # Get the width and height using the getter methods, using the example in the tutorial for syntax.
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def calculate_area(self):
        return self.width * self.height
# # Set new values for width and height using the setter methods
    def set_width(self,width):
         self.width =width
    def set_height(self,height):
         self.height=height
# # Get the updated width and height

# # Add a method to calculate and print the area
    

rectangle = Rectangle(5,3)

initial_width = rectangle.get_width()
print("initial_width:", initial_width)
initial_hight = rectangle.get_height()
print("initial_hight",initial_hight)

area=rectangle.calculate_area()
print("Area:", area)

rectangle.set_width(7)
rectangle.set_height(4)
# Get the updated width and height
updated_width = rectangle.get_width()
updated_height = rectangle.get_height()
print("Updated Width:", updated_width)  # Output: 7
print("Updated Height:", updated_height)  # Output: 4

# Calculate and print the area
area = rectangle.calculate_area()
print("Area:", area)  # Output: 28