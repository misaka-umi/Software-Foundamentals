
def my_selection_sort(data):
    length = len(data)
    for i in range(0,length-1):
        min = data[i]
        number = i
        for j in range(i+1,length):
            if min > data[j] :
                number = j
                min = data[j]
        if i != number:
            tmp = data[number]
            data[number] = data[i]
            data[i] = tmp
           # data[i] = 
    return data
letters = ['e', 'd', 'c', 'b', 'a','f','g','h','k']

my_selection_sort(letters)
print(letters)
'''


def selectionSort(arr):
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr
letters = ['e', 'd', 'c', 'b', 'a','f','g','h','k']
selectionSort(letters)
print(letters)
'''
