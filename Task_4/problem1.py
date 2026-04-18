def safe_devide(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print("You can't devide by zero")
    except TypeError:
        print("please enter two numbers")
print(safe_devide(6,2))