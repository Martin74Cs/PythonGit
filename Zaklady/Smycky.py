seznam = [1, 2, 3, 4, 5]
for prvek in seznam:
    print(prvek)

# Tato smyčka bude iterovat od 0 do 9
for i in range(10): #start, stop a volitelně step 
    print(i)

retezec = "Python"
for znak in retezec:
    print(znak)

slovnik = {'a': 1, 'b': 2, 'c': 3}
for klic, hodnota in slovnik.items():
    print(f"{klic}: {hodnota}")

for i in range(3,10): # Start na 3
    if i == 5:
        break  # Ukončí smyčku, když i dosáhne 5
    print(i)

#start, stop a volitelně step 
for i in range(1, 10, 2):  # Start na 1, iterace po dvou
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue  # Přeskočí sudá čísla
    print(i)

i = 0
while i < 5:
    print(i)
    i += 1  # Nezapomeň na změnu hodnoty, aby se smyčka jednou ukončila    

while True:
    vstup = input("Zadej 'q' pro ukončení: ")
    if vstup == 'q':
        break  # `break` ukončí smyčku    

for i in range(5):
    if i == 3:
        break  # Když se provede break, else se nespustí
    print(i)
else:
    print("Smyčka proběhla bez přerušení.")    