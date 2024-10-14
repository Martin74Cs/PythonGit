import numpy as np
import matplotlib.pyplot as plt

# Výchozí parametry Mandelbrotovy množiny
max_iter = 256
zoom = 1.0
offset_x = -0.5  # Počáteční posun na x ose
offset_y = 0.0   # Počáteční posun na y ose
width, height = 800, 600  # Rozměry obrázku

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

# Funkce pro vykreslení s interakcí
def interactive_mandelbrot():
    zoom = 1.0
    offset_x = -0.5
    offset_y = 0.0

    fig, ax = plt.subplots()

    def update_plot(event):
        nonlocal zoom, offset_x, offset_y

        # Zvětšení nebo zmenšení při otáčení kolečkem myši
        if event.button == 'up':
            zoom *= 1.5
        elif event.button == 'down':
            zoom /= 1.5
        
        # Přepočet offsetu na základě pozice kurzoru
        offset_x = (offset_x + (event.xdata - offset_x) / zoom)
        offset_y = (offset_y + (event.ydata - offset_y) / zoom)
        
        ax.clear()  # Vymazat starý obraz
        mandelbrot = mandelbrot_set(offset_x - 2.0 / zoom, offset_x + 2.0 / zoom,
                                    offset_y - 1.5 / zoom, offset_y + 1.5 / zoom,
                                    width, height, max_iter)
        ax.imshow(mandelbrot, extent=(offset_x - 2.0 / zoom, offset_x + 2.0 / zoom,
                                      offset_y - 1.5 / zoom, offset_y + 1.5 / zoom),
                  cmap="twilight_shifted")
        plt.draw()

    # Vykreslení s interakcí
    mandelbrot = mandelbrot_set(offset_x - 2.0 / zoom, offset_x + 2.0 / zoom,
                                offset_y - 1.5 / zoom, offset_y + 1.5 / zoom,
                                width, height, max_iter)
    ax.imshow(mandelbrot, extent=(offset_x - 2.0 / zoom, offset_x + 2.0 / zoom,
                                  offset_y - 1.5 / zoom, offset_y + 1.5 / zoom),
              cmap="twilight_shifted")
    
    fig.canvas.mpl_connect('scroll_event', update_plot)  # Propojíme zoomování s eventem
    plt.show()

# Spuštění interaktivního režimu
interactive_mandelbrot()