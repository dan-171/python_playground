from math import sqrt

class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)

    def get_diagonal(self):
        return sqrt(self.__width**2 + self.__height**2)

    def get_picture(self):
        if self.__width > 50 or self.__height > 50:
            return 'Too big for picture.'
        shape_pic = ""
        for i in range(self.__height):
            for j in range(self.__width):
                shape_pic += "*"
            shape_pic += "\n"
        return shape_pic

    def get_amount_inside(self, shape_2):
        return self.get_area() // shape_2.get_area()

    def __str__(self):
        return f"Rectangle(width={self.__width}, height={self.__height})"
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

    def __str__(self):
        return(f"Square(side={self._Rectangle__width})")

# test case
sqr = Square(5)
print(sqr.get_picture(), "\n")
rect = Rectangle(6, 2)
print(rect.get_picture())