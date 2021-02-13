number = int(input("Введите число: "))
ml = [7, 4, 3, 2]
c = ml.count(number)
for el in ml:
    if c > 0:
        i = ml.index(number)
        ml.insert(i+c, number)
        break
    else:
        if number > el:
            j = ml.index(el)
            ml.insert(j, number)
            break
        elif number < ml[len(ml) - 1]:
            ml.append(number)
print(ml)