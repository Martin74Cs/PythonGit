import pygame
import numpy as np

# Inicializace Pygame
pygame.init()

# Nastavení velikosti okna
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mandelbrotova množina s výběrem oblasti a postupným vykreslováním")

# Barvy
black = (0, 0, 0)

# Výchozí parametry Mandelbrotovy množiny
max_iter = 256
zoom = 1.0  # Počáteční zoom
offset_x = -0.5
offset_y = 0.0

# Funkce pro výpočet iterací Mandelbrotovy množiny
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

# Funkce pro vykreslení bodu na základě komplexního čísla c
def draw_point(x, y, c, max_iter):
    color_value = mandelbrot(c, max_iter)

    # Barvení bodu podle počtu iterací
    color = (color_value % 8 * 32, color_value % 16 * 16, color_value % 32 * 8)
    # print(x,y,color)
    screen.set_at((x, y), color) 

# Funkce pro vykreslení Mandelbrotovy množiny postupně
def draw_mandelbrot_stepwise(xmin, xmax, ymin, ymax, width, height, max_iter):
    real_range = np.linspace(xmin, xmax, width)
    imag_range = np.linspace(ymin, ymax, height)

    for x in range(width):
        for y in range(height):
            c = complex(real_range[x], imag_range[y])
            draw_point(x, y, c, max_iter)

        pygame.display.update()  # Aktualizuje obrazovku po každém řádku

# Hlavní smyčka hry
running = True
selecting = False
start_x = start_y = 0
pygame.display.update()

screen.fill(black)
# Vykreslení Mandelbrotovy množiny postupně
draw_mandelbrot_stepwise(-2.5, 2.5, -2.5, 2.5 , screen_width, screen_height, max_iter)
while running:
    # screen.fill(black) 
    
    # Definování oblasti, kterou chceme vykreslit
    xmin = offset_x - 2.0 / zoom
    xmax = offset_x + 2.0 / zoom
    ymin = offset_y - 1.5 / zoom
    ymax = offset_y + 1.5 / zoom
    # draw_mandelbrot_stepwise(xmin, xmax, ymin, ymax, screen_width, screen_height, max_iter)

    # Zpracování událostí
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Výběr oblasti pomocí myši
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Levé tlačítko myši
                selecting = True
                start_x, start_y = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and selecting:
                selecting = False
                end_x, end_y = pygame.mouse.get_pos()
                if end_x - start_x == 0:
                    continue
                print(start_x, start_y, end_x, end_y)
                # Přepočítání nové oblasti pro zoom
                start_real = xmin + (start_x / screen_width) * (xmax - xmin)
                end_real = xmin + (end_x / screen_width) * (xmax - xmin)
                start_imag = ymin + (start_y / screen_height) * (ymax - ymin)
                end_imag = ymin + (end_y / screen_height) * (ymax - ymin)

                offset_x = (start_real + end_real) / 2
                offset_y = (start_imag + end_imag) / 2
                zoom *= screen_width / abs(end_x - start_x)
                print(xmin, xmax, ymin, ymax, screen_width, screen_height, max_iter)
                draw_mandelbrot_stepwise(xmin, xmax, ymin, ymax, screen_width, screen_height, max_iter)

    pygame.display.update()

pygame.quit()
