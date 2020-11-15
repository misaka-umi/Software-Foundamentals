def set_list_element(a_list, index, value):
    try :
        a_list[index] = value
    except TypeError :
        return print('ERROR: Invalid input.')
    except IndexError :
        return print('ERROR: Invalid index: {}.'.format(index))
