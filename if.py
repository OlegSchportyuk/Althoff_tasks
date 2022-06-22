def if10(a):
        if a <= 10:
            print('Число меньше или равно десяти.')
        elif a > 10 and a <= 25:
            print('Число больше 10, но меньше или равно 25.')
        else:
            print('Число больше 25.')
try:
    while True:
        a = int(input('Введите целое число: '))
        if10(a)    
except KeyboardInterrupt:
    print('Выход из программы.')
    
