class Node:
    def __init__(self, data, next_data = None):
        self.__data = data
        self.__next = next_data
    def __str__(self):
        return self.__data
    def get_data(self):
        return self.__data
    def get_next(self):
        return self.__next
    def set_data(self,data):
        self.__data = data
    def set_next(self,next_data):
        self.__next = next_data
    def add_after(self, value):
        tmp = self.__next
        a = Node(str(value))
        self.__next = a
        a.set_next(tmp)
    def remove_after(self):
        tmp = self.get_next().get_next()
        self.__next = tmp
    def __contains__(self, value):
        if self.__next == None and self.__data != value:
            return False
        else:
            if self.__data == value :
                return True
            tmp = self.__next
            while tmp != None:
                if tmp.get_data() == value:
                    return True
                else:
                    tmp = tmp.get_next()
            return False
    def get_sum(self): #此处假设仅有整数值
        num = self.__data
        tmp = self.__next
        while tmp != None:
            num +=tmp.get_data()
            tmp = tmp.get_next()
        return num

class LinkedList():
    def __init__(self):
        self.__head = None
    def add(self, value):
        new_node = Node(value)
        new_node.set_next(self.__head)
        self.__head = new_node
    def size(self):
        tmp = self.__head
        num = 0
        while tmp != None:
            num += 1
            tmp = tmp.get_next()
        return num
    def get_head(self):
        return self.__head
    def clear(self):
        self.__head = None
    def is_empty(self):
        if self.__head == None:
            return True
        else:
            return False
    def __len__(self):
        return self.size()
    def __str__(self):
        tmp = self.__head
        s = '['
        while tmp != None:
            if tmp.get_next() ==None:
                s = s + str(tmp.get_data())
                break
            s = s + str(tmp.get_data()) + ', '
            tmp = tmp.get_next()
        s = s+']'
        return s
    def __contains__(self, search_value):     # 用法 print('hello' in values)
        tmp = self.__head
        while tmp != None:
            if tmp.get_data() == search_value:
                return True
            tmp = tmp.get_next()
        return False
    def __getitem__(self, index): #print(my_list[0])
        tmp = self.__head
        while index != 0:
            tmp = tmp.get_next()
            index -= 1
        return tmp.get_data()
    def add_all(self, a_list):
        num = len(a_list)
        for i in range(num):
            self.add(a_list[i])
    def get_min_odd(self):
        min_ = 999
        if self.__head == None:
            return min_
        tmp = self.__head
        while tmp != None:
            num=tmp.get_data()
            if num %2 != 0 and num < min_:
                min_ = num
            tmp = tmp.get_next()
        return min_

class LinkedListIterator:
    def __init__(self, head):
        self.__current = head
    def __next__(self):
        if self.__current != None:
            x = self.__current.get_data()
            self.__current = self.__current.get_next()
            return x
        else:
            raise StopIteration
	
values = LinkedList()
values.add('cherry')
values.add('banana')
values.add('apple')
for value in values:
    print(value)
