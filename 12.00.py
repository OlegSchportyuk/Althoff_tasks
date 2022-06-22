class Orange():
    def __init__(self,w,c):
        """вес в граммах"""
        self.weight = w
        self.color = c
        self.mold = 0
        print('Создано!')
    def rot(self, days, temp):
        self.mold = days*temp

orange = Orange(6, 'апельсин')
print(orange.mold)
orange.rot(10,33)
print(orange.mold)

class Rectangle():
    def __init__(self,w,l):
        self.width = w
        self.len = l
    def area(self):
        return self.width*self.len
    def change_size(self,w,l):
        self.width = w
        self.len = l
rect = Rectangle(10,20)
print(rect.area())
rect.change_size(20,40)
print(rect.area())

