from itertools import count
from math import factorial


def fact_gen():
    for el in count(1):
        yield factorial(el)


gen = fact_gen()
x = 0
y = int(input("Введите число: "))
for i in gen:
    if x < y - 1:
        x += 1
    else:
        print('Факториал числа =', i)
        break
