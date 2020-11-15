a=input("Enter a sentence: ")
sentence = a.split()
zidian={}
keys=[]
for i in sentence:
    if len(i) not in zidian:
        zidian[len(i)] = i.lower()
    elif i.lower() in zidian[len(i)]:
        pass
    else:
        zidian[len(i)]=zidian[len(i)]+" "+i.lower()
for i in zidian:
    keys.append(i)
keys.sort()
for i in zidian:
    words=zidian[i].split()
    words.sort()
    zidian[i]=" ".join(words)
for i in keys:
    print("{} {}".format(i,zidian[i]))
