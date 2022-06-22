def f1(a,b=2):
    '''Возвращает деление введенной цифры на 2'''
    return a/b
def f2(x,y=4):
    '''Возвращает умножение на 4'''
    return x*y
while True:
    a = int(input('Введите целое число: '))
    x = f1(a)
    print(f2(x))
    
    
