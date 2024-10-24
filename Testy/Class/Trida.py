import os

class A:
    jedna = "Test"

# Funguje
print(A.jedna) # Tisk Test
print(A().jedna) # Tisk Test

A.jedna = "zmena"
# Funguje
print(A.jedna) # Tisk zmnena
print(A().jedna) # Tisk zmnena

class B:
    #  _jedna = "Test"
    _jedna = "Test"

    @property
    def jedna(self):
        return  self._jedna
    

    @jedna.setter 
    def jedna(self,x): 
        self._jedna = x
     

print("Třída B")
# Funguje
print(B._jedna)
print(B()._jedna)
# print(B().jedna)
b = B()
print(b.jedna)
b.jedna = "Jahoda"
print(b._jedna)
print(b.jedna)



