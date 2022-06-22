def f(a):
    '''Преобразовывает строку в тип данных float'''
    return float(a)

try:
    while True:
        a = input('Введите число: ')
        print(f(a))
except ValueError:
    print('Ошибка ввода.')
    
