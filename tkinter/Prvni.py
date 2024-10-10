import tkinter as tk
from tkinter import messagebox

def odeslat():
    jmeno = entry_jmeno.get()
    email = entry_email.get()
    messagebox.showinfo("Odesláno", f"Jméno: {jmeno}\nE-mail: {email}")

# Vytvoření hlavního okna
okno = tk.Tk()
okno.title("Jednoduchý formulář")

# Vytvoření štítků a vstupních polí
label_jmeno = tk.Label(okno, text="Jméno:")
label_jmeno.pack()

entry_jmeno = tk.Entry(okno)
entry_jmeno.pack()

label_email = tk.Label(okno, text="E-mail:")
label_email.pack()

entry_email = tk.Entry(okno)
entry_email.pack()

# Tlačítko pro odeslání
button_odeslat = tk.Button(okno, text="Odeslat", command=odeslat)
button_odeslat.pack()

# Spuštění hlavní smyčky
okno.mainloop()
