import math
class QuadraticEquation:
    def __init__(self, coeff_a = 1, coeff_b = 1, coeff_c = 1):
        self.__a=coeff_a
        self.__b=coeff_b
        self.__c=coeff_c
    def get_coeff_a(self):
        return self.__a  
    def get_coeff_b(self):
        return self.__b
    def get_coeff_c(self):
        return self.__c
    def get_discriminant(self):
        d = self.__b * self.__b - 4*self.__a*self.__c
        return d
    def has_solution(self):
        if self.get_discriminant()<0:
            return "False"
        else:
            return "True"
    def get_root1(self):
        i=self.get_discriminant()
        return (math.sqrt(i)-self.__b)/(2*self.__a)
    def get_root2(self):
        i=self.get_discriminant()
        return (-math.sqrt(i)-self.__b)/(2*self.__a)
    def __str__(self):
        i = self.get_discriminant()
        if i < 0:
            return "The equation has no roots."
        if i==0:
            return "The root is {:.2f}.".format(self.get_root1())
        if i > 0:
            return "The roots are {:.2f} and {:.2f}.".format(self.get_root1(),self.get_root2())

equation1 = QuadraticEquation(4, 4, 1)
print(equation1)
equation2 = QuadraticEquation()
print(equation2)
equation3 = QuadraticEquation(1, 2, -63)
print(equation3)
