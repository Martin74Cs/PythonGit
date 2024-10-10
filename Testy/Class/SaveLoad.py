import json
import xmltodict

# pip install xmltodict

class Person:
    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'city': self.city
        }

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age}, city={self.city})'

# Načtení z JSON
def LoadJson(filename: str) -> Person:
    with open(filename, 'r') as f:
        data = json.load(f)
    # Rekonstruujeme seznam přátel
    friends = [Person(**friend) for friend in data['friends']]
    return Person(data['name'], data['age'], data['city'], friends)
    # return Person(**data)

# Uložení do JSON
def SaveToJson(person : Person, filename: str):
    with open(filename, 'w') as f:
        json.dump(person.to_dict(), f, indent=4) # Přidáme odsazení pro lepší čitelnost

# Uložení do XML pomocí xmltodict
def SaveToXml(person: Person, filename: str):
    person_dict = {'person': person.to_dict()}
    with open(filename, 'w') as f:
        f.write(xmltodict.unparse(person_dict, pretty=True))

# Načtení z XML pomocí xmltodict
def LoadXml(filename: str) -> Person:
    with open(filename, 'r') as f:
        data = xmltodict.parse(f.read())['person']
    return Person(**data)

# Příklad použití Json
Lide = []
# person = Person("Martin", 49, "Ústí nad Labem")

Lide.append(Person("Martin", 49, "Ústí nad Labem"))
Lide.append(Person("Alena", 35, "Ústí nad Labem"))
SaveToJson(Lide, 'person.json')

# Příklad použití Json
person_loaded = LoadJson('person.json')
print(person_loaded)

# Příklad použití XML
SaveToXml(person, 'person_dict.xml')
person_loaded_from_xml_dict = LoadXml('person_dict.xml')
print(person_loaded_from_xml_dict)
