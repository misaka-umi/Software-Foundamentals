def create_tags_dictionary(filename):
    tags = {}
    l=[]
    f = open(filename,'r')
    line = f.read().splitlines()
    f.close()
    length = len(line)
    for i in range(0,length):
        l = line[i].split(':')
        line2 = l[1].split()
        line2.sort()
        key = l[0]
        tags[key] = line2
    return tags
tags = create_tags_dictionary('0.txt')
for key in sorted(tags):
    print(key, tags[key])
