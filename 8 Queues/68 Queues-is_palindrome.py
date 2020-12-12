class Queue:
    def __init__(self):
        self.__items = []
    def enqueue(self,item):
        self.__items.append(item)
    def dequeue(self):
        if len(self.__items) == 0:
            raise IndexError("ERROR: The queue is empty!")
        else:
            return self.__items.pop(0)
    def peek(self):
        if len(self.__items) == 0:
            raise IndexError("ERROR: The queue is empty!")
        else:
            return self.__items[0]
    def __str__(self):
        return "Queue: {}".format(self.__items)
    def __len__(self):
        return len(self.__items)
    def clear(self):
        self.__items = []
    def enqueue_list(self, a_list):
        self.__items = self.__items + a_list
    def multi_dequeue(self, number):
        if len(self) < number :
            return False
        else:
            for i in range(number):
                self.dequeue()
                print(self)
            return True
def is_palindrome(word):
    q = Queue()
    num = len(word)
    for i in range(num):
        q.enqueue(word[i])
    if num%2 == 0 :
        for i in range(int(num/2)):
            if word[num-i-1] == q.peek():
                q.dequeue()
            else:
                return False
    if num %2 != 0 :
        for i in range(num//2):
            if word[num-i-1] == q.peek():
                q.dequeue()
            else:
                return False
    return True
print(is_palindrome("abcdef"))
print(is_palindrome("nonon"))
print(is_palindrome("abccba"))
