a = input('Введите последовательность чисел/букв: ')
b = list(a)
c = 0
for el in range(int(len(b) / 2)):
    b[c], b[c + 1] = b[c + 1], b[c]
    c += 2

print(b)

