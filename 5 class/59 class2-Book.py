class Book:
    def __init__(self, code, title, status=True):
        self.__code = code
        self.__title = title
        self.__status = status
    def __str__(self):
        return "{}(id = {}), ${}".format(self.__product_name,self.__product_id,self.__product_price)
    def get_book_title(self):
        return self.__title
    def get_book_code(self):
        return self.__code
    def is_available(self):
        return self.__status
    def borrow_book(self):
        self.__status = False
    def return_book(self):
        self.__status = True
    def __str__(self):
        if self.is_available():
            i = "Available"
        else:
            i = "On Loan"
        return "{} , {} ({})".format(self.__title,self.__code,i)

b1 = Book("QS12.03.001", "The Lord Of The Rings")
print(b1)
b2 = Book("QK12.04.002", "The Hitchhiker's Guide To The Galaxy")
print(b2)
b2.borrow_book()
print()
print(b2)
