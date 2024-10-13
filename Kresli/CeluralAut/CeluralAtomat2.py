import pygame
import numpy as np

# Nastavení
grid_size = 50  # velikost mřížky
cell_size = 15  # velikost buňky (pixelů)
width, height = grid_size * cell_size, grid_size * cell_size
black, white, gray = (0, 0, 0), (255, 255, 255), (50, 50, 50)

# Inicializace pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hra života - nastav buňky a spusť simulaci")
clock = pygame.time.Clock()

# Inicializace mřížky
grid = np.zeros((grid_size, grid_size))

# Funkce pro vykreslení mřížky
def draw_grid():
    for x in range(0, width, cell_size):
        for y in range(0, height, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            if grid[y // cell_size][x // cell_size] == 1:
                pygame.draw.rect(screen, white, rect)
            else:
                pygame.draw.rect(screen, black, rect)
            pygame.draw.rect(screen, gray, rect, 1)

# Funkce pro aktualizaci mřížky podle pravidel Hry života
def update_grid():
    new_grid = grid.copy()
    for i in range(grid_size):
        for j in range(grid_size):
            total = (grid[i, (j-1)%grid_size] + grid[i, (j+1)%grid_size] +
                     grid[(i-1)%grid_size, j] + grid[(i+1)%grid_size, j] +
                     grid[(i-1)%grid_size, (j-1)%grid_size] + grid[(i-1)%grid_size, (j+1)%grid_size] +
                     grid[(i+1)%grid_size, (j-1)%grid_size] + grid[(i+1)%grid_size, (j+1)%grid_size])
            
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
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not simulation:
            x, y = pygame.mouse.get_pos()
            # Přepínání mezi živou (1) a mrtvou (0) buňkou pomocí podmínky
            if grid[y // cell_size][x // cell_size] == 0:
                grid[y // cell_size][x // cell_size] = 1
            else:
                grid[y // cell_size][x // cell_size] = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                simulation = not simulation  # Přepíná mezi režimem nastavování a simulací
    
    if simulation:
        grid = update_grid()
    
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
