def get_sorted_unique_words_list(sentence):
    words = sentence.split()
    length = len(words)
    new_words = []
    for i in range(0,length):
        words[i] = words[i].lower()
    words.sort()
    for i in range(0,length):
        if words[i] not in new_words :
            new_words.append(words[i])
    return new_words

