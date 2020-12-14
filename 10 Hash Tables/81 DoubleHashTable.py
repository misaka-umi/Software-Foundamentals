class DoubleHashTable:
    def __init__(self, size = 7,second_hash_value = 5):
        self.__size = size
        self.__second_hash_value = second_hash_value
        self.__slots = [None] * self.__size
    def __str__(self):
        return str(self.__slots)
    def put(self, key):
        num = key % self.__size
        count = 0
        for i in range(self.__size):
            if self.__slots[i] != None:
                count += 1
        if count == self.__size:
            raise IndexError("ERROR: The hash table is full.")
        if self.__slots[num] == None:
            self.__slots[num] = key
        else:
            step = 1
            step_size = self.get_new_hash_code_double_probing(key)
            num1= num
            while self.__slots[num1] != None:
                next_index = (num+ step * step_size) %self.__size
                step += 1
                num1 = next_index
            self.__slots[num1] = key
    def get_new_hash_code_double_probing(self, key):
        step_size = self.__second_hash_value - (key % self.__second_hash_value)
        return step_size

my_hash_table=DoubleHashTable()
my_hash_table.put(1)
print(my_hash_table)
my_hash_table.put(8)
print(my_hash_table)
my_hash_table.put(15)
print(my_hash_table)
my_hash_table.put(22)
print(my_hash_table)
my_hash_table.put(41)
print(my_hash_table)
