# pip install requests
import os
import requests

class books:

    def __init__(self, base): 
        self.BaseAdres = base

    # def adresa(cls):
    #      return cls.Adresa

    Adresa = ""

    def Get(self):
        # if(self.adresa is None or self.baseadres is None): return
        # Adresa = f"{self.baseadres}" + adresa()
        Adresa = f"{self.BaseAdres}{self.Adresa}"
        # print("Adresa " , Adresa)
        response = requests.get(Adresa)
        # print("response:", response)
        if response.status_code == 200:
            books = response.json()
            # print("Všechny knihy:")
            # for book in books:
            #     print(f"{book['id']}: {book['title']} od {book['author']}")
            return books
        else:
            print("Chyba při získávání knih:", response.status_code)
            return []

    def GetId(self, id : int):
        Adresa = f"{self.BaseAdres}{self.Adresa}/{id}"
        # print(Adresa)
        response = requests.get(Adresa)
        if response.status_code == 200:
            book = response.json()
            # print(f"Kniha ID {id}: {book['title']} od {book['author']}")
            return book
        else:
            print("Kniha nenalezena:", response.status_code)
            return []

    def Post(self, novy):
        response = requests.post(f'{self.BaseAdres}{self.Adresa}', json=novy)
        if response.status_code == 201:
            created = response.json()
            # print("Nová kniha vytvořena:", created_book)
            return created
        else:
            print("Chyba při vytváření knihy:", response.status_code)
            return []

    def Put(self, id, data):
        response = requests.put(f'{self.BaseAdres}{self.Adresa}/{id}', json=data)

        if response.status_code == 200:
            updated = response.json()
            print("Kniha aktualizována:", updated)
            return updated
        else:
            print("Chyba při aktualizaci knihy:", response.status_code)
            return []

    def Delete(self, id):
        response = requests.delete(f'{self.BaseAdres}{self.Adresa}/{id}')
        if response.status_code == 200:
            delete = response.json()
            print("Kniha smazána.", delete)
            return delete
        else:
            print("Chyba při mazání knihy:", response.status_code)
            return []
    
def Knihy():
    APIbook.Adresa = "/api/books"
    print(f"{APIbook.BaseAdres}{APIbook.Adresa}")

    Sbooks = APIbook.Get()
    print("Všechny knihy")
    for book in Sbooks:
        print(f"{book['id']}: {book['title']} od {book['author']}")
    print()
    
    Sbook1 = APIbook.GetId(2)
    print("Jedna kniha")
    print(Sbook1)
    print()

    polozka = {
        "title": "Fahrenheit 451",
        "author": "Ray Bradbury"
    }
    nova = APIbook.Post(polozka)
    print("Nová kniha vytvořena:", nova)
    print()

    # APIbook.Get()

    update_data = {"title": "Brave New World Revisited"  }
    APIbook.Put(2, update_data)
    test = APIbook.Get()
    for book in test:
        print(f"{book['id']}: {book['title']} od {book['author']}")
    print()

    test = APIbook.Delete(3)
    print("Delete kniha", test)

    Sbooks = APIbook.Get()
    print("Všechny kontrola")
    for book in Sbooks:
        print(f"{book['id']}: {book['title']} od {book['author']}")


os.system("cls")
# Získání názvu počítače
hostname = os.environ['COMPUTERNAME']
print(f"Název počítače: {hostname}")

APIbook = books("http://10.55.1.84:80")
if(hostname == "MARTIN"):
    APIbook = books("http://192.168.1.32:8080")

APIbook.Adresa = "/api/data"
print(f"{APIbook.BaseAdres}{APIbook.Adresa}")
Datas = APIbook.Get()
print("Všechny data")
print(Datas)
print()

# polozka = { "id": 0, "title": "Fahrenheit 451", "author": "Ray Bradbury" }
# Data = APIbook.Post(polozka)
# print("Data Add" , Data)

# Ukázková data
DataPrvni = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "Brave New World", "author": "Aldous Huxley"},
    { "id": 0, "title": "Fahrenheit 451", "author": "Ray Bradbury" },
]

for item in DataPrvni:
    Data = APIbook.Post(item)

Datas = APIbook.Get()

for item in Datas:
    Data = APIbook.Delete(item.id)

print("Všechny kontrola")
print(Datas)

