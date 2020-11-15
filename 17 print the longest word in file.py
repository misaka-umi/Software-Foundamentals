filename = input("Enter a filename: ")
f = open(filename,'r')
pockage = f.readlines()
num = []
for i in pockage :
    a = i.split()
    for j in a :
        num.append(j)
len = len(num)
max = 0
maxname = 0
for i in len :
    if max < len(num[i]) :
        max = len(num[i])
        maxname = num[i]
print("The longest word is",)
