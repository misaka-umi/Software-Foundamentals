def count_down(n):
    if n == 0 :
        return print("GO!")
    else :
        print(n)
        return count_down(n-1)
