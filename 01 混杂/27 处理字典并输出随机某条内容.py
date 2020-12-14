import random
def print_random_phrase(tags_dictionary) :
    list1 = tags_dictionary['DT']
    list2 = tags_dictionary['JJ']
    list3 = tags_dictionary['NN']
    list4 = []
    for i in list1:
        for j in list2:
            for k in list3:
                list5 = [i,j,k]
                list4.append(list5)
    length = len(list4)
    m = random.randrange(0,length)
    '''
    len1 = len(list1)
    len2 = len(list2)
    len3 = len(list3)
    i  = random.randrange(0,len1)
    j = random.randrange(0,len2)
    k = random.randrange(0,len3)
    '''
    print(list4[m][0],list4[m][1],list4[m][2])
    return 0

tags = {'JJ': ['brown', 'yellow'], 'NN': ['grass', 'summer'], 'DT': ['the', 'a']}
print_random_phrase(tags)
