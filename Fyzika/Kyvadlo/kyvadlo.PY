import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def simulace_tlumeneho_kyvadla(delka, gravitace, pocatecni_uhel, cas_simulace, krok_casu, koeficient_tlumeni):
    # Výpočet periody kyvadla
    T = 2 * math.pi * math.sqrt(delka / gravitace)
    
    # Inicializace seznamů pro ukládání dat
    cas = []
    uhel = []
    
    # Simulace pohybu kyvadla
    t = 0
    while t <= cas_simulace:
        omega = math.sqrt(gravitace / delka)
        theta = pocatecni_uhel * math.exp(-koeficient_tlumeni * t) * math.cos(omega * t)
        
        cas.append(t)
        uhel.append(theta)
        
        t += krok_casu
    
    return cas, uhel, T

# Parametry kyvadla
delka = 1.0  # délka provazu v metrech
gravitace = 9.81  # gravitační zrychlení v m/s^2
pocatecni_uhel = math.radians(30)  # počáteční úhel ve stupních, převedený na radiány
cas_simulace = 20  # celkový čas simulace v sekundách
krok_casu = 0.05  # časový krok simulace v sekundách
koeficient_tlumeni = 0.1  # koeficient tlumení (čím vyšší, tím rychlejší útlum)

# Provedení simulace
cas, uhel, perioda = simulace_tlumeneho_kyvadla(delka, gravitace, pocatecni_uhel, cas_simulace, krok_casu, koeficient_tlumeni)

# Vytvoření grafu a animace
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))
fig.suptitle('Tlumené kyvadlo')

# Graf průběhu kmitů
line, = ax1.plot([], [], lw=2)
ax1.set_xlim(0, cas_simulace)
ax1.set_ylim(min(uhel), max(uhel))
ax1.set_xlabel('Čas (s)')
ax1.set_ylabel('Úhel (rad)')
ax1.grid()

# Animace kyvadla
pendulum, = ax2.plot([], [], 'o-', lw=2)
ax2.set_xlim(-1.2*delka, 1.2*delka)
ax2.set_ylim(-1.2*delka, 0.2*delka)
ax2.set_aspect('equal', adjustable='box')
ax2.grid()

# Informace o kyvadlu
info = f'Délka provazu: {delka} m\nPočáteční úhel: {math.degrees(pocatecni_uhel):.1f}°\nPerioda: {perioda:.2f} s\nKoeficient tlumení: {koeficient_tlumeni}'
ax2.text(0.05, 0.95, info, transform=ax2.transAxes, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))

def init():
    line.set_data([], [])
    pendulum.set_data([], [])
    return line, pendulum

def animate(i):
    line.set_data(cas[:i], uhel[:i])
    x = delka * math.sin(uhel[i])
    y = -delka * math.cos(uhel[i])
    pendulum.set_data([0, x], [0, y])
    return line, pendulum

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(cas), interval=50, blit=True)

plt.show()

print(f"Perioda kyvadla: {perioda:.2f} sekund")
