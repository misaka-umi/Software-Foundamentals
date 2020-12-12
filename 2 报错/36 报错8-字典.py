def get_maori_word(dictionary, word):
    try :
        maori_word = dictionary[word]
        return maori_word
    except KeyError :
        return "ERROR: {} is not available.".format(word)




dictionary ={'example': 'tauira', 'house': 'whare', 'apple': 'aporo', 'love': 'aroha', 'food': 'kai',
'hello': 'kiaora', 'work': 'mana', 'weather': 'huarere', 'greenstone': 'pounamu',
'red': 'whero', 'orange': 'karaka', 'black': 'mangu'}
