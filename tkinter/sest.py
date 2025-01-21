import tkinter as tk
import tkinter.font as font
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task.")

root = tk.Tk()
root.title("To-Do List")

# Vytvoření fontu s nastavenou velikostí
# marfont = font.Font(family='Helvetica', size=14, weight='bold')
marfont = font.Font(family='Arial', size=14)

frame = tk.Frame(root)
frame.pack()

listbox = tk.Listbox(frame, height=10, width=50, font=marfont)
listbox.pack(side=tk.LEFT)

# Jedá se o  posuvník
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Vstupní pole
entry_task = tk.Entry(root, width=50, font=marfont)
entry_task.pack()

buttonAdd = tk.Button(root, text="Add task", width=48, command=add_task, 
    font=marfont, bg='green', fg='white', activebackground='yellow', activeforeground='yellow', relief='flat', borderwidth=0)
buttonAdd.pack()

buttonDelete = tk.Button(root, text="Delete task", width=48, command=delete_task, 
font=marfont, bg='red', fg='white')
buttonDelete.pack()

root.mainloop()