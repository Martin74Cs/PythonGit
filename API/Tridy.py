#  https://json2csharp.com/code-converters/json-to-python

import os
from typing import List
from typing import Any
from dataclasses import dataclass
import json

@dataclass
class Entity:
    def  __init__(self) -> 'Entity':
        self.id = 0
        self.apid = ""

@dataclass
class DruhElektro(Entity):

    def  __init__(self,obj) -> 'DruhElektro':
        self.name = str(obj.get("name"))
        self.popis = str(obj.get("popis"))
        self.elektros = [ElektroElement(y) for y in obj.get("elektros")]

@dataclass
class ElektroElement(Entity):

    def  __init__(self, obj) -> 'ElektroElement':
        self.name = str(obj.get("name"))
        self.popis = str(obj.get("popis"))
        if obj.get("elektroId") is not None: self.elektroId = int(obj.get("elektroId"))
        if obj.get("elektroApid") is not None: self.elektroApid = str(obj.get("elektroApid"))
        if obj.get("elektro") is not None: self.elektro = str(obj.get("elektro"))
        if obj.get("elementId") is not None: self.elementId = int(obj.get("elementId"))
        if obj.get("elementApid") is not None: self.elementApid = str(obj.get("elementApid"))
        if obj.get("element") is not None: self.element = Element(obj.get("element"))

@dataclass
class Element(Entity):

    def  __init__(self, obj) -> 'Element':
        self.name = str(obj.get("name"))
        self.popis = str(obj.get("popis"))
        self.kategorieId = int(obj.get("kategorieId"))
        self.kategorieApid = str(obj.get("kategorieApid"))
        self.kategorie = Kategorie(obj.get("kategorie"))
        self.svorkys = [Svorky(y) for y in obj.get("svorkys")]

@dataclass
class Kategorie(Entity):

    def __init__(self,obj: Any) -> 'Kategorie':
        self.name = str(obj.get("name"))
        self.popis = str(obj.get("popis"))
        self.cislo = int(obj.get("cislo"))


@dataclass
class Elektro(Entity):

    def  __init__(self) -> 'Elektro':
        self.name = ""
        self.popis = ""
        self.elektroElements = []   
        self.druhElektroId = 0
        self.druhElektroApid = ""
        # self.druhElektro = DruhElektro(obj.get("druhElektro"))

    def  json(obj) -> 'Elektro':
        if obj.get("name") is not None: Elektro.name  = str(obj.get("name"))
        if obj.get("popis") is not None: Elektro.popis = str(obj.get("popis"))
        if obj.get("elektroElements") is not None: Elektro.elektroElements = [ElektroElement(y) for y in obj.get("elektroElements")]   
        if obj.get("druhElektroId") is not None: Elektro.druhElektroId = int(obj.get("druhElektroId")) 
        if obj.get("druhElektroApid") is not None: Elektro.druhElektroApid = str(obj.get("druhElektroApid"))
        if obj.get("druhElektro") is not None: Elektro.druhElektro = DruhElektro(obj.get("druhElektro"))

    # def  __init__(self,obj) -> 'Elektro':
    #     self.name = str(obj.get("name"))
    #     self.popis = str(obj.get("popis"))
    #     if obj.get("elektroElements") is not None: self.elektroElements = [ElektroElement(y) for y in obj.get("elektroElements")]   
    #     if obj.get("druhElektroId") is not None: self.druhElektroId = int(obj.get("druhElektroId")) 
    #     if obj.get("druhElektroApid") is not None: self.druhElektroApid = str(obj.get("druhElektroApid"))
    #     if obj.get("druhElektro") is not None: self.druhElektro = DruhElektro(obj.get("druhElektro"))

@dataclass
class Svorky(Entity):

    def  __init__(self,obj) -> 'Svorky':
        self.name = str(obj.get("name"))
        self.popis = str(obj.get("popis"))
        self.elementId = int(obj.get("elementId"))
        self.elementApid = str(obj.get("elementApid"))
        self.element = str(obj.get("element"))

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)

# Example Usage
if __name__ == "__main__":
    os.system("cls")
    asd = {'name': 'Python', 'popis': 'Python', 'id': 17, 'apid': 'ucxfswmw8', 'elektroElements' : [ {'name' : 'Python111', 'popis': 'Python11133' },{'name' : 'Python222', 'popis': 'Python22233' }] }
    print(asd)
    print(asd['elektroElements'])
    print(asd['elektroElements'][1])
    print(asd['elektroElements'][0]['name'])

    pokus = Elektro()
    print("name ", pokus.name)
    # print(json.dumps(pokus, indent=4 )) 

    Pokus = Elektro.json(asd)
    print('\nVysledky')
    print(pokus.elektroElements[0].name)
    print(pokus.name)

"""
from typing import Any
from dataclasses import dataclass
import json
import os

@dataclass
class Elektro:
    def __init__(self, obj):
        self.id = int(obj.get("id"))
        self.apid = str(obj.get("apid"))
        self.name = str(obj.get("name"))
        self.popis = str(obj.get("popis"))

@dataclass
class Test:
    def __init__(this, obj):
        this.name = str(obj.get("name"))
        this.Cislo = int(obj.get("cislo"))

    # def load(obj):
    #     jedna = int(obj.get("name"))
    #     dva = str(obj.get("cislo"))
    #     return Test(jedna, dva)

#  Example Usage
if __name__ == "__main__":
    os.system("cls")
    asd = {'name': 'Python', 'popis': 'Python', 'id': 17, 'apid': 'ucxfswmw8'}
    print(asd)
    test = Elektro(asd)
    print(test.apid)

    os.system("cls")
    asd = {'name': 'Python', 'cislo': 17}
    print(asd)
    test = Test(asd)
    print(test.name)    

"""