import pygame
import numpy as np

# Inicializace Pygame
pygame.init()

# Nastavení velikosti okna
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mandelbrotova množina s zoomem (optimalizováno)")

# Barvy
black = (0, 0, 0)

# Výchozí parametry Mandelbrotovy množiny
max_iter = 256
zoom = 200  # Počáteční zoom
offset_x = 0
offset_y = 0

# Funkce pro výpočet iterací Mandelbrotovy množiny
def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    # Vytvoříme mřížku pro komplexní čísla
    real = np.linspace(xmin, xmax, width)
    imag = np.linspace(ymin, ymax, height)
    real, imag = np.meshgrid(real, imag)
    c = real + 1j * imag
    
    # Inicializace Z a maska pro bod v množině
    z = np.zeros_like(c)
    mandelbrot = np.full(c.shape, max_iter, dtype=int)
    
    for i in range(max_iter):
        mask = np.abs(z) <= 2
        z[mask] = z[mask] * z[mask] + c[mask]
        mandelbrot[mask] = i
    
    return mandelbrot

# Funkce pro vykreslení Mandelbrotovy množiny
def draw_mandelbrot():
    xmin = offset_x - screen_width / (2 * zoom)
    xmax = offset_x + screen_width / (2 * zoom)
    ymin = offset_y - screen_height / (2 * zoom)
    ymax = offset_y + screen_height / (2 * zoom)
    
    mandelbrot = mandelbrot_set(xmin, xmax, ymin, ymax, screen_width, screen_height, max_iter)
    
    # Normalizujeme výsledky pro barvy a převod na RGB
    mandelbrot_norm = (mandelbrot % 256).astype(np.uint8)
    colors = np.dstack((mandelbrot_norm % 8 * 32, mandelbrot_norm % 16 * 16, mandelbrot_norm % 32 * 8))
    
    # Vykreslení obrazovky pomocí surfarray
    pygame.surfarray.blit_array(screen, colors)

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

        # Posun kurzorem myši při zoomu
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:  # Držení levého tlačítka myši pro posun
                mouse_x, mouse_y = pygame.mouse.get_pos()
                offset_x += (mouse_x - screen_width / 2) / zoom
                offset_y += (mouse_y - screen_height / 2) / zoom

pygame.quit()
