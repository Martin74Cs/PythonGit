import os

class A:
    def __init__(self): 
        self.__jedna = None

    # getter method 
    @property
    def jedna(self): 
        return self.__jedna
    
    # setter method 
    @jedna.setter 
    def jedna(self, x): 
        self.__jedna = x 

class Trida:
    def __init__(self): 
        self._age = None
        self.__name = None
        self.__qwe = A()

    # getter method 
    @property
    def qwe(self): 
        return self.__qwe
    
    # setter method 
    @qwe.setter 
    def age(self, x): 
        self.__qwe = x 

    # getter method 
    @property
    def age(self): 
        return self._age
    
    # setter method 
    @age.setter 
    def age(self, x): 
        self._age = x 

    # getter method 
    @property
    def name(self): 
        return self.__name
    
    # setter method 
    @name.setter 
    def name(self, x): 
        self.__name = x 

    @name.deleter
    def name(self):
        print("deleter of name called" , self.__name)
        del self.__name

    # getter method 
    @property
    def nameAge(self): 
        # print(type(self.__name))
        # POZOR HODNOTA NONE NELZE VYPSAT
        return str(self.__name) + " " + str(self._age)
        #return self._age

os.system("cls")

Test = Trida()
# Test.age = 10
print(Test._age)        # zapozdření nefunguje
print(Test.age)
# print(Test.__name)    Jedná se zapoudření
# print(Test._name)     Nefunguje
# print(Test.name)

Test.jatro = "je to celé na játro"
print(Test.jatro)

# asd =  A
A.jedna = 123
Test.gwe = "asdf"
print(Test.qwe.jedna)

Test = Trida()
Test.age = 10
Test.name = "Pokus"
print("Test.nameAge {:>20s}" .format(Test.nameAge))
# https://www.w3schools.com/python/ref_string_format.asp
# 20 znaků je na konci
print("Test.nameAge {:>20s}".format(Test.nameAge))
print("Test._age {:>20d}".format(Test._age) )      # zapozdření nefunguje
print(Test.age)
# print(Test.__name)    Nefunguje Jedná se zapoudření
# print(Test._name)     Nefunguje
print(Test.name)
del Test.name         # deleter called
#print(Test.name)     # nejde vypsat
