import os
from APIrequests import API

if __name__ == "__main__":
    # Vyčištění konzole
    os.system("cls" if os.name == "nt" else "clear")

    # Definice adresy API
    adresa = "http://10.55.1.100/api/elektro"

    # Volání API a uložení odpovědi
    response = API(adresa)

    # Výpis odpovědi
    print(response)