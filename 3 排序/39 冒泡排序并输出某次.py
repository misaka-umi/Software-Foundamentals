def bubble_row(data, index):
    length = len(data)
    times = 0
    for i in range(0,length-1):
        for j in range(0, length-1):
            if data[j] > data [j+1] :
                change_letter = data[j+1]
                data[j+1] = data[j]
                data[j] = change_letter
            times += 1
            if times == index :
                break
        if times == index :
            break
    return data

	
letters = ['m', 'v', 'o', 'd', 'h', 'l', 'y', 's', 'x', 'z']
bubble_row(letters, 4)
print(letters)
