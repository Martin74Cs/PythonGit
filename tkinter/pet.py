import tkinter as tk

def celsius_to_fahrenheit():
    celsius = float(entry_celsius.get())
    fahrenheit = (celsius * 9/5) + 32
    label_result.config(text=f"{fahrenheit:.2f} °F")

def fahrenheit_to_celsius():
    fahrenheit = float(entry_fahrenheit.get())
    celsius = (fahrenheit - 32) * 5/9
    label_result.config(text=f"{celsius:.2f} °C")

root = tk.Tk()
root.title("Temperature Converter")

tk.Label(root, text="Celsius:").grid(row=0, column=0)
entry_celsius = tk.Entry(root)
entry_celsius.grid(row=0, column=1)
tk.Button(root, text="Convert to Fahrenheit", command=celsius_to_fahrenheit).grid(row=0, column=2)

tk.Label(root, text="Fahrenheit:").grid(row=1, column=0)
entry_fahrenheit = tk.Entry(root)
entry_fahrenheit.grid(row=1, column=1)
tk.Button(root, text="Convert to Celsius", command=fahrenheit_to_celsius).grid(row=1, column=2)

label_result = tk.Label(root, text="Result")
label_result.grid(row=2, column=0, columnspan=3)

root.mainloop()