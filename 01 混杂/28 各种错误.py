def errors(a,b):
    try :
        file = open("1.txt")
        return a/b
    except FileNotFoundError :
        print("NoFile")
        return 0
    except ZeroDivisionError :
        return 0
print(errors(10,0))
