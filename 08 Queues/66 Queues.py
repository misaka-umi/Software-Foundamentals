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
	

