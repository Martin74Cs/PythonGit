
#
# Výpočet přeletů mouchy mezi vlaky 
#

def vypocet_letu_mouchy(vzdalenost, rychlost_vlaku1, rychlost_vlaku2, rychlost_mouchy,cas_obratumouchy):
    """
    Vypočítá, kolikrát moucha přeletí mezi vlaky před jejich srážkou.
    
    :param vzdalenost: Počáteční vzdálenost mezi vlaky v km
    :param rychlost_vlaku1: Rychlost prvního vlaku v km/h
    :param rychlost_vlaku2: Rychlost druhého vlaku v km/h
    :param rychlost_mouchy: Rychlost mouchy v km/h
    :return: Počet přeletů mouchy a čas do srážky vlaků
    """
    cas = 0
    pozice_mouchy = 0
    pocet_preletu = 0
    smer = 1  # 1 pro let doprava, -1 pro let doleva
    krok_casu = 0.000001  # Malý časový krok pro přesnější aproximaci
    

    while vzdalenost > 0:
        cas += krok_casu
        vzdalenost -= (rychlost_vlaku1 + rychlost_vlaku2) * krok_casu
        pozice_mouchy += rychlost_mouchy * krok_casu * smer

        if pozice_mouchy >= vzdalenost or pozice_mouchy <= 0:
            pocet_preletu += 1
            smer *= -1  # Změna směru letu mouchy
            pozice_mouchy += (cas_obratumouchy + rychlost_mouchy * smer)

    return pocet_preletu, cas

# Vstupní parametry
vzdalenost = float(input("Zadejte počáteční vzdálenost mezi vlaky (km): "))
rychlost_vlaku1 = float(input("Zadejte rychlost prvního vlaku (km/h): "))
rychlost_vlaku2 = float(input("Zadejte rychlost druhého vlaku (km/h): "))
rychlost_mouchy = float(input("Zadejte rychlost mouchy (km/h): "))
cas_obratumouchy = 0.2
# Výpočet
pocet_preletu, cas_do_srazky = vypocet_letu_mouchy(vzdalenost, rychlost_vlaku1, rychlost_vlaku2, rychlost_mouchy, cas_obratumouchy)

# Výstup
print(f"\nMoucha přeletí mezi vlaky {pocet_preletu} krát.")
print(f"\nOtočka mouchy trvá {cas_obratumouchy} sekund.")
print(f"Čas do srážky vlaků: {cas_do_srazky:.2f} hodin.")
