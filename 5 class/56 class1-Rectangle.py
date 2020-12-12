class Rectangle:
    def __init__(self,width=10,height=10):
        self.__width=width
        self.__height=height
    def get_height(self):
        return self.__height
    def get_width(self):
        return self.width
    def __str__(self):
        return "{} x {}".format(self.__width,self.__height)
    def __repr__(self):
        return "Rectangle({},{})".format(self.__width,self.__height)
    def get_area(self):
        c = self.__width * self.__height
        return c
    def get_perimeter(self):
        d = (self.__width * 2) + (self.__height*2)
        return d


r1 = Rectangle(3, 4)
print(r1.get_area())
print(r1.get_perimeter())
r3 = Rectangle()
print(r3.get_area())
print(r3.get_perimeter())
