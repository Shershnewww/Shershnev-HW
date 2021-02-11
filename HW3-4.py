def func(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res


print(func(float(input("Первое значение - ")), int(input("Второе значение - "))))
