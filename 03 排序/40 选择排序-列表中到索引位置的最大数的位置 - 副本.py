def get_position_of_highest(data, index):
    number = 0
    max = data[0]
    for i in range(1, index+1):
        if max < data[i] :
            number = i
            max = data[i]
    return number
letters = ['y', 'd', 'h', 'w', 't', 'e', 'q', 'a']
print(get_position_of_highest(letters, 3))
