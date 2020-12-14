while True:
    i = 0
    list = []
    star = int(input("Enter number of rows: "))
    for i in range(0,star):
        list.append([])
        for j in range(0,star):
            list[i].append(" ")
    for i in range (0,star):
        if i == 0 or i ==star-1:
            for j in range (star):
                list[i][j]="*"
        elif i == (star-1)/2:
            list[i][i]="*"
            list[i][0]="*"
            list[i][star-1]='*'
        else :
            list[i][0]="*"
            list[i][star-1]="*"
            list[i][i]="*"
            list[i][star-i-1]="*"
    for i in range (0,star):
        for j in range(0,star):
            print(list[i][j],end="")
        print("")
    break
