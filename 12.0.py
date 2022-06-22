class Orange:
    def __init__(self,w,c):
        self.weight = w
        self.color = c
        print('Создано!')
or1 = Orange(4, 'светлый апельсин')
or2 = Orange(8, 'темный арельсин')
or3 = Orange(14, 'темный арельсин')
or3.weight = 24
or3.color = 'желтый апельсин'
print(or1.weight, or1.color, '\n', or3.weight, or3.color)

