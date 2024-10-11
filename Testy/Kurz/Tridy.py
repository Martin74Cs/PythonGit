class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# staticmethod(function) -> method
# Convert a function to be a static method.
# A static method does not receive an implicit first argument. To declare a static method, use this idiom:
#      class C:
#          @staticmethod def f(arg1, arg2, ...):
#              ...
# It can be called either on the class (e.g. C.f()) or on an instance (e.g. C().f()). Both the class and the instance are ignored, and neither is passed implicitly as the first argument to the method.
# Static methods in Python are similar to those found in Java or C++. For a more advanced concept, see the classmethod builtin.

# Převeďte funkci na statickou metodu.
# Statická metoda neobdrží implicitní první argument. Chcete-li deklarovat statickou metodu, použijte tento idiom:
# třída C:
# @staticmethod def f(arg1, arg2, ...):
# ...
# Může být volána buď na třídě (např. C.f()) nebo na instanci (např. C().f()). Třída i instance jsou ignorovány a žádná z nich není předána implicitně jako první argument do metody.
# Statické metody v Pythonu jsou podobné těm, které se nacházejí v Javě nebo C++. Pokročilejší koncept naleznete ve vestavěné classmethod.

result = MathUtils.add(9, 8)
print(result)

class demoClass:
#  konstruktor třídy
    def __init__(self, a, b):
        self.a = a
        self.b = b

# metoda třídy
    def add(a, b):
        return a + b
 
    def diff(self):
        return self.a-self.b

test = demoClass(5,3)

hodnota = demoClass.add(5,3)
print(hodnota)

hodnota = demoClass.diff()
print(hodnota)

# convert the add to a static method
demoClass.add = staticmethod(demoClass.add)
print(demoClass.add(5,3))