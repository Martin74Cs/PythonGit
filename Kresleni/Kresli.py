# import graphics
# import math as m
from graphics import *
import random
import Metody as Met

print("Start")
# win:any

# def Obrazek():
    # Obrazek neexistuje
    # img = Image(Point(250,250)"Jablko.gir")
    # img.draw(win)

def Texty(Popis): 
    txt = Text(Point(250,250), Popis)
    txt.setTextColor(color_rgb(0,255,200))
    txt.setSize(30)
    txt.setFace("courier")
    txt.draw(win)
    return txt


def Okno():
    win = GraphWin("Kateřina", 500, 500 )
    win.setBackground(color_rgb(0,0,0))
    # Nastaví souřadnicový systém okna.
    win.setCoords(0,0,500,500)
    # win = GraphWin("Update Example", 320, 200, autoflush=False)
    # for i in range(255):
    # # <drawing commands for ith frame>
    #     win.setBackground(color_rgb(i,i,0))
    #     update(30)    
    # win = GraphWin("My Animation", 400, 400, autoflush=False)
    return win
    # win.checkMouse(200,200)
    
    # Ukoncemi okna
    # win.close()

def Klavesa():
    key = win.checkKey()
    return key

win = Okno()
txt = Texty("Kateřina je zrzka.")
Bod = win.getMouse()
txt.move(Bod.getX(),Bod.getY())
# win.getMouse()
# txt.undraw()

win.plot(35,128,"blue")
while (win.getKey() == "k"):
    Bod = win.getMouse()
    Texty(Bod)
    clickPoint = win.checkMouse()
    Texty(clickPoint )

keyString = win.getKey()
keyString = win.checkKey()
Texty("Bod " + Bod.x , ",  " + Bod.y )
# pauza na kliknutí myši
win.getMouse()
# win.close()