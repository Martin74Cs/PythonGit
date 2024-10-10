# app/script.py
import pygame
import random

# Inicializace Pygame
pygame.init()

# Nastavení obrazovky
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animované obrazce")

# Barva
color = (0, 150, 255, 128)

# Třída pro obrazce
class Shape:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.radius = random.randint(10, 30)
        self.dx = random.uniform(-2, 2)
        self.dy = random.uniform(-2, 2)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.radius += random.uniform(-0.5, 0.5)
        if self.radius < 5:
            self.radius = 5

    def draw(self, screen):
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), int(self.radius))

shapes = []

# Hlavní smyčka
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if random.random() < 0.1:  # Přidání nového obrazce
        shapes.append(Shape())

    screen.fill((255, 255, 255))  # Vyčištění obrazovky
    for shape in shapes:
        shape.update()
        shape.draw(screen)

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()