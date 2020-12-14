class CircularQueue:
    def __init__(self,number=8):
        self.__items = [None]* number
        self.__front = 0
        self.__back = number -1
        self.__count = 0
        self.__number = number
    def is_empty(self):
        if self.__count == 0 :
            return True
        else:
            return False
    def __str__(self):
        return "{}, front:{}, back:{}, count:{}".format(self.__items,self.__front,self.__back,self.__count)
    def is_full(self):
        return self.__count == self.__number
    def enqueue(self,item):
        if self.is_full():
            raise IndexError("ERROR: The queue is full.")
        else:
            self.__back = (self.__back +1 )% self.__number
            self.__items[self.__back] = item
            self.__count += 1
    def dequeue(self):
        if len(self.__items) == 0:
            raise IndexError("ERROR: The queue is empty!")
        else:
            self.__front = (self.__front + 1) % self.__number
            self.__count -=1
            item = self.__items[self.__front-1]
            return item
    def print_all(self):
        if self.__front == self.__back:
            return print(self.__items[self.__front])
        num = self.__back - self.__front
        for i in range(num):
            print(self.__items[self.__front + i],end = ' ')
        print(self.__items[self.__front + num])
q1 = CircularQueue(5)
q1.enqueue(1)
q1.dequeue()
q1.enqueue(2)
print(q1)
q1.print_all()
