def get_phone(phones_dictionary, name):
    try :
        if name == "":
            raise ValueError()
        if type(name) != str :
            raise TypeError()
        number = phones_dictionary[name]
        return number
    except KeyError :
        return "ERROR: {} is not available.".format(name)
    except ValueError:
        return "ERROR: Invalid name!"
    except TypeError:
        return "ERROR: Invalid input!"
    




phones_dictionary = {'Martin':8202, 'Angela':6620, 'Ann':4947, 'Damir':2391, 'Adriana':7113, 'Andrew':5654}
