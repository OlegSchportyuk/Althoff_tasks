import math
class Circle():
    def __init__(self,rad):
        self.radius = rad
    def area(self):
        return math.pi*self.radius*self.radius
circle = Circle(10)
print(circle.area())

class Triangle():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        p = (self.a+self.b+self.c)/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
triangle = Triangle(3,3,3)
print(triangle.area())

class Hexagon():
    def __init__(self,a,b,c,d,e,f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
    def calculate_perimeter(self):
        x = [self.a, self.b, self.c, self.d, self.e, self.f]
        perimeter = sum(x)
        return perimeter
hexagon = Hexagon(3,4,2,8,7,5)
print(hexagon.calculate_perimeter())

        
