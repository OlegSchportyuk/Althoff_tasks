while True:
        age = int(input('Введите свой возраст: '))
        if age < 18:
            print('Малолет')
        elif age >= 18 and age < 60:
            print('Да ты уже взрослый')
        else:
            print('Привет, пенсионер!')
            
