
# float
a = 5.56
print("Datový typ " , type(a) , "Proměná " , a)

# int
a = 5
print("Datový typ " , type(a) , "Proměná " , a)

# string
a = "aaa"
print("Datový typ " , type(a) , "Proměná " , a)

# comlex
a = 3j+1
print("Datový typ " , type(a) , "Proměná " , a)
print("Komplexní násobení ", a,"*", a, "=", a * a )
print("Komplexní Sčitání ", a, "+", a, "=",  a + a )

# tuple
# nejde změnit ani doplnit
a = ()
print("Datový typ " , type(a) , "Proměná " , a)
a = ("okurka", "citron", "jahoda")
print("Datový typ " , type(a) , "Proměná " , a)

# bude načten předchozí seznam a 
a = list(a)
print("Datový typ " , type(a) , "Proměná " , a)
# nyní lze přidávat a mazat
a.append("citron")
print("Datový typ " , type(a) , "Proměná " , a)
a.remove("okurka")
print("Datový typ " , type(a) , "Proměná " , a, "Index", a.index("jahoda") )

# pole
a = []
print("Datový typ " , type(a) , "Proměná " , a)

# přidání hodnot
a.append("Auto")
a.append(12)
a.append("Liska")
print("Datový typ " , type(a) , "Proměná " , a)
a.remove(12)
print("Datový typ " , type(a) , "Proměná " , a)
a.insert(0,"Hrnek")
print("Datový typ " , type(a) , "Proměná " , a)

# dict
a = {}
print("Datový typ " , type(a) , "Proměná " , a)
#  zadaní a vypis hodnot
x = {"name": "Suraj", "age": 24}
print("Datový typ " , type(x) , "Proměná " , x)

# set
# opakování hodnot bude zrušeno
a = {"geeks", "for", "geeks"}
print("Datový typ " , type(a) , "Proměná " , a)

# frozenset
a = frozenset({"Jedna", "Dva", "Tri" , "Jedna"})
print("Datový typ " , type(a) , "Proměná " , a)

# range - asi rozsah
a = range(10)
print("Datový typ " , type(a) , "Proměná " , a)

# bool
a = True # False
print("Datový typ " , type(a) , "Proměná " , a)

# bytes
a = b"Geeks"
print("Datový typ " , type(a) , "Proměná " , a)

# bytearray
a = bytearray(4)
print("Datový typ " , type(a) , "Proměná " , a)

# memoryview
a = memoryview(bytes(6))
print("Datový typ " , type(a) , "Proměná " , a)

# NoneType
a = None
print("Datový typ " , type(a) , "Proměná " , a)

