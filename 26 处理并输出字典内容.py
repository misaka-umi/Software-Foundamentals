def print_dictionary(tags_dictionary) :
    list1 = tags_dictionary.keys()
    list1 = list(list1)
    list1.sort()
    for i in list1 :
        print(i,tags_dictionary[i])
    return 0

tags_dictionary = {'DT': 1, 'CC': 1, 'NN': 4, 'PRP$': 1, 'VBD': 1}
print_dictionary(tags_dictionary)
