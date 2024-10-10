import tkinter as tk
from tkinter import messagebox
import json

# Globální proměnné
data_list = []
current_index = 0

# Funkce pro uložení dat do JSON souboru
def save_data():
    global data_list
    data = {
        "name": entry_name.get(),
        "age": entry_age.get()
    }
    data_list.append(data)
    with open("data.json", "w") as json_file:
        json.dump(data_list, json_file)
        print("Data saved successfully!")
        # messagebox.showinfo("Info", "Data saved successfully!")

# Funkce pro načtení dat z JSON souboru
def load_data():
    global data_list, current_index
    try:
        with open("data.json", "r") as json_file:
            data_list = json.load(json_file)
            if data_list:
                current_index = 0
                display_data(current_index)
    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found!")


# Funkce pro zobrazení dat
def display_data(index):
    entry_name.delete(0, tk.END)
    entry_name.insert(0, data_list[index]["name"])
    entry_age.delete(0, tk.END)
    entry_age.insert(0, data_list[index]["age"])

# Funkce pro procházení záznamů
def next_record():
    global current_index
    if current_index < len(data_list) - 1:
        current_index += 1
        display_data(current_index)

def previous_record():
    global current_index
    if current_index > 0:
        current_index -= 1
        display_data(current_index)

# Funkce pro změnu dat
def update_data():
    global data_list, current_index
    if data_list:
        data_list[current_index]["name"] = entry_name.get()
        data_list[current_index]["age"] = entry_age.get()
        with open("data.json", "w") as json_file:
            json.dump(data_list, json_file)
        print("Data updated successfully!")
        # messagebox.showinfo("Info", "Data updated successfully!")
    else:
        messagebox.showerror("Error", "No data to update!")


# Vytvoření hlavního okna
root = tk.Tk()
root.title("Data Entry")

# Vytvoření a umístění widgetů
tk.Label(root, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Age:").grid(row=1, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1)

tk.Button(root, text="Save Data", command=save_data).grid(row=2, column=0)
tk.Button(root, text="Load Data", command=load_data).grid(row=2, column=1)
tk.Button(root, text="Previous", command=previous_record).grid(row=3, column=0)
tk.Button(root, text="Next", command=next_record).grid(row=3, column=1)

# Přidání tlačítka pro aktualizaci dat
tk.Button(root, text="Update Data", command=update_data).grid(row=4, column=0, columnspan=2)

# Spuštění hlavní smyčky
root.mainloop()
