while True:
    a=input('Enter number a:')
    b=input('Enter number b:')
    try:
        result= int(a)/int(b)
    except ZeroDivisionError:
        print("Zerro division")
    except ValueError:
        print("Not a digit")
    else:
        print('Square Resutl:',result**2)
        break
