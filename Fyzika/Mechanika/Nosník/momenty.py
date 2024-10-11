import numpy as np
import matplotlib.pyplot as plt

# Definování konstant
q = 80917.44589226524  # intenzita spojitého zatížení (N/m)
Delka = 20  # celková délka nosníku (m)
a = 2.5   # vzdálenost první podpěry od levého konce (m)
c = 2.5   # vzdálenost druhé podpěry od levého konce (m)

# Výpočet reakcí
# Ra = q * L - q * (L - a) * L / (2 * (L - b))
#  Rb =         q * (L - a) * L / (2 * (L - b))
b = Delka - a - c
#Ra = q * (a + c -b)/2
#Rb = q * (b + c -a)/2
Rb = q /(2 * b) * (( b + c )**2 - a**2)
Ra = q * Delka - Rb
print("Ra=", Ra, " Rb=",Rb)

# Funkce pro výpočet momentů
def moment_0_a(x):
    return - q * x**2 / 2
 #  return - (q / 2 * x**2 )

def moment_a_b(x):
    return  - q / 2 * x**2 + Ra * (x-a)
#    return  q / 2 * x**2

def moment_b_L(x):
    return - q/2 * x**2 + Ra * (x-a)  + Rb * (x-a-b) 
 #  return Rb * (L - x) - q / 2 * (L - x)**2 

# Diskretizace délky nosníku
x1 = np.linspace(0, a, 100)
x2 = np.linspace(a, Delka - c, 100)
x3 = np.linspace(Delka - c, Delka, 100)

# Výpočty momentů
M1 = moment_0_a(x1)
M2 = moment_a_b(x2)
M3 = moment_b_L(x3)

# Vykreslení průběhu momentů
plt.figure(figsize=(10, 6))
plt.plot(x1, M1, label=f'Úsek 0 až {a} m')
plt.plot(x2, M2, label=f'Úsek {a} až {a + b} m')
plt.plot(x3, M3, label=f'Úsek {a + c } až {Delka} m')

plt.title('Průběh ohybového momentu podél nosníku')
plt.xlabel('Délka nosníku [m]')
plt.ylabel('Ohybový moment [Nm]')
plt.axhline(0, color='black',linewidth=0.5)
plt.legend()
plt.grid(True)

plt.show()