def f(a=1,b=1):
    c = a/b
    print('Частное = '+str(c))
try:
    while True:
        a = int(input('Введите числитель: '))
        b = int(input('Введите знаменатель: '))
        f(a,b)
except(ZeroDivisionError, ValueError):
        print('Ошибка ввода.')
        
                
        
        
