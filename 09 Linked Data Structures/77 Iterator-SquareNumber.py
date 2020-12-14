class SquareNumber:
    def __init__(self, number):
        self.__count = number
    def __iter__(self):
        return SquareNumberIterator(self.__count)
class SquareNumberIterator:
    def __init__(self,count):
        self.__count = count
        self.__current = 1
    def __next__(self):
        print(self.__current)
        if self.__current <= self.__count:
            x = self.__current
            self.__current += 1
            return x*x
        else:
            raise StopIteration


for number in SquareNumber(5):
    print(number)
