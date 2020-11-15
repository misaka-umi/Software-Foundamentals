def get_tags_frequency(list_of_tuples) :
    dictionary = {}
    length = len(list_of_tuples)
    for i in range(0,length):
        if list_of_tuples[i][1] not in dictionary :
            dictionary[list_of_tuples[i][1]] = 1
        else :
            num = dictionary[list_of_tuples[i][1]]
            num += 1
            dictionary[list_of_tuples[i][1]] = num
    return dictionary

list_of_tuples = [('a', 'DT'), ('and', 'CC'), ('father', 'NN'), ('his', 'PRP$'), ('mother', 'NN'), ('shoemaker', 'NN'), ('was', 'VBD'), ('washerwoman', 'NN')]
freq_dict = get_tags_frequency(list_of_tuples)
for key in sorted(freq_dict.keys()):
    print(key, freq_dict[key])
