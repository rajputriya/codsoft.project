import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

app = tk.Tk()
app.title("To-Do List App")

label = tk.Label(app, text="Enter Task:")
label.pack()

entry = tk.Entry(app)
entry.pack()

add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack()

delete_button = tk.Button(app, text="Delete Task", command=delete_task)
delete_button.pack()

listbox = tk.Listbox(app)
listbox.pack()

app.mainloop()
