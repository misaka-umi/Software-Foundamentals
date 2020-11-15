def no_evens(words):
    if len(words) > 0:
        if words[0] %2 == 0:
            return 'False'
        words.pop(0)
        return no_evens(words)
    return 'True'

print(no_evens([3, 5, 6]))
