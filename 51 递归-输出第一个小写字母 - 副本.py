def get_first_lower_case(word):
    if len(word) == 1 :
        if ord(word[0])>97 and ord(word[0])<122 :
            return word[0]
    else :
        if ord(word[0])>97 and ord(word[0])<122 :
            return word[0]
        else :
            return get_first_lower_case(word[1:])

s = 'WELL done'
print(get_first_lower_case(s))
s = 'GREAT'		
print(get_first_lower_case(s))
