import os
import math
import sympy as s

os.system("cls")
# Jmeno adresaře
cesta = os.path.dirname(__file__)
print(cesta)
soubor = cesta + "\\Soubor" 
print(soubor)

a = s.solve(5+3)
print (a)

if not os.path.exists(soubor):
    os.mkdir(soubor)
cesta = soubor +"\\kamen.csv"
print(cesta)
g = 10
t = 0.0
dt = 0.1
l = 10.0
cas = 5.0
h = 1/2 * g * math.pow(cas,2) 
# vy = math.pow(h*g, 1/2)
vy = h  / cas
vx = l / cas

print('rychlost={:f}'.format(vy), ' vyska={:f}'.format(h))

a =  open(cesta,"w")
while (t <= cas + dt):
    x = vx * t
    y = vy * t - (1/2 * g * t * t)

    text = '{:0.2f};'.format(t), '{:f};'.format(x), '{:f};'.format(y), '{:f};'.format(vx),'{:f}'.format(vy)
    a.writelines(text)    
    print(text)
    t = t +  dt

a.close

print("Funguje")
