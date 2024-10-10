import tkinter as tk
import tkinter.font as font
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task.")

root = tk.Tk()
root.title("To-Do List")

# Vytvoření fontu s nastavenou velikostí
# marfont = font.Font(family='Helvetica', size=14, weight='bold')
marfont = font.Font(family='Arial', size=14)

frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack()

button_add_task = tk.Button(root, text="Add task", width=48, command=add_task, 
    font=marfont, bg='green', fg='white', activebackground='yellow', activeforeground='yellow', relief='flat', borderwidth=0)
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete task", width=48, command=delete_task, 
font=marfont, bg='red', fg='white')
button_delete_task.pack()

root.mainloop()