import pygame
import random
import numpy as np
from tensorflow import keras
import tensorflow as tf

print("Inicializace...")

# Konstanty
SIRKA = 800
VYSKA = 600
RYCHLOST_PALKY = 5
RYCHLOST_MICKU = 5
VELIKOST_PALKY = 100

# Inicializace Pygame
pygame.init()
obrazovka = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption("Pimpong s neuronovými sítěmi (TensorFlow/Keras)")
hodiny = pygame.time.Clock()

print("Pygame inicializováno")

# Definice neuronové sítě
def vytvor_sit():
    model = keras.Sequential([
        keras.layers.Dense(16, activation='relu', input_shape=(4,)),  # Změněno na 4 vstupy
        keras.layers.Dense(16, activation='relu'),
        keras.layers.Dense(3, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy')
    return model

# Vytvoření a inicializace neuronových sítí
sit1 = vytvor_sit()
sit2 = vytvor_sit()

print("Neuronové sítě inicializovány")

# Inicializace herních objektů
palka1 = pygame.Rect(50, VYSKA // 2 - VELIKOST_PALKY // 2, 10, VELIKOST_PALKY)
palka2 = pygame.Rect(SIRKA - 60, VYSKA // 2 - VELIKOST_PALKY // 2, 10, VELIKOST_PALKY)
micek = pygame.Rect(SIRKA // 2 - 15, VYSKA // 2 - 15, 30, 30)

rychlost_micku = [RYCHLOST_MICKU * random.choice((1, -1)), RYCHLOST_MICKU * random.choice((1, -1))]

def ziskej_stav(palka, micek, rychlost_micku):
    return np.array([[
        palka.y / VYSKA,
        micek.y / VYSKA,
        rychlost_micku[0] / RYCHLOST_MICKU,  # Normalizovaná x-ová složka rychlosti
        rychlost_micku[1] / RYCHLOST_MICKU   # Normalizovaná y-ová složka rychlosti
    ]])

def proved_akci(palka, akce):
    if akce == 0:  # Nahoru
        palka.y = max(palka.y - RYCHLOST_PALKY, 0)
    elif akce == 2:  # Dolů
        palka.y = min(palka.y + RYCHLOST_PALKY, VYSKA - palka.height)

def reset_micek():
    micek.center = (SIRKA // 2, VYSKA // 2)
    return [RYCHLOST_MICKU * random.choice((1, -1)), RYCHLOST_MICKU * random.choice((1, -1))]

print("Začíná hlavní herní smyčka")

# Hlavní herní smyčka
skore1 = 0
skore2 = 0
bezi = True
frame_count = 0
ucici_frekvence = 10  # Učení každých 10 snímků
pamet1 = []
pamet2 = []

@tf.function
def predict_batch(model, states):
    return model(states)

while bezi:
    frame_count += 1
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            bezi = False

    # Získání stavů a provedení akcí
    stav1 = ziskej_stav(palka1, micek, rychlost_micku)
    stav2 = ziskej_stav(palka2, micek, rychlost_micku)
    
    akce1 = np.argmax(predict_batch(sit1, stav1))
    akce2 = np.argmax(predict_batch(sit2, stav2))
    
    proved_akci(palka1, akce1)
    proved_akci(palka2, akce2)

    # Pohyb míčku
    micek.x += rychlost_micku[0]
    micek.y += rychlost_micku[1]

    # Odraz míčku od horní a dolní stěny
    if micek.top <= 0 or micek.bottom >= VYSKA:
        rychlost_micku[1] = -rychlost_micku[1]

    # Detekce kolize s pálkami
    if micek.colliderect(palka1):
        rychlost_micku[0] = abs(rychlost_micku[0])  # Zajistí pohyb doprava
        rychlost_micku[1] += (micek.centery - palka1.centery) / (VELIKOST_PALKY / 2) * RYCHLOST_MICKU  # Přidá vertikální složku podle místa odrazu
    elif micek.colliderect(palka2):
        rychlost_micku[0] = -abs(rychlost_micku[0])  # Zajistí pohyb doleva
        rychlost_micku[1] += (micek.centery - palka2.centery) / (VELIKOST_PALKY / 2) * RYCHLOST_MICKU  # Přidá vertikální složku podle místa odrazu

    # Normalizace rychlosti míčku
    rychlost = (rychlost_micku[0]**2 + rychlost_micku[1]**2)**0.5
    rychlost_micku[0] = rychlost_micku[0] / rychlost * RYCHLOST_MICKU
    rychlost_micku[1] = rychlost_micku[1] / rychlost * RYCHLOST_MICKU

    # Skórování a reset míčku
    if micek.left <= 0:
        skore2 += 1
        rychlost_micku = reset_micek()
    elif micek.right >= SIRKA:
        skore1 += 1
        rychlost_micku = reset_micek()

    # Ukládání zkušeností
    odmena1 = 1 if micek.colliderect(palka1) else -1 if micek.left <= 0 else 0
    odmena2 = 1 if micek.colliderect(palka2) else -1 if micek.right >= SIRKA else 0
    pamet1.append((stav1, akce1, odmena1))
    pamet2.append((stav2, akce2, odmena2))

    # Učení neuronových sítí
    if frame_count % ucici_frekvence == 0:
        if pamet1:
            stavy1, akce1, odmeny1 = zip(*pamet1)
            y_true1 = np.zeros((len(pamet1), 3))
            y_true1[np.arange(len(pamet1)), akce1] = odmeny1
            sit1.train_on_batch(np.vstack(stavy1), y_true1)
            pamet1 = []

        if pamet2:
            stavy2, akce2, odmeny2 = zip(*pamet2)
            y_true2 = np.zeros((len(pamet2), 3))
            y_true2[np.arange(len(pamet2)), akce2] = odmeny2
            sit2.train_on_batch(np.vstack(stavy2), y_true2)
            pamet2 = []

    # Vykreslení
    obrazovka.fill((0, 0, 0))
    pygame.draw.rect(obrazovka, (255, 255, 255), palka1)
    pygame.draw.rect(obrazovka, (255, 255, 255), palka2)
    pygame.draw.ellipse(obrazovka, (255, 255, 255), micek)
    pygame.draw.aaline(obrazovka, (255, 255, 255), (SIRKA // 2, 0), (SIRKA // 2, VYSKA))

    font = pygame.font.Font(None, 36)
    text = font.render(f"{skore1} : {skore2}", True, (255, 255, 255))
    obrazovka.blit(text, (SIRKA // 2 - 40, 10))

    pygame.display.flip()
    hodiny.tick(60)

    if frame_count % 1000 == 0:
        print(f"Frame {frame_count}, Skóre: {skore1}:{skore2}")

print("Hra skončila")
pygame.quit()
