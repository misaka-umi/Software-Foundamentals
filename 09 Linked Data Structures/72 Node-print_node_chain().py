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
    a = node_of_chain
    while a != None:
        print(a.get_data())
        a = a.get_next()
node1 = Node('hello')
node2 = Node('world')
node3 = Node('goodbye')
node1.set_next(node2)
node2.set_next(node3)
print_node_chain(node1)
