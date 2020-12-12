def print_keys_values_inorder(dictionary):
    length=[]
    word=[]
    for i in dictionary:
        length.append(i)
    length.sort()
    for i in length:
        dictionary[i].sort()
        word.append(dictionary[i])
    k=0
    print(word)
    for i in range(0,len(length)):
        print(length[i],end=" ")
        for j in range(k,len(word)):
            b=word[j]
            for h in b:
                print(h,end=" ")
            k=j+1
            break
        print("")
my_dict = {6:['monday', 'coffee', 'strong'], 5:['short'], 3:['may', 'and']}
print_keys_values_inorder(my_dict)
