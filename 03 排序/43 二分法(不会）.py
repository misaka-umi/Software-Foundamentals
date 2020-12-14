'''
def binary_search(numbers, value):
    max_index = len(numbers) - 1
    min_index = 0
    while (min_index <= max_index):
        mid_index = int((min_index + max_index)/2)
        if numbers[mid_index] == value :
            return mid_index
        if numbers[mid_index] < target :
            mid_index = mid_index + 1
        else :
            max_index = mid_index - 1
'''
#如下为普通方法，非二分法
def binary_search(numbers, value):
    max_index = len(numbers) - 1
    min_index = 0
    correct = -1
    length = len(numbers)
    for i in range(0, length):
        if value == numbers[i]:
            correct = i
    return correct

numbers = [6, 30, 33, 51, 63, 66, 74, 77, 86]
print(binary_search(numbers, 6))
