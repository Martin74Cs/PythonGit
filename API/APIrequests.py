import requests
import json
import os
import Tridy
# from Tridy import Elektro

def apiAll(url):
    print("začala metoda Všechny")
    # verify=False (rychlé, ale nebezpečné)
    response = requests.get(url, verify=False)
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
        trida = Tridy.Elektro.json(prvek)
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

    # response = requests.post(url, json=data)
    Out = response.json()
    return Out

def apiIDelete(url, id):
    print("začala metoda delete")
    # url = 'https://example.com/resource'
    # headers = {'ID': '123'}
    # response = requests.delete(url, headers=headers)

    # Nahrazení {id} za skutečné ID
    # urlLink = 'https://example.com/resource/{id}'
    # response = requests.delete(urlLink.format(id=123))
    urlLink = f"{url}/{id}"
    print(urlLink)
    response = requests.delete(urlLink)
    # response = requests.delete(urlLink.format(id = id))
    if response.status_code != 200:
        print("Chyba ", response)
        exit()
    print("záznam byl smazán ", response)
    
    # Out = response.json()
    # print("response jako slovnik " ,Out)
    
    # text  = response.text
    # print("Toto je text ", text)

    # trida = Tridy.Elektro.json(Out)
    return 

def apiPut(url, data):
    response = requests.post(url, json=data)
    Out = response.json()
    return Out

if __name__ == "__main__":
    os.system("cls")
    # Funguje server musí být spuštěn
    # apiUrl = "http://10.55.1.100/api/elektro"
    apiUrl = "http://localhost/api/elektro"
    print(apiUrl)
    
    # Všechny záznamy
    rest = apiAll(apiUrl)
    print(rest)

    # Přidat záznam
    name = "xxxx" 
    popis = "dddd"
    data = {"name": name, "popis": popis}
    Pole = apiPost(apiUrl, data)
    print(Pole)


    if rest:
        lastData = rest[-1]
        print("Poslední zaznam: " , lastData.apid)
        # print("Poslední aspid: " , lastData['apid'])

        # pokus o převod na trřídu
        # lastRecord = Tridy.Elektro.json(lastData)
        # lastRecord = lastData
        # Apid = lastRecord['apid']       
        # Apid = lastRecord.apid
        # print("Apid: " , Apid)
    
        # Delete dle apid
        # headers = {'apid': lastRecord.apid}
        # print("Apid: " , headers)
        data = apiIDelete(apiUrl, lastData.apid)  
        print("Toto je smazanáý záznam", data)
        # print(list)  

    # Save to a file
    with open("sample.json", "w") as outfile:
        # indent je počet mezer ve formátu json
        json.dump(rest, outfile, indent=4)

    with open("sample.json", "r") as outfile:
        data = json.load(outfile)

    print("Tisk načteného souboru")
    print(type(data))    
    print(data)    