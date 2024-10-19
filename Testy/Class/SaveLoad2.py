import json
import xmltodict
import os
import csv

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
    return [trida(**item) for item in data["Root"][trida.__name__]]   

os.system("cls")

def SaveToCsv(objects: list, filename: str):
    if not objects: return  

    # Získání názvů sloupců (atributů) z prvního objektu
    fieldnames = vars(objects[0]).keys()

    with open(filename, 'w', newline='\n', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
        # Zápis hlavičky
        writer.writeheader()
        # Zápis dat
        for obj in objects:
            writer.writerow(vars(obj))

# Dynamická funkce pro serializaci
def serialize(obj):
    """Serializuje objekt do slovníku."""
    serialized_data = {}
    for attr, value in vars(obj).items():
        # Zkontroluj, zda je hodnota instancí jiných tříd
        if isinstance(value, list):
            # Zpracuj seznam
            serialized_data[attr] = [serialize(item) if hasattr(item, '__dict__') else item for item in value]
        elif hasattr(value, '__dict__'):
            # Pokud je to instance třídy, rozbal ji
            nested_data = serialize(value)
            for nested_attr, nested_value in nested_data.items():
                serialized_data[f"{attr}.{nested_attr}"] = nested_value
        else:
            serialized_data[attr] = value
    return serialized_data


def SaveToCsv2(objects: list, filename: str):
    if not objects: return  

    # Serializace prvního objektu pro zjištění názvů sloupců
    fieldnames = list(serialize(objects[0]).keys())

    with open(filename, 'w', newline='\n', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')

        # Zápis hlavičky
        writer.writeheader()

        # Zápis dat
        for obj in objects:
            serialized = serialize(obj)  # Serializuj objekt
            writer.writerow(serialized)  # Zapiš do CSV

if __name__ == "__main__":
    
    class Person:
        def __init__(self, jmeno: str, age: int, city: str):
            self.jmeno = jmeno
            self.age = age
            self.city = city

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

    filename =os.path.join(Adresar , 'person.csv')
    SaveToCsv2(Lide, filename)

