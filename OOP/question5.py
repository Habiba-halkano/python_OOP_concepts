#constructor overloading
class Rectangle:
    def __init__(self, width=2, height=None):
        #if height is not provided, use width for both width and height(square)
        if height is None:
            self.width = width
            self.height = width
        else:
         self.width = width
         self.height = height

    def area(self):
        return self.width * self.height

#for square:
square1 = Rectangle(5)
print(f"area of square is {square1.area()}")
#for rectangle
rec1 = Rectangle(5,3)
print(f"area of rectangle is {rec1.area()}")