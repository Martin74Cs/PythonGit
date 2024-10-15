# pip install requests
import os
import requests

class books:

    def __init__(self, base): 
        self.baseadres = base

    def adresa(self, adresa):
        self.adresa = adresa

    def Get(self):
        # if(self.adresa is None or self.baseadres is None): return
        Adresa = f"{self.baseadres}{self.adresa}"
        # print("Adresa " , Adresa)
        response = requests.get(Adresa)
        print("response:", response)
        if response.status_code == 200:
            books = response.json()
            # print("Všechny knihy:")
            # for book in books:
            #     print(f"{book['id']}: {book['title']} od {book['author']}")
            return books
        else:
            print("Chyba při získávání knih:", response.status_code)
            return []

    def GetId(self,id):
        Adresa = f"{self.baseadres}{self.adresa}/{id}"
        print(Adresa)
        response = requests.get(Adresa)

        if response.status_code == 200:
            book = response.json()
            print(f"Kniha ID {id}: {book['title']} od {book['author']}")
            return book
        else:
            print("Kniha nenalezena:", response.status_code)

    def Post(self, novy):
        response = requests.post(f'{self.baseadres}{self.adresa}', json=novy)

        if response.status_code == 201:
            created_book = response.json()
            print("Nová kniha vytvořena:", created_book)
        else:
            print("Chyba při vytváření knihy:", response.status_code)

    def Put(self, id, data):
        response = requests.put(f'{self.baseadres}{self.adresa}/{id}', json=data)

        if response.status_code == 200:
            updated_book = response.json()
            print("Kniha aktualizována:", updated_book)
        else:
            print("Chyba při aktualizaci knihy:", response.status_code)

    def Delete(self, id):
        response = requests.delete(f'{self.baseadres}{self._adresa}/{id}')

        if response.status_code == 200:
            print("Kniha smazána.")
        else:
            print("Chyba při mazání knihy:", response.status_code)

os.system("cls")
# book = books("http://127.0.0.1:8080")
book = books("http://10.55.1.84:8080")
book.adresa = "/api/books"
print(f"{book.baseadres}{book.adresa}")

# book.Get()
# print()
 
test = book.GetId(1)
print(test)

# polozka = {
#     "title": "Fahrenheit 451",
#     "author": "Ray Bradbury"
# }
# book.Post(polozka)
# print()
# book.Get()
# print()

# update_data = {
#     "title": "Brave New World Revisited"
# }
# book.Put(2, update_data)
print("Všechny knihy")
test = book.Get()
print(test)
# for book in test:
#     print(f"{book['id']}: {book['title']} od {book['author']}")