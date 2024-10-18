import json
import xmltodict
import os
# pip install xmltodict

# Načtení z JSON
def LoadJson(trida, filename: str) -> list:
    if(os.path.exists(filename) == False ):  return []
    with open(filename, 'r', encoding='utf-8', newline='\n') as f:
        data = json.load(f)
    # převod záznamu pole na person
    return [trida(**item) for item in data]

# Uložení do JSON
def SaveToJson(objects: list, filename: str):
    with open(filename, 'w', encoding='utf-8', newline='\n') as f:
        json.dump([vars(obj) for obj in objects], f , indent=4, ensure_ascii=False)

# Uložení do XML pomocí xmltodict
def SaveToXml(objects: list, filename: str):
    person_dict ={"Root": {objects[0].__class__.__name__: [vars(obj) for obj in objects]}}
    with open(filename, 'w', encoding='utf-8', newline='\n') as f:
        f.write(xmltodict.unparse(person_dict, pretty=True))

# Načtení z XML pomocí xmltodict
def LoadXml(trida, filename: str) -> list:
    if(os.path.exists(filename) == False ):  return []
    with open(filename, 'r', encoding='utf-8', newline='\n') as f:
        xml_content = f.read()
    data = xmltodict.parse(xml_content)
    # Převod záznamů na objekty dané třídy
    return [trida(**item) for item in data["Root"][cls.__name__]]   

os.system("cls")

class Person:
    def __init__(self, jmeno: str, age: int, city: str):
        self._jmeno = jmeno
        self._age = age
        self._city = city

# cesta k aktualnímu adresáři skritu
StartAdresar = os.path.dirname(__file__)
# Složení cesty k  adresáři
Adresar = os.path.join(StartAdresar, "Soubor")
# Vytvoření adresáře pokud nexistuje
os.makedirs(Adresar, exist_ok=True)

# Příklad použití Json
#  person = Person("Martin", 49, "Ústí nad Labem")
Lide = []
Lide.append(Person("Martin", 49, "Ústí nad Labem"))
Lide.append(Person("Alena", 35, "Ústí nad Labem"))

# Složení cesty k souboru 
filename = os.path.join(Adresar , 'person.json')
SaveToJson(Lide, filename)

# Příklad použití Json
print("personJson")
person_loaded = LoadJson(Person, filename)
print(person_loaded)

# Příklad použití XML
filename =os.path.join(Adresar , 'person.xml')
SaveToXml(Lide, filename)
personXml = LoadXml(Person, filename)
print("personXml")
print(personXml)
