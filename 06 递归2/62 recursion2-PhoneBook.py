class Contact:
    def __init__(self,name,phone_number,email,status=True):
        self.__name = name
        self.__phone_number = phone_number
        self.__email = email
        self.__status = status
    def get_name(self):
        return self.__name
    def get_phone_number(self):
        return self.__phone_number
    def get_email(self):
        return self.__email
    def is_active(self):
        return self.__status
    def set_phone_number(self,phone_number):
        self.__phone_number = phone_number
        return self.__phone_number
    def set_email(self,email):
        self.__email = email
        return self.__email
    def set_active(self,value):
        self.__status = value
        return self.__status
    def __str__(self):
        if self.__status:
            return "{} ({}), {}".format(self.__name,self.__phone_number,self.__email)
        else:
            return "{} is an inactive record.".format(self.__name)

class PhoneBook:
    def __init__(self):
        self.__phone_book = []
    def load_records(self,filename):
        try:
            f = open(filename,"r")
            lines = f.read().splitlines()
            number = len(lines)
            if number == 0:
                print("{} record loaded.".format(number))
            if number > 0:
                print("{} records loaded.".format(number))
            for i in range(0,number):
                line = lines[i].split(",")
                a = Contact(line[0],line[1],line[2])
                self.__phone_book.append(a)
            f.close()
        except FileNotFoundError:
            return print("ERROR: The file '{}' does not exist.".format(filename))
    def show_all_records(self):
        for i in self.__phone_book:
            print(i)
    def __len__(self):
        return len(self.__phone_book)
    def find_record(self, search_name):
        right = 0
        for i in self.__phone_book:
            if i.get_name() == search_name:
                right = 1
                return i

    def update_phone(self, search_name, phone_number):
        right = 0
        for i in self.__phone_book:
            if i.get_name() == search_name:
                i.set_phone_number(phone_number)
                right = 1
                return print("{}'s contact is updated".format(search_name))
                break
        if right == 0:
            return print("ERROR: {} is not found.".format(search_name))
    def set_active(self, search_name):
        a = self.find_record(search_name)
        if a == None:
            print("ERROR: {} is not found.".format(search_name))
        else:
            a.set_active(True)
            print("{} is active from now on.".format(search_name))
    def set_inactive(self,search_name):
        a=self.find_record(search_name)
        if a==None:
            print("ERROR: {} is not found.".format(search_name))
        else:
            a.set_active(False)
            print("{} is inactive from now on.".format(search_name))
    def show_active_records(self):
        for i in self.__phone_book:
            if i.is_active:
                print(i)
            

              
my_phonebook = PhoneBook()
my_phonebook.load_records("1.txt")
my_phonebook.set_inactive("June")
print()
my_phonebook.show_all_records()
print()
my_phonebook.set_inactive("Kelly")
my_phonebook.show_all_records()
print()
my_phonebook.set_active("Kelly")
my_phonebook.show_all_records()
print()

