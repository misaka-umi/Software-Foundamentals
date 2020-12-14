def selection_row(data, index):
    number = index
    max = data[index]
    for i in range(0, index+1):
        if max < data[i] :
            max = data[i]
            number = i
    data[number] = data[index]
    data[index] = max
    return data


letters = ['a', 'd', 'h', 'w', 't', 'p']
selection_row(letters, 3)
print(letters)
