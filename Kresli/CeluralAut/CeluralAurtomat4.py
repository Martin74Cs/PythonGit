import pygame
import numpy as np
import json
import os

# Nastavení
grid_size = 150  # velikost mřížky
cell_size = 5  # velikost buňky (pixelů)
width, height = grid_size * cell_size, grid_size * cell_size + 50  # Výška zvětšena kvůli menu
black, white, gray, green, red = (0, 0, 0), (255, 255, 255), (50, 50, 50), (0, 255, 0), (255, 0, 0)

# Inicializace pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hra života - nastav buňky, spusť simulaci, ukládej a načítej")
clock = pygame.time.Clock()

# Inicializace mřížky (nyní int místo float)
grid = np.zeros((grid_size, grid_size), dtype=int)

# Funkce pro vykreslení mřížky
def draw_grid():
    for x in range(0, width, cell_size):
        for y in range(50, height, cell_size):  # Posunuto kvůli tlačítkům
            rect = pygame.Rect(x, y, cell_size, cell_size)
            if grid[(y - 50) // cell_size][x // cell_size] == 1:
                pygame.draw.rect(screen, white, rect)
            else:
                pygame.draw.rect(screen, black, rect)
            pygame.draw.rect(screen, gray, rect, 1)

# Funkce pro vykreslení tlačítek
def draw_buttons():
    pygame.draw.rect(screen, green, (10, 10, 100, 30))  # Tlačítko "Uložit"
    pygame.draw.rect(screen, green, (120, 10, 100, 30))  # Tlačítko "Načíst"
    pygame.draw.rect(screen, green, (230, 10, 180, 30))  # Tlačítko "Náhodně rozmístit"
    pygame.draw.rect(screen, green, (420, 10, 100, 30))  # Tlačítko "Náhodně rozmístit"

    font = pygame.font.SysFont(None, 24)
    save_text = font.render('Uložit', True, black)
    load_text = font.render('Načíst', True, black)
    random_text = font.render('Náhodně rozmístit', True, black)
    delete = font.render('Smazat', True, black)

    screen.blit(save_text, (25, 15))
    screen.blit(load_text, (135, 15))
    screen.blit(random_text, (240, 15))
    screen.blit(delete, (430, 15))

# Funkce pro uložení mřížky do souboru
def save_grid(filename="grid_save.json"):
    with open(filename, 'w') as f:
        json.dump(grid.tolist(), f)

# Funkce pro načtení mřížky ze souboru
def load_grid(filename="grid_save.json"):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            global grid
            grid = np.array(json.load(f))

# Funkce pro náhodné rozmístění buněk
def randomize_grid():
    global grid
    # grid = np.random.choice([0, 1], size=(grid_size, grid_size))
    ProcentaZivota=0.7
    # grid = np.random.choice([0, 1], size=(grid_size, grid_size), p=[1 - ProcentaZivota, ProcentaZivota])

    grid = np.zeros((grid_size, grid_size), dtype=int)  # Inicializace mřížky s mrtvými buňkami (0)
    fill_size = 10  # Velikost centrální vyplněné oblasti
    start = (grid_size - fill_size) // 2  # Výpočet začátku centrální oblasti
    end = start + fill_size  # Výpočet konce centrální oblasti

    # Vyplnění centrální oblasti živými buňkami (1)
    # grid[start:end, start:end] = np.random.choice([0, 1], size=(fill_size, fill_size))
    grid[start:end, start:end] = np.random.choice([0, 1], size=(fill_size, fill_size), p=[1 - ProcentaZivota, ProcentaZivota])
    save_grid()
    
# Funkce pro mazání
def delete_grid():
    global grid
    grid.fill(0)

# Funkce pro aktualizaci mřížky podle pravidel Hry života
def update_grid():
    new_grid = grid.copy()
    # row x->i , col y=->j
    for i in range(grid_size):
        for j in range(grid_size):
            for d in range(1,2):
                total = (grid[i, (j-d)%grid_size] + grid[i, (j+d)%grid_size] +
                        grid[(i-d)%grid_size, j] + grid[(i+d)%grid_size, j] +
                        grid[(i-d)%grid_size, (j-d)%grid_size] + 
                        grid[(i-d)%grid_size, (j+d)%grid_size] +
                        grid[(i+d)%grid_size, (j-d)%grid_size] + 
                        grid[(i+d)%grid_size, (j+d)%grid_size])
            
            if grid[i, j] == 1:
                if total < 2 or total > 3:
                    new_grid[i, j] = 0
            else:
                if total == 3:
                    new_grid[i, j] = 1
    return new_grid

# Hlavní smyčka
running = True
simulation = False
while running:
    screen.fill(black)
    draw_grid()
    draw_buttons()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            
            # Kliknutí na tlačítka
            if 10 <= x <= 110 and 10 <= y <= 40:  # Uložit
                save_grid()
            elif 120 <= x <= 220 and 10 <= y <= 40:  # Načíst
                load_grid()
            elif 230 <= x <= 230+180 and 10 <= y <= 40:  # Náhodně rozmístit
                randomize_grid()
            elif not simulation and y >= 50:  # Kliknutí do mřížky (pod menu)
                grid[(y - 50) // cell_size][x // cell_size] ^= 1  # Přepnutí buňky mezi živou a mrtvou
            elif 430 <= x <= 430+100 and 10 <= y <= 40:  # Náhodně rozmístit
                delete_grid()               
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                simulation = not simulation  # Přepínání mezi simulací a editací
    
    if simulation:
        grid = update_grid()
    
    pygame.display.flip()
    # clock.tick(500)

pygame.quit()