# Přehled jednoduché výuky
# https://docs.google.com/document/d/1uwEvRE8xjPdasdNNhQwzN-ErkgUvWrSq/edit?pli=1

from turtle import Turtle, Screen
import random

my_tuple = [1, 5, 8]
my_tuple = (100, 5, 8)

# Vyhodí chybu
# my_tuple[0] = 12

# Tuple změníme na list
tuple_to_list = list(my_tuple)
print(tuple_to_list)
tuple_to_list[0] = 12
print(tuple_to_list)

print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])

colors = ["violet", "yellow", "red", "green", "blue", "pink"]

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def randomColor1():
    r = random.random()
    g = random.random()
    b = random.random()
    tup = (r, g, b)
    return tup

Had = Turtle()
# 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'.
Had.shape("classic")

for i in range(0,255):
    # Had.pendown()
    Had.forward(100)
    # Had.penup()
    Had.pensize(i)
    # tup = (0.2, 0.8, 0.55)
    # Had.pencolor(tup)
    # Had.pencolor(randomColor())
    print(randomColor1())
    Had.pencolor(randomColor1())
    Had.right(100)

# Obraz = Screen()
# print(f"sirka:  {Obraz.canvheight}")
# print(f"sirka:  {Obraz.canvwidth}")

# Obraz.title("Had")

# Obraz.colormode(456521)


# Obraz.exitonclick()