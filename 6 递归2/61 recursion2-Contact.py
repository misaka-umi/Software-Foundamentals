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
c1 = Contact("John", "7589943", "john@amail.com")
print(c1)
c2 = Contact("Kelly", "4344345", "kelly@bmail.com")
print(c2)
print()
c1.set_phone_number("1234567")
c1.set_email("abc@abc.com")
c2.set_active(False)
print(c1)
print(c2)
