def f(obj1,obj2):
    print(obj1 is obj2)

class Person():
    def __init__(self):
        self.name = 'Пандил'
pand = Person()
pand1 = pand
lapk = Person()
f(pand,pand1)
f(pand,lapk)
