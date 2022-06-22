def square(x):
    '''Возвращает квадрат введенной целочисленной цифры.'''
    x = x*x
    return x
while True:
    x = int(input('Введите целое число, которое хотите возвести в квадрат: '))
    y = square(x)
    print(y)
    
