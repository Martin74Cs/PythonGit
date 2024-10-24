import os

class A:
    def __init__(self): 
        self._jedna = None

    # getter method 
    @property
    def jedna(self): 
        return self._jedna
    
    # setter method 
    @jedna.setter 
    def jedna(self, x): 
        self._jedna = x 

class Trida:
    def __init__(self): 
        self.__age = None
        self._name = None
        self._tridaA = A()


    # getter method 
    @property
    def tridaA(self): 
        return self._tridaA
    
    # setter method 
    @tridaA.setter 
    def age(self, x): 
        self._tridaA = x 



    # getter method 
    @property
    def age(self): 
        return self.__age
    
    # setter method 
    @age.setter 
    def age(self, x): 
        self.__age = x 




    # getter method 
    @property
    def name(self): 
        return self._name
    
    # setter method 
    @name.setter 
    def name(self, x): 
        self._name = x 

    @name.deleter
    def name(self):
        print("deleter of name called" , self._name)
        del self._name


    # getter method 
    @property
    def nameAge(self): 
        # print(type(self.__name))
        # POZOR HODNOTA NONE NELZE VYPSAT
        return str(self._name) + " " + str(self.__age)
        #return self._age

os.system("cls")

Test = Trida()
# Test.age = 10
# print(Test.__age)        # zapozdření nefunguje
print(Test.age)
# print(Test.__name)    Jedná se zapoudření
# print(Test._name)     Nefunguje
# print(Test.name)

Test.jatro = "je to celé na játro"
print(Test.jatro)

A.jedna = 123
print(A.jedna)

Test.__age = "Pokus"
print("3-",Test.__age)
print("4-",Test.age)

Test.age = "Další"
print("1-", Test.__age)
print("2-", Test.age)


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
