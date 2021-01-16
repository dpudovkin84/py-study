try:
    a=input('Enter number a:')
    b=input('Enter number b:')
    print('Result:', int(a)/int(b))
except (ZeroDivisionError,ValueError):
    print("Something went wrong")
