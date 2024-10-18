import sys                                      ; sys.path.append('D:\\bin\\py')
################################################################################
from equiplist import Document, Project, Revision, objById
########### STAVEBNÍ OBJEKTY / INŽENÝRSKÉ OBJEKTY / PROVOZNÍ SOUBORY ###########
from units import *
#################################### REVIZE ####################################
revs: list = []

#                                                          DFT
#                                                          PRL
#                                                          FIN
#                                                          CFC
#                                                          CAN
#                                                          ASB
#                     č.   YYYY MM DD   POPIS              AFL   ZPRAC.   KONTR.   SCHVÁ.
revs.append(Revision("A", "2024 10 17", "K připomínkám" , "PRL", "Šimko", "Fučík", "Počinek"))
revs.append(Revision("B", "2024 10 18", "K připomínkám" , "PRL", "Šimko", "Fučík", "Počinek"))
#evs.append(Revision("0", "2024 10 16", "Finální vydání", "FIN", "Šimko", "Fučík", "Počinek"))

#################################### PROJEKT ###################################
proj: object = Project()

proj.number = "P.020394 0202"
proj.client = "Povrly Copper Industries a.s."
proj.name   = "PCI—Rekonstrukce, rozšíření a modernizace závodu"

################################### DOKUMENTY ##################################
docs: list = []

docs.append(Document("", "SSaZ_vse", None, None, None))  # celý seznam
ID = 18; PS = objById(objs,ID); docs.append(Document("N", 8928, "D2.1–c" , f"{PS.pfx} {PS.num:02d}–{PS.name}",ID))
ID = 19; PS = objById(objs,ID); docs.append(Document("N", 8929, "D2.2–c" , f"{PS.pfx} {PS.num:02d}–{PS.name}",ID))
ID = 20; PS = objById(objs,ID); docs.append(Document("N", 8935, "D2.3–c" , f"{PS.pfx} {PS.num:02d}–{PS.name}",ID))
ID = 26; PS = objById(objs,ID); docs.append(Document("N", 8954, "D2.9–c" , f"{PS.pfx} {PS.num:02d}–{PS.name}",ID))
ID = 27; PS = objById(objs,ID); docs.append(Document("N", 9074, "D2.10–c", f"{PS.pfx} {PS.num:02d}–{PS.name}",ID))
ID = 28; PS = objById(objs,ID); docs.append(Document("N", 9075, "D2.11–c", f"{PS.pfx} {PS.num:02d}–{PS.name}",ID))
ID = 29; PS = objById(objs,ID); docs.append(Document("N", 9076, "D2.12–c", f"{PS.pfx} {PS.num:02d}–{PS.name}",ID))
ID = 30; PS = objById(objs,ID); docs.append(Document("N", 9077, "D2.13–c", f"{PS.pfx} {PS.num:02d}–{PS.name}",ID))

# Poznámky pod seznamen strojů a zařízení
#...,....1....,....2....,....3....,....4....,....5....,....6....,....7....,....8....,....9....,...10....,...11....,...12....,...13....,...14....,...15
Document.notes = """
- VÝZNAM PŘEDZNAMENÁNÍ U OZNAČENÍ TECHNOLOGICKÉHO CELKU / ZAŘÍZENÍ:
   - První alfabetický znak má význam typu technologického celku.  Může nabývat hodnot [H|X].
     Význam typu technologického celku: H = ZDVIHACÍ ZAŘÍZENÍ
                                        X = BALENÁ JEDNOTKA
   - První dvě číslice za alfabetickým znakem mají význam pořadového čísla technologického celku.  Může nabývat hodnot [0-9][0-9].
   - První číslice za tečkou má význam pořadového čísla dílčího technologického celku.  Může nabývat hodnot [1-9].
- BALENÉ JEDNOTKY OBSAHUJÍ POUZE VÝPIS ZÁKLADNÍCH KOMPONENT A JEJÍ CELKOVÝ ELEKTRICKÝ PŘÍKON JE OZNAČEN SYMBOLEM „∑“.
- NERELEVANTNÍ HODNOTY VZTAŽENÉ K ZAŘÍZENÍ NEBO NEZNÁMÉ HODNOTY JSOU OZNAČENY SYMBOLEM „—“.
"""
#...,....1....,....2....,....3....,....4....,....5....,....6....,....7....,....8....,....9....,...10....,...11....,...12....,...13....,...14....,...15

# vim:tw=10000:ts=4:sts=4:sw=4:noexpandtab:
