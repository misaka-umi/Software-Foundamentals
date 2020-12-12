def get_max_len_list(words,length= 0):
    if len(words) > 0:
        if len(words[0]) >length:
            length = len(words[0])
        words.pop(0)
        return get_max_len_list(words,length)
    return length
lst = ['This']
print(get_max_len_list(lst))
