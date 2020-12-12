
def get_max_list(numbers,max_=-1000000):

    if len(numbers) > 0 :
        if numbers[0] > max_ :
            max_ = numbers[0]
        numbers.pop(0)
        return get_max_list(numbers,max_)
    return max_

lst = [1, 4, 5, -9]
print(get_max_list(lst))

