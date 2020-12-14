class Stack:
    def __init__(self):
        self.__items = []
    def pop(self):
        if len(self.__items) > 0 :
            a= self.__items.pop()
            return a
        else:
            raise IndexError ("ERROR: The stack is empty!")
    def peek(self):
        if len(self.__items) > 0 :
            return self.__items[len(self.__items)-1]
        else:
            raise IndexError("ERROR: The stack is empty!")
    def __str__(self):
        return "Stack: {}".format(self.__items)
    def __len__(self):
        return len(self.__items)
    def clear(self):
        self.__items = []
    def push(self,item):
        self.__items.append(item)
    def push_list(self,a_list):
        self.__items = self.__items + a_list
    def multi_pop(self, number):
        if number > len(self.__items):
            return "False"
        else:
            for i in range(0,number):
                self.__items.pop()
            return "True"
    def copy(self):
        a=Stack()
        for i in self.__items:
            a.push(i)
        return a
    def __eq__(self,other):
        if not isinstance(other,Stack):
            return "False"
        else:
            if len(other) != len(self):
                return "False"
            else:
                a = other.copy()
                b = self.copy()  #self调用的就是栈本身
                for i in range(len(a)):
                    if a.pop() != b.pop():
                        return "False"
                return "True"

def reverse_sentence(sentence):
    a = Stack()
    b  = sentence.split(" ")
    c = ''
    for i in range(len(b)):
        a.push(b[i])
    for i in range(len(b)):
        if c == '':
            c= a.peek()
        else:
            c = c+" "  + a.peek()
        a.pop()
    return c
print(reverse_sentence('Python programming is fun '))


