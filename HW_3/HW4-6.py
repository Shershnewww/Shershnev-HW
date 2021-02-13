from itertools import count

for el in count(int(input('Введите стартовое число '))):
    if el > 20:
        break
    print(el)

from itertools import cycle

count = 0
my_list = ['the', 'truth', 'is', 'somewhere', 'near']
for el in cycle(my_list):
    if count > 14:
        break
    print(el)
    count += 1