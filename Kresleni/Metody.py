import math
import random

def NahodneCislo():
    random.seed()
    # cislo 0 až 1
    random.random()
    # cislo mezt 20 až 100
    random.uniform(20,100)
    return random.random()

class Element():
    Jmeno = "Ondra"
    Id = 1.2
    # def __init__(self):
    #     pass

class Elektro(Element):
    
    def Tisk():
        print(Element.Jmeno)
        Element.Jmeno = "Alena"
        print(Element.Jmeno)
        pass

# print(Element.Jmeno)
Pokus = Elektro
Pokus.Tisk()