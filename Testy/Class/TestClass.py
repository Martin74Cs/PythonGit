print("Hello, World!")

class Abc:
    Simko = "Simko"

    @staticmethod
    def print_test():
        Abc.print_AAA()
        Abc().print_AAA()

        Abc.print_BBB()
        Abc().print_BBB()

        # Abc.print_CCC()
        Abc().print_CCC()

        # print_DDD()
        # Abc.print_DDD()
        # Abc().print_DDD()

        # print(Simko)
        print(Abc.Simko)
        print(Abc().Simko)

    @classmethod        
    def print_DDD():
        print("DDD")

    def print_CCC(self):
        print("CCC")

    @classmethod        
    def print_BBB(self):
        print("BBB")

    @staticmethod
    def print_AAA():
        print("AAAA")

print("----- Abc() -----------")
obj1 = Abc()
obj1.print_test()

print("----- Abc() -----------")
Abc().print_test()
print("-----")
Abc.print_test()

print("----- AAA -----------")
Abc.print_AAA()
Abc().print_AAA()

print("----- BBB -----------")
Abc.print_BBB()
Abc().print_BBB()

print("----- CCC -----------")
# Abc.print_CCC()
# Mustí být jako instance
Abc().print_CCC()

print("----- DDD -----------")
# Abc().print_DDD()
# Abc.print_DDD()
