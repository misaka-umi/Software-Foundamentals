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
def print_node_chain(node_of_chain):
    while node_of_chain != None:
        print(node_of_chain.get_data())
        node_of_chain=node_of_chain.get_next()
    return None
def create_node_chain(values): #假设列表(values)非空
    num = len(values)
    tmp = Node(values[num-1])
    if len(values) == 1:
        return tmp
    else:
        for i in range(1,num):
            c = Node(values[num-i-1])
            c.set_next(tmp)
            tmp =c
        return tmp
values = create_node_chain(['apple', 'banana', 'cherry', 'date', 'elderberry'])
print_node_chain(values)
    
