import json
import xmltodict
import os
import pathlib

# pip install xmltodict

class Person:
    def __init__(self, jmeno: str, age: int, city: str):
        self.__jmeno = jmeno
        self.__age = age
        self.__city = city
        # self.jmeno = jmeno
        # self.age = age
        # self.city = city

    def to_dict(self):
        return { 'Person' : {
            'jmeno': self.__jmeno,
            'age': self.__age,
            'city': self.__city
            }
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Person':
        # friends = [cls.from_dict(friend_data) for friend_data in data]
        return cls(
            data['Person']['jmeno'],
            data['Person']['age'],
            data['Person']['city'],
        )
    
    def __repr__(self):
        # return f'Person(name={self.jmeno}, age={self.age}, city={self.city})'
        return f'Person(name={self.__jmeno}, age={self.__age}, city={self.__city})'

# Načtení z JSON
def LoadJson(filename: str) -> list[Person]:
    if(os.path.exists(filename) == False ):  return []
    print(filename)
    with open(filename, 'r', encoding='utf-8', newline='\n') as f:
        data = json.load(f)
    print(data)
    
    # převod záznamu pole na person
    # people = [Person(**item) for item in data]

    # Převod dat zpět do objektů Person
    people = [Person(**fix_mangled_names(item)) for item in data]

    # Toto funguje ale používá se prevodní tabulka from_dict
    # seznam_trid_nacteny = [Person.from_dict(item) for item in data]

    # Desirilizace jednoho záznamu
    # person = Person(**JsonData)

    # Rekonstruujeme seznam přátel
    # friends = [Person(**friend) for friend in data['friends']]
    # return Person(data['name'], data['age'], data['city'], friends)
    # return Person(**data)

    # Ověření výsledku
    # for person in people:
    #     print(person)
        
    return people

# Pomocná funkce pro převod manglovaných atributů
def fix_mangled_names(dct):
    # Opravíme manglované názvy atributů
    return {
        key.replace('_Person__', ''): value
        for key, value in dct.items()
    }


# Export dat s využitím DateEncoder se použíje jen u parameru které nejsou standarními typy pro formátování json 
class DateEncoder(json.JSONEncoder):
	def default(self, obj):
		return obj.__dict__

# Uložení do JSON
def SaveToJson(people : Person, filename: str):
    # Funguje čeština
    with open(filename, 'w', encoding='utf-8', newline='\n') as f:

        json.dump([vars(person) for person in people], f , indent=4, ensure_ascii=False)

        # Funguje stejně
        # jsonData = json.dumps([vars(obj) for obj in people], indent=4, ensure_ascii=False, cls=DateEncoder)
        # f.write(jsonData)

        # Funguje stejně
        # json.dump([person.to_dict() for person in people], f, indent=4) # Přidáme odsazení pro lepší čitelnost

        # Funguje stejne 
        # jsonFile = json.dumps([vars(person) for person in people], indent=4, ensure_ascii=False)
        # f.write(jsonFile)

        # Export dat s využitím DateEncoder se použíje jen u parameru které nejsou standarními typy pro formátování json 
        # jsonData = json.dumps([vars(obj) for obj in people], indent=4, ensure_ascii=False, cls=DateEncoder)
        # f.write(jsonData)

# Uložení do XML pomocí xmltodict
def SaveToXml(person: Person, filename: str):
    # person_dict = {'person': person.to_dict()}
    # person_dict ={"Root": {"Person": [obj.to_dict() for obj in person]}}
    person_dict ={"Root": {"Person": [vars(obj) for obj in person]}}
    # Funguje čeština
    with open(filename, 'w', encoding='utf-8', newline='\n') as f:
    # with open(filename, 'w') as f:
        f.write(xmltodict.unparse(person_dict, pretty=True))

# Načtení z XML pomocí xmltodict
def LoadXml(filename: str) -> Person:
    with open(filename, 'r', encoding='utf-8', newline='\n') as f:
        xml_content = f.read()
    data = xmltodict.parse(xml_content)
    # data = [Person.from_dict(item) for item in data["Root"]["Person"]]
    # data = [Person(**item) for item in data["Root"]["Person"]]
    
    data = [Person(**fix_mangled_names(item)) for item in data["Root"]["Person"]]
    return data

os.system("cls")

# Příklad použití:
cesta = __file__
directory = os.path.dirname(cesta)
soubor = directory + "\\Podpora" + "\\txt.txt"

# Vytvoření adresáře pokud nexistuje
cesta = pathlib.Path(os.path.dirname(soubor))
cesta.mkdir(parents=True, exist_ok=True)

# Získání aktuálního adresáře
current_directory = os.getcwd()

# Získání adresáře, kde je spuštěný Python skript
current_directory = os.path.dirname(os.path.abspath(__file__))

# Příklad použití Json
Lide = []
# person = Person("Martin", 49, "Ústí nad Labem")

Lide.append(Person("Martin", 49, "Ústí nad Labem"))
Lide.append(Person("Alena", 35, "Ústí nad Labem"))
# Složení cesty k souboru v aktuálním adresáři
filename = os.path.join(cesta , 'person.json')
SaveToJson(Lide, filename)

# Příklad použití Json
person_loaded = LoadJson(filename)
print(person_loaded)

# Příklad použití XML
filename =os.path.join(cesta , 'person.xml')
print(filename)
SaveToXml(Lide, filename)
person_loaded_from_xml_dict = LoadXml(filename)
print(person_loaded_from_xml_dict)
