def count_consonants(word):
    a = 0
    b = list(word)
    consonant = ['A','a','E','e','I','i','O','o','U','u']
    for i in b:
        if i in consonant:
            continue
        else:
            a = a+1
    return a
print(count_consonants('Abracadabra'))
