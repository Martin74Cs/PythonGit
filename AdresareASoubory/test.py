import os
from datetime import datetime

def porovnat_datum_souboru(start_adresar, zadane_datum, output_file):
    """
    Prochází adresář a jeho podadresáře, porovnává datum poslední úpravy souborů
    se zadaným datem a zapisuje odpovídající soubory do výstupního souboru.

    :param start_adresar: Výchozí adresář pro prohledávání
    :param zadane_datum: Zadané datum pro porovnání (ve formátu 'YYYY-MM-DD')
    :param output_file: Cesta k výstupnímu textovému souboru
    """
    # Převeď zadané datum na datetime objekt
    try:
        referencni_datum = datetime.strptime(zadane_datum, "%Y-%m-%d")
    except ValueError:
        print("Špatný formát data. Použij formát YYYY-MM-DD.")
        return

    # Otevři výstupní soubor pro zápis
    with open(output_file, "w", encoding="utf-8") as soubor:
        soubor.write(f"Soubory upravené po {referencni_datum.strftime('%d.%m.%Y')}:\n\n")
        # Procházej adresář
        for root, dirs, files in os.walk(start_adresar):
            for file in files:
                cesta = os.path.join(root, file)
                Aresar = os.path.join(root)
                if os.path.isdir(dirs):
                    print("Dir " + dirs)
                # Získej datum poslední úpravy
                timestamp = os.path.getmtime(cesta)
                datum_upravy = datetime.fromtimestamp(timestamp)
                # Porovnej s referenčním datem
                if datum_upravy > referencni_datum:
                    # Vypiš relativní cestu a datum úpravy
                    relativni_cesta = os.path.relpath(cesta, start_adresar)
                    soubor.write(f"{relativni_cesta} - {datum_upravy.strftime('%d.%m.%Y %H:%M:%S')}\n")

    print(f"Výpis dokončen. Výsledky jsou uložené v '{output_file}'.")

if __name__ == "__main__":
    # Zadej výchozí adresář, zadané datum a výstupní soubor
    start_adresar = "g:/z/P.020394/Podklady_vstup/Zakaznik/A58_Nová tavírna/240919_Aktualizované podklady k technologiím"  # Nahraď vlastní cestou
    zadane_datum = "2024-04-10"   # Nahraď požadovaným datem ve formátu YYYY-MM-DD
    output_file = "vypis.txt"

    porovnat_datum_souboru(start_adresar, zadane_datum, output_file)
