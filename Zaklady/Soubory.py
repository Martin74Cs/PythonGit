import os
import pathlib
import shutil
import sys

os.system("cls")
# print(__name__)
# print(__file__)
# print(__doc__)

# This exports:
# all functions from posix or nt, e.g. unlink, stat, etc.
# os.path is either posixpath or ntpath
# os.name is either 'posix' or 'nt'
# os.curdir is a string representing the current directory (always '.')
# os.pardir is a string representing the parent directory (always '..')
# os.sep is the (or a most common) pathname separator ('/' or '\')
# os.extsep is the extension separator (always '.')
# os.altsep is the alternate pathname separator (None or '/')
# os.pathsep is the component separator used in $PATH etc
# os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
# os.defpath is the default search path for executables
# os.devnull is the file path of the null device ('/dev/null', etc.)

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
    directory = os.path.dirname(cesta)
    soubor = directory + "\\Soubor" + "\\txt.txt"

    # Vytvoření adresáře pokud nexistuje
    cesta = pathlib.Path(os.path.dirname(soubor))
    cesta.mkdir(parents=True, exist_ok=True)

    # Oveření existence souboru
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
        with open(soubor, mode="w", encoding="utf-8", buffering=1 , newline="/n") as fs:
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
        changeFileExtension(soubor, ".csv")
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
