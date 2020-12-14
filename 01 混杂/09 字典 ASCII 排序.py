word=input("Enter a word: ")
abc=dict.fromkeys(word)
for i in abc:
    abc[i]= ord(i)
a=sorted(abc.keys())
for i in  a:
    print("{}:{}".format(i,abc[i]))
