def reverse_string(word):
    if len(word) <= 1:
        return word
    else :
        return reverse_string(word[1:])+ word[0]
s = 'hello'		
print(reverse_string(s))
