def remove_letters(word1, word2):
    result = list(word2)
    for letter in word1:
        if letter in result:
            result.remove(letter)
    return ''.join(result)
print(remove_letters('hello', 'world'))
