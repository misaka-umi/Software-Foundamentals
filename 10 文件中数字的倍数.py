integer = int (input ("Enter an integer: "))
file_name =input ("Enter a filename: ")
f = open (file_name , "r")
neirong = f.readlines()
num=[]
for i in neirong:
    number=i.split()
    for a in number:
        num.append(int(a))
j=0
for i in num :
    if i%number1 ==0:
        j=j+1
if j < 2:
    print ("There is {} multiple of {} in the \'{}\' file.".format(j,number1,file_name))
else :
    print ("There are {} multiples of {} in the \'{}\' file.".format(j,number1,file_name))
f.close()
