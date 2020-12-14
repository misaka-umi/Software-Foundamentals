def get_sum_positive_even(numbers):
    a = 0
    for i in numbers:

        if i > 0 and i%2 == 0 :
            a = a + i
    return a
numbers = [1,2,34,2134,3241]
print(get_sum_positive_even(numbers))
