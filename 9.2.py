answer = int(input('Сколько тебе лет?\n '))
if answer < 1:
    print('Маловато будет')
if answer > 100:
    print('Ого!')
else:
    f = open('answer.txt','w')
    f.write(str(answer))
    f.close()
    print('Ответ записан.')
    
    
    
