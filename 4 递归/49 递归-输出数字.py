def print_between(start, end):
    if start != end :
        print(start,end = ' ')
        return print_between(start+1, end)
    else :
        return print(end)
print_between(1, 5)
