def a(*args):

    try:
        arg1 = int(input("Input Arg1 "))
        arg2 = int(input("Input Arg2 "))
        a = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong Arg2! "

    return a


print(f'Result  {a()}')