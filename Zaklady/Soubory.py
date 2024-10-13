import os
import pathlib
import shutil
import sys

os.system("cls")
print("__name__")
print(__name__)

print("__file__")
print(__file__)

print("__doc__")
print(__doc__)

# Tento export:
# všechny funkce z posixu nebo nt, např. unlink, stat, atd.
# os.path je buď posixpath nebo ntpath
# os.name je buď 'posix' nebo 'nt'
# os.curdir je řetězec představující aktuální adresář (vždy '.').
# os.pardir je řetězec představující nadřazený adresář (vždy „..“)
# os.sep je oddělovač (nebo nejběžnější oddělovač) názvů cest ('/' nebo '\').
# os.extsep je oddělovač přípon (vždy '.')
# os.altsep je oddělovač alternativních názvů cest (None nebo '/').
# os.pathsep je oddělovač komponent používaný v $PATH atd.
# os.linesep je oddělovač řádků v textových souborech ('\r' nebo '\n' nebo '\r\n')
# os.defpath je výchozí vyhledávací cesta pro spustitelné soubory
# os.devnull je cesta k souboru nulového zařízení ('/dev/null' atd.)

# přejmenování souboru podle přípony souboru
def changeFileExtension(file_path, new_extension):
    base_name, _ = os.path.splitext(file_path)
    new_file_path = base_name + new_extension
    new_file_path
    if not(os.path.exists(new_file_path)):
        # nejde přejmenovat pokud existuje
        os.rename(file_path, new_file_path)
 
# změna přípony souboru k zadané ceste.
def changeExtension(file_path, new_extension) -> str:
    base_name, _ = os.path.splitext(file_path)
    new_file_path = base_name + new_extension
    return new_file_path

if __name__ == "__main__":
    cesta = os.path.realpath(__file__)
    print("Cesta k aktuálnímu skriptu:", cesta)
    cesta = __file__
    print("Cesta k aktuálnímu skriptu:", cesta)

    # cesta k aktulnímu adresáži
    directory = os.path.dirname(cesta)
    print("Adresář:", directory)

    # jméno souboru z cesty k souboru
    directory = os.path.basename(cesta)
    print("Jmeno soubor:", directory)

    directory = os.path.splitext(cesta)
    print("Přípona souboru jako pole:", directory)

    directory = os.path.splitdrive(cesta)
    print("Disk jako pole:", directory)

    # Příklad použití:
    # cesta = __file__
    directory = os.path.dirname(__file__)
    Adresar =  os.path.join(directory, "Save")
    # Jedná o vložení cesta do třídy 
    # potom lze použít metody třídy s tečkovou notací
    libAdresar = pathlib.Path(Adresar)
    print("Cesta1: " , directory)
    print("Cesta2: " , Adresar)
    print("Cesta3: " , libAdresar)
    print("Cesta4: " , pathlib.Path(os.path.dirname(Adresar)))
    # soubor = Adresar + "\\Save" + "\\txt.txt"
    soubor = os.path.join(Adresar, "Txt.txt")
       
    # Vytvoření adresáře pokud nexistuje    
    # musí být součástí pathlib.Path
    libAdresar.mkdir(parents=True, exist_ok=True)

    # Vytvoření adresáře včetně rodičovských složek, pokud neexistují
    os.makedirs(Adresar, exist_ok=True)
    # os.mkdir()

    # Otevření existence souboru
    if not os.path.exists(soubor):
        print("Soubor existuje:", soubor)
    else:
        print("Soubor NE-existuje:", soubor)

    # Oveření existence adresaře    
    if os.path.exists(cesta):
        print("Adresař existuje:", cesta)
    else:
        print("Adresař NE-existuje:", cesta)

    print()
    print("Cesta k souboru:", soubor)
    print("Cesta k Adresar:", cesta)

    if not os.path.exists(soubor):
    # UVOLNENI ZDROJE POUŽITÍ PŘI PRÁCI SOUBORU A DATABAZI:
        with open(soubor, mode="w", encoding="utf-8", buffering=1 , newline="\n") as fs:
            fs.write("První řádek\n")
            fs.write("Dva řádek\n")
            fs.close()
        print()
        print("Soubor vytvořen: ", soubor)
    else:
        print("Konec")
        sys.exit() 

    cil = changeExtension(soubor,".qwe")
    if os.path.exists(cil) :
        # shutil.copyfile(soubor, changeExtension(soubor,".qwe"))
        shutil.copy(soubor, cil)

    print("Cesta k souboru:", soubor)
    if os.path.exists(soubor):
        changeFileExtension(soubor, ".txt")
        print("Úspěšně změněno!")
    else:
        print("Soubor EXISTUJE" , soubor)
        sys.exit() 

    a = os.listdir(directory)
    print("Datový typ " , type(a) , "Proměná " , a)

    a = os.walk(directory) 
    print("Datový typ " , type(a) , "Proměná " , a)

    a = os.scandir() 
    print("Datový typ " , type(a) , "Proměná " , a)


print("Funguje")
print("Cesta ", __name__)

