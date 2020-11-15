def count_consonants(word,number = 0):
    yuanyin = ['a','e','i','o','u','A','E','I','O','U',' ',',','.']
    if len(word) <= 1 :
        if word not in yuanyin:
            number += 1
        return number
    else :
        if word[0] not in yuanyin:
            number += 1

        return count_consonants(word[1:],number)
print(count_consonants('Well Done.'))

