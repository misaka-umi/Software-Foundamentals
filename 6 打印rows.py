a = int(input("Enter number of rows: "))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end = ' ')
    if i != a:
        print("")
