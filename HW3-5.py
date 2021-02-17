def sum ():
    sum1 = 0
    ex = False
    while ex == False:
        number = input('Введите число или X для выхода - ').split()

        a = 0
        for el in range(len(number)):
            if number[el] == 'x' or number[el] == 'X':
                ex = True
                break
            else:
                a = a + int(number[el])
        sum1 = sum1 + a
        print(f'Текущая сумма {sum1}')
    print(f'Финальное значение {sum1}')


sum()