def func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg1 + arg3


print(f'Result - {func(int(input("enter arg1 ")), int(input("enter arg2 ")), int(input("enter arg3 ")))}')
