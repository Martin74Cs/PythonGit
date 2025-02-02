import requests
import json
import os
import Tridy
import random
import string

# from Tridy import Elektro

def randomSlovo(delka=10):
    return ''.join(random.choices(string.ascii_letters, k=delka))

def apiAll(url):
    print("začala metoda Všechny")
    # verify=False (rychlé, ale nebezpečné)
    headers = {"Content-Type": "application/json"}  
    response = requests.get(url, verify=False, headers=headers)
    if not response.status_code == 200:
        print("chyba")
        exit()
    # odpověd je kód jako dopadnul dotaz
    print("Odpověď respose " ,response)
    # tady je json jako slovník
    Out = response.json()
    print("response jako slovnik " ,Out)
    Pole = []

    for prvek in Out:
        # trida = Tridy.Elektro.jsonToObject(prvek)
        trida = Tridy.Elektro(**prvek)
        Pole.append(trida)
    return Pole

def apiPost(url, data):
    print("začala metoda Add")
    headers = {"Content-Type": "application/json"}  
    # verify=False (rychlé, ale nebezpečné)
    response = requests.post(url, json=data , headers=headers, verify=False)

    if response.status_code in [200, 201]:
        print("✅ Úspěšně odesláno!")
    else:
        print(f"⚠️ Chyba při odesílání: {response.status_code}")
    
    Out = response.json()
    print("response jako slovnik " ,Out)

    trida = Tridy.Elektro.json(Out)

    return trida

def apiDelete(url, id):
    print("začala metoda delete")
    # url = 'https://example.com/resource'
    # headers = {'ID': '123'}
    # response = requests.delete(url, headers=headers)

    # Nahrazení {id} za skutečné ID
    urlLink = f"{url}/{id}"
    print(urlLink)
    headers = {"Content-Type": "application/json"}  
    response = requests.delete(urlLink, headers=headers)
    # response = requests.delete(urlLink.format(id = id))
    if response.status_code != 200:
        print("Chyba ", response)
        # exit()
    else:
        print("záznam byl smazán ", response)
    return 

def apiPut(url, data):
    headers = {"Content-Type": "application/json"}  
    response = requests.post(url, json=data, headers=headers)
    Out = response.json()
    return Out

# Export dat pro profese
class ElekroEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "__dict__"):
            return obj.__dict__
        return super().default(obj)

# Jedna se o testovaní uvedených metod
if __name__ == "__main__":
    os.system("cls")
    # Funguje server musí být spuštěn
    # apiUrl = "http://10.55.1.100/api/elektro"
    apiUrl = "http://localhost/api/elektro"
    apiUrl = "http://localhost/api/Elektro/Relations"
    print(apiUrl)
    
    # Všechny záznamy vratí seznam tříd Elektro
    restultAll = apiAll(apiUrl)


    # Přidat záznam
    data = {"name": randomSlovo(5), "popis": randomSlovo(10)}
    Pole = apiPost(apiUrl, data)
    print(Pole)


    if restultAll:
        lastData = restultAll[-1]
        print("Poslední zaznam: " , lastData.apid)
        data = apiDelete(apiUrl, lastData.apid)  
        print("Toto je smazanáý záznam", data)

    # Save to a file
    print()
    print("Save sample.json ")
    
    restultAll = apiAll(apiUrl)
    data = json.dumps(restultAll, cls=ElekroEncoder, indent=4)
    print(data)

    with open("sample.json", "w") as outfile:
        outfile.write(data)
        # indent je počet mezer ve formátu json
        # json.dump([vars(obj) for obj in rest],  outfile=outfile, indent=4, ensure_ascii=False, cls=DateEncoder)
        # json_data = json.dumps([vars(obj) for obj in restultAll], indent=4)

        # for obj in restultAll:
            # print(vars(obj))
        

        # json.dump([vars(obj) for obj in restultAll],  outfile=outfile, indent=4)
        # json.dumps([vars(obj) for obj in restultAll], outfile, indent=4)
        # json.dumps(restultAll, outfile, indent=4)

    with open("sample.json", "r") as outfile:
        data = json.load(outfile)

    print("Tisk načteného souboru")
    print(type(data))    
    print(data)    