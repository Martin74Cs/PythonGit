# Vypíše jednotlivé adresáře a soubory 

import os
from datetime import datetime

def GetDatum(zadane_datum):
    # Převeď zadané datum na datetime objekt
    try:
        return datetime.strptime(zadane_datum, '%Y-%m-%d')
    except ValueError:
        print("Špatný formát data. Použij formát YYYY-MM-DD.")
        print(f"Chyba: {e}")
        return None

def vypis_strom(adresar, soubor, datum, odsazeni=""):
    # if datum == "":
    #     quit()
    # Zapiš název aktuálního adresáře
    soubor.write(f"{odsazeni}{"-"} {os.path.basename(adresar)}\n")
     # Získání seznamu všech souborů a podadresářů v aktuálním adresáři
    polozky = os.listdir(adresar)
    
    # Iterace přes podadresáře
    for polozka in polozky:
        cesta = os.path.join(adresar, polozka)
        if os.path.isdir(cesta):
            # Rekurzivní volání pro podadresáře
            vypis_strom(cesta, soubor, datum, odsazeni + "\t")
        else:
            # Získej datum poslední úpravy
            timestamp = os.path.getmtime(cesta)
            datum_upravy = datetime.fromtimestamp(timestamp)
            if datum_upravy > datum:
                # Zapiš název souboru
                soubor.write(f"{odsazeni} {"-"} {polozka}\n")

if __name__ != "__main__":
    print("Skript byl importován jako modul.")
    # Ukončení skriptu
    quit()

# Zadej výchozí adresář a cestu k výstupnímu souboru
# start_adresar = "g:\z\P.020394\Podklady_vstup\Zakaznik\A58_Nová tavírna\240919_Aktualizované podklady k technologiím"  # Nahraď vlastní cestou
start_adresar = "g:/z/P.020394/Podklady_vstup/Zakaznik/A58_Nová tavírna/240919_Aktualizované podklady k technologiím"  # Nahraď vlastní cestou
zadane_datum = "2024-10-11"   # Nahraď požadovaným datem ve formátu YYYY-MM-DD
output_file = "vypis.txt"

datum = GetDatum(zadane_datum)
print(datum)
# Otevři soubor pro zápis
with open(output_file, "w", encoding="utf-8") as soubor:
    vypis_strom(start_adresar, soubor, datum )

print("Výpis dokončen.")