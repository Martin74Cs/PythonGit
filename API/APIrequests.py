import requests
import json
import os

from Tridy import Elektro

def API(url) -> any:
    response = requests.get(url)
    Out = response.json()
    return Out

def APIPost(url, data):
    response = requests.post(url, json=data)
    Out = response.json()
    return Out

def APIDelete(url, id):
    # Jiný příklad
    # url = 'https://example.com/resource'
    # headers = {'ID': '123'}
    # response = requests.delete(url, headers=headers)

    # Nahrazení {id} za skutečné ID
    urlLink = 'https://example.com/resource/{id}'
    response = requests.delete(urlLink.format(id=123))
    Out = response.json()
    return Out

def APIPut(url, data):
    response = requests.post(url, json=data)
    Out = response.json()
    return Out

if __name__ == "__main__":
    os.system("cls")
    # Funguje server musí být spuštěn
    api_url = "http://10.55.1.100/api/elektro"
    response = requests.get(api_url)
    if not response.status_code == 200:
        print("chyba")
        exit()
    print("Toto je Odpoveď respose") # odpověd je kód jako dopadnul dotaz
    print(response)
    rest = response.json()

    if rest:
        lastData = rest[-1]
        print("Poslední zaznam: " , lastData)
        print("Poslední zaznam: " , lastData['apid'])

        lastRecord = Elektro(lastData)
        # Apid = lastRecord['apid']       
        Apid = lastRecord.apid
        print("Apid: " , Apid)
    
    headers = {'apid': lastRecord.apid}
    print("Apid: " , headers)
    responsedel = requests.delete(api_url + "/" + lastRecord.apid)
    if responsedel.status_code != 200:
        print("chyba", responsedel)
        exit()

    print("delete ", responsedel)

    list =  response.json()
    # print("Toto je List")
    # print(list)

    test  = response.text
    # print("Toto je text")
    # print(test)

    # Save to a file
    with open("sample.json", "w") as outfile:
        # indent je počet mezer ve formátu json
        json.dump(list, outfile, indent=4)

    with open("sample.json", "r") as outfile:
        data = json.load(outfile)

    # print("Tisk načteného souboru")
    # print(type(data))    
    # print(test)    