import sys

class MojeTrida: 
    """
    Ahoj
    """
    # Instance této třídy mohou mít pouze tyto dva atributy
    __slots__ = ["__parametr", "__qwe"]

    # __parametr = 100  # Třídní parametr

    def __init__(self, par : int , qwe):
        """
        Toto je konstroktor
        """
        MojeTrida.__parametr = par  # Instanční parametr
        self.__qwe = qwe

    @property
    def parametr(xxx):
        return xxx.__parametr   # Instanční parametr
    
    @property
    def paraInstance(self):
        return self.__qwe   # Instanční parametr
    
    @paraInstance.setter
    def paraInstance(cls, xa):
        cls.__qwe = xa   # Instanční parametr  

# Vytvoření dvou instancí
objekt1 = MojeTrida(4545.12,"A")
objekt2 = MojeTrida(20,"B")
objekt2 = MojeTrida("www","B")
# objekt3 = MojeTrida("asdfasfd","B")

# print(objekt1.parametrTrida)  # Výstup: 100
print(objekt1.parametr, objekt1.paraInstance)  # Výstup: 100
# print(objekt2.parametrTrida)  # Výstup: 100
print(objekt2.parametr, objekt2.paraInstance)  # Výstup: 100

# Změna třídního parametru
# MojeTrida.parametrTrida = 200
objekt1.paraInstance = "qqq"

print(objekt1.parametr, objekt1.paraInstance)  # Výstup: 200
# print(objekt1.parametrTrida)  # Výstup: 100
print(objekt1.parametr, objekt1.paraInstance)  # Výstup: 200
# print(objekt2.parametrTrida)  # Výstup: 100
print(objekt2.parametr, objekt2.paraInstance)  # Výstup: 200


# help(MojeTrida)

# sys.exc_info()