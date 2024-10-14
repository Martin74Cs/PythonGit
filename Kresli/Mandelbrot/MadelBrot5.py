import pygame
import numpy as np

# Inicializace Pygame
pygame.init()

# Nastavení velikosti okna
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mandelbrotova množina s zoomem")

# Barvy
black = (0, 0, 0)

# Výchozí parametry Mandelbrotovy množiny
iterace = 50
zoom = 0  # Počáteční zoom
offsetx = 0
offsety = 0

# Funkce pro výpočet Mandelbrotovy množiny
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

# Funkce pro vykreslení Mandelbrotovy množiny
def draw_mandelbrot(x1, y1, x2, y2, width, height):
    print(x1, y1, x2, y2, width, height)
    print("data", (0 - width /2) / 2000, (width - width /2) / 200, (x1 - width /2) / 200 )
    offsetx = (x1 - screen_width / 2) / 200
    zoom = 1 
    print("offsetx" , offsetx)
    for x in range(width):
        for y in range(height):
            # Převod souřadnic obrazovky na komplexní rovinu
            # real = (x - width / 2) / zoom + offset_x
            # imag = (y - height / 2) / zoom + offset_y
            real = (x - width /2) / (200 + zoom) + offsetx
            imag = (y - height/2) / (200 + zoom) 
            c = complex(real, imag)
            color_value = mandelbrot(c, iterace)

            # Barvení bodu podle počtu iterací
            color = (color_value % 8 * 32, color_value % 16 * 16, color_value % 32 * 8)
            # print(x,y,color)
            screen.set_at((x, y), color) 

# Hlavní smyčka hry
running = True
x1 = y1 = 0
x2 = screen_width
y2= screen_height 
selecting = False

while running:
    # screen.fill(black)

    # Definování oblasti, kterou chceme vykreslit
    # xmin = offset_x  
    # xmax = offset_x 
    # ymin = offset_y  
    # ymax = offset_y  


    # Zpracování událostí
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Vykreslení Mandelbrotovy množiny postupně
                draw_mandelbrot(x1, y1, x2, y2, screen_width, screen_height)

        # Výběr oblasti pomocí myši
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Levé tlačítko myši
                selecting = True
                x1,y1 = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and selecting:
                selecting = False
                x2,y2 = pygame.mouse.get_pos()
                dx = abs(x2 - x1) 
                dy = abs(y2 - y1)
                print(x1, y1, x2, y2, dx, dy )
                offsetx = (screen_width / 2 )
                zoom = dx
                # Přepočítání nové oblasti pro zoom
                # print(xmin, xmax, ymin, ymax, screen_width, screen_height, max_iter)
    pygame.display.update()  # Aktualizuj obrazovku

pygame.quit()
