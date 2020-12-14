class QuadraticHashTable:
    def __init__(self, size = 7):
        self.__size = size
        self.__slots = [None] * self.__size
    def __str__(self):
        return str(self.__slots)
    def get_hash_code(self, key):
        return key % self.__size
    def get_size(self):
        return self.__size
    def put(self, key):
        num = key % self.__size
        count = 0
        for i in range(self.__size):
            if self.__slots[i] != None:
                count += 1
        if count == self.__size:
            raise IndexError("ERROR: The hash table is full.")
        if self.__slots[key % self.__size] == None:
            self.__slots[key % self.__size] = key
        else:
            num = self.get_new_hash_code_quadratic_probing(num)
            self.__slots[num] = key
        
    def __len__(self):
        length = 0
        for i in self.__slots:
            if i != None :
                length += 1
        return length
    def get_new_hash_code_quadratic_probing(self, index):
        x= 1
        index1 = index
        while self.__slots[index1] != None:
            index1 = (x*x +index)%self.__size
            x = x+1
        return index1
    def is_empty(self):
        for i in range(self.__size):
            if self.__slots[i] != None:
                return False
        return True
    def clear(self):
        self.__slots = [None] * self.__size
    def rehashing(self, new_size):
        list1 = []
        for i in range(self.__size):
            if self.__slots[i] != None:
                list1.append(self.__slots[i])
        self.__size = new_size
        self.__slots = [None]*self.__size
        for i in list1:
            self.put(i)
