my_parametrs = {'Рост':'193','Вес':'74','Любимый цвет':'синий'}
рост = input('Введите ваш рост: ')
if рост == my_parametrs['Рост']:
    print('Верно')
else:
    print('В прошлый раз ваш рост был %sсм.'%my_parametrs['Рост'])
вес = input('Введите ваш вес: ')
if вес == my_parametrs['Вес']:
    print('Верно')
else:
    print('В прошлый раз ваш вес был %sкг.'%my_parametrs['Вес'])
цвет = input('Введите ваш любимый цвет: ').lower()
if цвет == my_parametrs['Любимый цвет']:
    print('Верно')
else:
    print('В прошлый раз ваш любимый цвет был %s'%my_parametrs['Любимый цвет'])
