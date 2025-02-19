# from abc import ABC, abstractmethod

# class IEntity:
#     """Rozhraní pro všechny entity."""
#     @abstractmethod
#     def get(self, id):
#         pass

#     @abstractmethod
#     def set(self, id, value):
#         pass

class Entity:

    def __init__(self, id=None, name=None):
        self.Id  = id
        self.Name = name
        # super().__init__(self,id=None)  # Initialize Entity attributes

    # @property
    # def Id(self):
    #     return self.Id

    # @Id.setter
    # def Id(self, x):
    #     self.Id = x

    # @property
    # def Name(self):
    #     return self.Name

    # @Name.setter
    # def Name(self, x):
    #     self.Name = x


class Elektro(Entity):

    def __init__(self, id=None, name=None, hmotnost=None):
        super().__init__(id, name)  # Initialize Entity attributes
        self.Hmotnost = hmotnost

    # @property
    # def Hmotnost(self):
    #     return self.Hmotnost

    # @Hmotnost.setter
    # def Hmotnost(self, x):
    #     self.Hmotnost = x

    def __str__(self):
        # return f"Elektro(ID={self.get('Id')}, Name={self.get('Name')}, Hmotnost={self.get('Hmotnost')})"
        return f"Elektro(ID={self.Id}, Name={self.Name}, Hmotnost={self.Hmotnost})"
class Stroj(Entity):

    def __init__(self, id=None, name=None, velikost=None):
        super().__init__(id, name)  # Initialize Entity attributes
        self.Velikost = velikost

    # @property
    # def Velikost(self):
    #     return self.Velikost

    # @Velikost.setter
    # def Velikost(self, x):
    #     self.Velikost = x

    def __str__(self):
        # return f"Elektro(ID={self.get('Id')}, Name={self.get('Name')}, Hmotnost={self.get('Hmotnost')})"
        return f"Stroj(ID={self.Id}, Name={self.Name}, Velikost={self.Velikost})"

def Select(entity: enumerate[Entity], find: int) -> Entity | None:
    pole = []
    for znak in entity:
        if(znak.Id == find):
            pole.append(znak)
            return znak
    # return pole

def SelectPodmínka(entity: enumerate[Entity], Podmínka) -> enumerate[Entity] | None:
    pole = []
    for znak in entity:
        if(Podmínka(znak)):
            pole.append(znak)
    return pole

Pole = []
Test = Elektro()
Test.Id = 10
Test.Name = "dafsd"
Test.Hmotnost = 1234
Pole.append(Test)

Pole.append(Elektro(1,"Jedna",100))
Pole.append(Elektro(2,"Dva",200))
Pole.append(Elektro(3,"Tři",300))
Vyber = Select(Pole, 3)
print(Vyber.Hmotnost)
Vyber = SelectPodmínka(Pole, lambda e: e.Id > 2)
print("Počet :", len(Vyber))
for znak in Vyber:
    print(znak)

Pole = []
Test = Stroj()
Test.Id = 10
Test.Name = "dafsd"
Test.Velikost = 1234
Pole.append(Stroj(1,"Jedna",100))
Pole.append(Stroj(2,"Dva",200))
Vyber = Select(Pole, 2)
Vyber = SelectPodmínka(Pole, lambda e: e.Id > 2)
print("Počet :", len(Vyber))
for znak in Vyber:
    print(znak)

Pole = []
Pole.append(Stroj(1,"Jedna",100))
Pole.append(Stroj(2,"Dva",200))
Pole.append(Elektro(1,"Jedna",100))
Pole.append(Elektro(2,"Dva",200))
Pole.append(Elektro(3,"Tři",300))
Pole.append(Stroj(3,"Dva",200))
Pole.append(Stroj(4,"Dva",200))
Vyber = Select(Pole, 2)
Vyber = SelectPodmínka(Pole, lambda e: e.Id > 2)
print("Počet :", len(Vyber))
for znak in Vyber:
    print(znak)



