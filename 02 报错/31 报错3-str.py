def count_consonants(word):
    try :
        n = 0
        list1 = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
        if type(word) != str :
            raise TypeError ()
        for i in word :
            if i in list1 :
                n += 1
        return n
    except TypeError:
        return "ERROR: Invalid input!"

