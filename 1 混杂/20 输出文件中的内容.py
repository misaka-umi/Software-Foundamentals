def read_content(filename):
    f = open(filename,'r')
    pockage = f.read().splitlines()
    f.close()
    return pockage
