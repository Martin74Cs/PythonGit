# Proměná name obsahuje informace o jménu modulu
# lze využít při importování zavislých souboru

# Definice fukcí
def Pokus():
    print("Funkce pokus")

# V proměné name je __main__ pokud je spuštěno jako hlavni
# Pokud je spůštěno jako import obsahuje jsméno souboru
print("__name__ " + __name__)

if __name__=="__main__":
    a = input("jmeno > ")
    print("jedna " , a)

print("Test")
object.__str__("Tisk")

qwe : int = 10
print(qwe)

qwe = "asdf"
print(qwe)
