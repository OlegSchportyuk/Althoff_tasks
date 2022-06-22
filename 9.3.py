films = [['Звездные войны','Терминатор','Искуственный интеллект'],
         ['Дурак','Матильда','Левиафан'],
         ['Люди вчерном','Я - робот','Эволюция']]

import csv

with open('films.csv','w') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow(films[0])
    w.writerow(films[1])
    w.writerow(films[2])
f.close()
print('End')

