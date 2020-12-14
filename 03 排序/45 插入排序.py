def insertion_row(data, index):
    item_to_check = data[index]
    i = index - 1
    while i >= 0 and data[i] > item_to_check:
        data[i+1] = data[i]
        data[i] = item_to_check
        i -= 1
    return data


def my_insertion_sort(data):	
    for index in range(1, len(data)):
        insertion_row(data, index)
    return data
letters = ['x', 'b', 'f', 'u', 'r', 'k']
my_insertion_sort(letters)
print(letters)
