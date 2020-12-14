def print_all_phrases(tags_dictionary) :
    list1 = tags_dictionary['DT']
    list2 = tags_dictionary['JJ']
    list3 = tags_dictionary['NN']
    for i in list1:
        for j in list2:
            for k in list3:
                print(i,j,k)
    return 0

tags = {'DT': ['a','one'], 'NN': ['father', 'mother', 'room', 'shoemaker', 'washerwoman'], 'JJ': ['poor','rich']}
print_all_phrases(tags)
