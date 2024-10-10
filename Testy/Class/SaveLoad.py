import json
import xmltodict
import os

# pip install xmltodict

class Person:
    def __init__(self, jmeno: str, age: int, city: str):
        self.jmeno = jmeno
        self.age = age
        self.city = city

    def to_dict(self):
        return { 'Person' : {
            'jmeno': self.jmeno,
            'age': self.age,
            'city': self.city
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
        return f'Person(name={self.jmeno}, age={self.age}, city={self.city})'

# Načtení z JSON
def LoadJson(filename: str) -> list[Person]:
    with open(filename, 'r') as f:
        data = json.load(f)
        seznam_trid_nacteny = [Person.from_dict(item) for item in data]
        # data = json.load(f)    return [Person.from_dict(person) for person in data]
    # Rekonstruujeme seznam přátel
    # friends = [Person(**friend) for friend in data['friends']]
    # return Person(data['name'], data['age'], data['city'], friends)
    # return Person(**data)

# Uložení do JSON
def SaveToJson(people : Person, filename: str):
    with open(filename, 'w') as f:
        # json.dump(person.to_dict(), f, indent=4) # Přidáme odsazení pro lepší čitelnost
        json.dump([person.to_dict() for person in people], f, indent=4) # Přidáme odsazení pro lepší čitelnost

# Uložení do XML pomocí xmltodict
def SaveToXml(person: Person, filename: str):
    # person_dict = {'person': person.to_dict()}
    person_dict ={"Root": {"Person": [obj.to_dict() for obj in person]}}
    with open(filename, 'w') as f:
        f.write(xmltodict.unparse(person_dict, pretty=True))

# Načtení z XML pomocí xmltodict
def LoadXml(filename: str) -> Person:
    with open(filename, 'r') as f:
        xml_content = f.read()
        data = xmltodict.parse(xml_content)
        data = [Person.from_dict(item) for item in data["Root"]["Person"]]
    return data

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
filename = os.path.join(current_directory, 'person.json')
SaveToJson(Lide, filename)

# Příklad použití Json
person_loaded = LoadJson(filename)
print(person_loaded)

# Příklad použití XML
filename =os.path.join(current_directory, 'person.xml')
print(filename)
SaveToXml(Lide, filename)
person_loaded_from_xml_dict = LoadXml(filename)
print(person_loaded_from_xml_dict)
