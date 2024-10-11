import os

class MujSeznam(list):
    def first(self):
        return self[0] if self else ""


def vypis_stromovou_strukturu(start_adresar, urovnen=0):
    # Procházíme adresářovou strukturu pomocí os.walk
    for root, dirs, files in os.walk(start_adresar):
        prvni = root + dirs
        print(prvni)
        # Výpis aktuálního adresáře
        odsazeni = "\t" * (urovnen * 4)  # Nastavení odsazení pro lepší čitelnost
        odsazeni = " " * (urovnen * 4)  # Nastavení odsazení pro lepší čitelnost
        print(f"{odsazeni}{os.path.basename(root)}")
        # print(f"{odsazeni}- {root}")
        
        # Nejprve výpis souborů v aktuálním adresáři
        files.sort()  # Volitelně seřadit soubory
        for file in files:
            print(f"{odsazeni}    {file}")
        
        # Poté výpis podadresářů
        dirs.sort()  # Volitelně seřadit adresáře
        for dir in dirs:
            vypis_stromovou_strukturu(os.path.join(root, dir), urovnen + 1)

# Zadej startovní adresář
start_adresar = "/cesta/k/adresari"
start_adresar = "g:/z/P.020394/Podklady_vstup/Zakaznik/A58_Nová tavírna/240919_Aktualizované podklady k technologiím"  # Nahraď vlastní cestou
vypis_stromovou_strukturu(start_adresar)