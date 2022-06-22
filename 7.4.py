qs = ['3','2','1','5','7']
n=0
print('Введи X для выхода')
while True:
    a = input('Угадай загаданную цифру: ')
    if a == 'X':
        break
    if a == qs[n]:
        print('Верно')
    else:
        print('Неверно')
    n = (n+1)%5
    
