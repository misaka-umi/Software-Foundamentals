def get_word_tag_tuple(tags_dictionary, search_word):
    keys = tags_dictionary.keys()
    keys = list(keys)
    for i in keys:
        if search_word in tags_dictionary[i] :
            tup = (search_word,i)
            break
    return tup
dict = {'NN': ['dreamer', 'father', 'fun', 'grass', 'mother', 'odense', 'rain', 'shoemaker', 'spring', 'summer', 'tortoise', 'toy', 'washerwoman'],'IN':['abc']}
print(get_word_tag_tuple(dict, 'abc'))
