def get_multiples_of_5(numbers):
    a = []
    for i in numbers :
        if i > 0 and i%5 == 0:
            a.append(i)
    return a
print(get_multiples_of_5([3, 1, 6, 2, 3, 9, 7, 9, 5, 4, 25]))
