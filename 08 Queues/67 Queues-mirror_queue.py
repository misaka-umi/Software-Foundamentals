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
def mirror_queue(a_queue):
    a_list = []
    if len(a_queue) == 0:
        return 0
    else:
        for i in range(len(a_queue)):
            a_list.append(a_queue.peek())
            a_queue.dequeue()
        num =len(a_list)
        for i in range(num):
            a_list.append(a_list[num-i-1])
        a_queue.enqueue_list(a_list)

q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
print(q1)
mirror_queue(q1)
print(q1)
