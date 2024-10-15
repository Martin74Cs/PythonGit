print("Hello, World!")

class Abc:
    Simko = "Simko"

    @staticmethod
    def print_test():
        # print(Simko # Chyba 
        print(Abc.Simko)
        print(Abc().Simko)

    @classmethod        
    def print_DDD():
        print("DDD")

    def print_BBB():
        print(Abc.Simko)
        print(Abc().Simko)

    def print_CCC(self):
        print(self.Simko)

    def print_AAA(cls):
        print(cls.Simko)

print("----- Super -----------")
obj1 = Abc()
print(obj1.Simko) 
print(Abc.Simko) 

obj1.Simko = "Alena"
print(obj1.Simko) 
Abc.Simko = "Martin "
print(Abc.Simko) 

print("----- Abc() -----------")
obj1 = Abc()
obj1.print_test()
Abc().print_test()
Abc.print_test()

print("----- BBB() -----------")
# Abc.print_AAA() # Chyba
Abc().print_AAA() 
Abc().print_AAA # chyba není ale nefunguje
Abc.print_AAA # chyba není ale nefunguje
# Abc().print_BBB()
# Abc.print_BBB()

print("----- CCC -----------")
# Abc.print_CCC() # Chyba - Mustí být jako instance
Abc().print_CCC()

print("----- DDD -----------")
# Abc().print_DDD() # Chyba
# Abc.print_DDD() # Chyba
