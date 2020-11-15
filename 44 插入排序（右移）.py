def insertion_row(data, index):
    item_to_check = data[index]
    i = index - 1
    while i >= 0 and data[i] > item_to_check:
        data[i+1] = data[i]
        data[i] = item_to_check
        i -= 1
    return data
letters = ['h', 't', 'w', 'e', 'q', 'c', 'x']
insertion_row(letters, 3)
print(letters)
