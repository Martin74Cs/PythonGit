import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Rozměry mřížky
grid_size = 50

# Inicializace mřížky s náhodným stavem (1 = živá buňka, 0 = mrtvá buňka)
grid = np.random.choice([0, 1], size=(grid_size, grid_size))

# Funkce pro aktualizaci mřížky podle pravidel Hry života
def update(frameNum, img, grid):
    new_grid = grid.copy()
    
    for i in range(grid_size):
        for j in range(grid_size):
            # Počet živých sousedů
            total = (grid[i, (j-1)%grid_size] + grid[i, (j+1)%grid_size] +
                     grid[(i-1)%grid_size, j] + grid[(i+1)%grid_size, j] +
                     grid[(i-1)%grid_size, (j-1)%grid_size] + grid[(i-1)%grid_size, (j+1)%grid_size] +
                     grid[(i+1)%grid_size, (j-1)%grid_size] + grid[(i+1)%grid_size, (j+1)%grid_size])
            
            # Pravidla Hry života
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = 0  # Buňka umírá
            else:
                if total == 3:
                    new_grid[i, j] = 1  # Buňka ožije
    
    # Aktualizace mřížky
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,

# Nastavení grafiky
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='binary')

# Animace
ani = animation.FuncAnimation(fig, update, fargs=(img, grid), frames=10, interval=200, save_count=50)

# Zobrazení animace
plt.show()
