class Shape():
    #def __init__(self):
        #pass
    def what_am_i(self):
        print('Я - фигура.')
class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l
    def calculate_perimeter(self):
        return 2*(self.width+self.len)
class Square(Shape):
    square_list = []
    def __init__(self, x):
        self.side = x
        self.square_list.append(self.side)
    def __repr__(self):
        return 'Квадрат {} на {} на {} на {}.'.format(self.side, self.side, self.side, self.side)
    def calculate_perimeter(self):
        return 4*self.side
    def change_size(self, size):
        self.size = size
        self.side = self.side + size
        
rectangle = Rectangle(10,5)
rectangle.what_am_i()
print(rectangle.calculate_perimeter())
square = Square(7)
square.what_am_i()
print(square.calculate_perimeter())
square.change_size(2)
print(square.side)
print(square.calculate_perimeter())

class Horse():
    def __init__(self, name, breed, rider):
        self.name = name
        self.breed = breed
        self.rider = rider
class Rider():
    def __init__(self, name):
        self.name = name
pandil = Rider('Пандик')
horse = Horse('Быстрая','Пони',pandil)
print(horse.rider.name)

#14.1-14.2
square1 = Square(5)
print(Square.square_list)
print(square, square1)
