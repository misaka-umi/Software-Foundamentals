def check(number):
    try :
        if number % 2 == 0 :
            return int(number)
        else :
            return int(0)
    except TypeError :
        return int(0)

def get_sum_even(numbers):
    length = len(numbers)
    num = 0
    i = 0
    for i in range(0,length):
        num = num + check(numbers[i])
        
    return num

