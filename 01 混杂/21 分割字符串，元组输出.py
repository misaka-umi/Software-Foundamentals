def get_tag_words(line):
    line = line.split(':')
    tup1 = (line[0],)
    line2 = line[1].split()
    line2.sort()
    tup2 = (line2,)
    tup  = tup1 + tup2
    return tup
