def get_max(numbers):
    try :
        length = len(numbers)
        max = -1000000000
        for i in range(0,length):
            if max < numbers[i] :
                max = numbers[i]
        return float(max)
    except TypeError :
        return 'ERROR: Invalid number!'

