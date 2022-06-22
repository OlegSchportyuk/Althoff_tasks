class Apple:
    def __init__(self, weight,color,vid,price):
        self.weight = weight
        self.color = color
        self.vid = vid
        self.price = price
        print('Яблочко!')
apple = Apple(4,'зеленое','семеренко',100)
print(apple.weight,apple.color,apple.vid,apple.price)
