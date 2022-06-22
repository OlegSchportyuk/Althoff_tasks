class Data:
    def __init__(self):
        self.nums = [1,2,3,4,5]
    def change_data(self,index,n):
        self.nums[index] = n
data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)
data_two = Data()
data_two.change_data(0,100)
print(data_two.nums)

class Shape():
    def __init__(self,w,l):
        self.width=w
        self.len =l
    def print_size(self):
        print("""{} на {}""".format(self.width,self.len))
my_shape = Shape(20,25)
my_shape.print_size()

class Square(Shape):
    def area(self):
        return self.width*self.len
    #def print_size(self):
        #print("""Я {} на {}""".format(self.width,self.len))
a_square = Square(20,20)
print(a_square.area())
#a_square.print_size()

#композиция
class Dog():
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner
class Person():
    def __init__(self,name):
        self.name = name
oleg = Person('Олег Шпортюк')
panda = Dog('Панда','Дворняжка',oleg)
print(panda.owner.name)
