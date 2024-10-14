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
max_iter = 50
zoom = 200  # Počáteční zoom
offset_x = 0
offset_y = 0

# Funkce pro výpočet Mandelbrotovy množiny
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

# Funkce pro vykreslení Mandelbrotovy množiny
def draw_mandelbrot():
    for x in range(screen_width):
        for y in range(screen_height):
            # Převod souřadnic obrazovky na komplexní rovinu
            real = (x - screen_width / 2) / zoom + offset_x
            imag = (y - screen_height / 2) / zoom + offset_y
            c = complex(real, imag)
            color_value = mandelbrot(c, max_iter)

            # Barvení bodu podle počtu iterací
            color = (color_value % 8 * 32, color_value % 16 * 16, color_value % 32 * 8)
            screen.set_at((x, y), color)

# Hlavní smyčka hry
running = True
while running:
    screen.fill(black)
    draw_mandelbrot()  # Vykresli Mandelbrotovu množinu
    
    pygame.display.update()  # Aktualizuj obrazovku

    # Zpracování událostí
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Zoom pomocí kolečka myši
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Kolečko myši nahoru (přiblížení)
                zoom *= 1.2
            if event.button == 5:  # Kolečko myši dolů (oddálení)
                zoom /= 1.2

            if event.button == 1 and selecting:
                selecting = False
                end_x, end_y = pygame.mouse.get_pos()

        # Posun kurzorem myši při zoomu
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:  # Držení levého tlačítka myši pro posun
                mouse_x, mouse_y = pygame.mouse.get_pos()
                offset_x += (mouse_x - screen_width / 2) / zoom
                offset_y += (mouse_y - screen_height / 2) / zoom

pygame.quit()
