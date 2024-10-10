# Objektově orientované programování
print(type(5))
print(type("david"))
print(type(True))
print(type(()))
print(type([]))


# Atributy a metody
class Car:
    # code
    pass

car1 = Car()
car2 = Car()
car3 = Car()

print(type(car1))

# Atributy a metody
class Player:
    # constructor
    def __init__(self, name="anonym", age=10):
        self.name = name
        self.age = age

    # metoda
    def attack(self):
        print("Útok!")


Hrac = Player() 
print("Player")
print(Player)
print("Hrac")
print(Hrac)
print("Jmeno a Vek")
print(Hrac.name , Hrac.age)
Hrac.age = 55
print(Hrac.age)

# Atributy a metody
class Pouzdro:
    # constructor
    def __init__(self, name="anonym", age=10):
        self._name = name
        self._age = age


Hrac = Pouzdro() 
print("Jmeno a Vek", Hrac._name , Hrac._age)
Hrac._age = 50
print("Jmeno a Vek", Hrac._name , Hrac._age)