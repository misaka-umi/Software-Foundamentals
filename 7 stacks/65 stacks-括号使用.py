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
            return False
        else:
            for i in range(0,number):
                self.__items.pop()
            return True
    def copy(self):
        a=Stack()
        for i in self.__items:
            a.push(i)
        return a
    def __eq__(self,other):
        if not isinstance(other,Stack):
            return False
        else:
            if len(other) != len(self):
                return False
            else:
                a = other.copy()
                b = self.copy()  #self调用的就是栈本身
                for i in range(len(a)):
                    if a.pop() != b.pop():
                        return False
                return True


def is_balanced_brackets(text):
    a=Stack()
    for i in text:
        if i == '(' or i == '[' or i == '{':
            a.push(i)
        if i == ')':
            if len(a) == 0:
                return False
            else:
                if a.pop() != '(':
                    return False
        if i == ']':
            if len(a) == 0:
                return False
            else:
                if a.pop() != '[':
                    return False
        if i == '}':
            if len(a) == 0:
                return False
            else:
                if a.pop() != '{':
                    return False
    if len(a) == 0:
        return True
    else:
        return False
print(is_balanced_brackets('({x})(())()'))
print(is_balanced_brackets('x(y)z'))
print(is_balanced_brackets('([x)](())()'))
print(is_balanced_brackets('x[y)(]z'))
