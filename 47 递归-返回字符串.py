def copy_string(word,s = ''):
    if s == '':
        s = word
        return copy_string(word,s)
    else :
        return s
s = 'hello'		
print(copy_string(s))
