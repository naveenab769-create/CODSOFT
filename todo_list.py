import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("380x450")
root.resizable(False, False)

# ---------- THEMES ----------
dark_theme = {
    "bg": "#1e1e1e",
    "fg": "white",
    "entry": "#2d2d2d",
    "button": "#3a3a3a"
}

light_theme = {
    "bg": "#f4f4f4",
    "fg": "black",
    "entry": "white",
    "button": "#dddddd"
}

current_theme = dark_theme

# ---------- FUNCTIONS ----------
def apply_theme():
    root.configure(bg=current_theme["bg"])
    title.config(bg=current_theme["bg"], fg=current_theme["fg"])
    entry.config(bg=current_theme["entry"], fg=current_theme["fg"])
    listbox.config(bg=current_theme["entry"], fg=current_theme["fg"])
    frame.config(bg=current_theme["bg"])
    theme_btn.config(bg=current_theme["button"], fg=current_theme["fg"])

    for btn in buttons:
        btn.config(bg=current_theme["button"], fg=current_theme["fg"])

def toggle_theme():
    global current_theme
    current_theme = light_theme if current_theme == dark_theme else dark_theme
    apply_theme()

def add_task():
    task = entry.get().strip()
    if task == "":
        return
    listbox.insert(tk.END, task)
    entry.delete(0, tk.END)

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Select a task")

def update_task():
    try:
        index = listbox.curselection()[0]
        new_task = entry.get().strip()
        if new_task == "":
            return
        listbox.delete(index)
        listbox.insert(index, new_task)
        entry.delete(0, tk.END)
    except:
        messagebox.showwarning("Warning", "Select a task to update")

def mark_done():
    try:
        index = listbox.curselection()[0]
        task = listbox.get(index)
        if not task.startswith("✔"):
            listbox.delete(index)
            listbox.insert(index, "✔ " + task)
    except:
        messagebox.showwarning("Warning", "Select a task")

# ---------- UI ----------
title = tk.Label(root, text="To-Do List", font=("Segoe UI", 18, "bold"))
title.pack(pady=10)

entry = tk.Entry(root, font=("Segoe UI", 12))
entry.pack(pady=8, ipadx=10, ipady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

add_btn = tk.Button(frame, text="Add", width=9, command=add_task)
update_btn = tk.Button(frame, text="Update", width=9, command=update_task)
done_btn = tk.Button(frame, text="Done", width=9, command=mark_done)
delete_btn = tk.Button(frame, text="Delete", width=9, command=delete_task)

add_btn.grid(row=0, column=0, padx=4, pady=4)
update_btn.grid(row=0, column=1, padx=4, pady=4)
done_btn.grid(row=1, column=0, padx=4, pady=4)
delete_btn.grid(row=1, column=1, padx=4, pady=4)

buttons = [add_btn, update_btn, done_btn, delete_btn]

listbox = tk.Listbox(root, font=("Segoe UI", 12), height=10, width=32)
listbox.pack(pady=10)

theme_btn = tk.Button(root, text="Toggle Theme", command=toggle_theme)
theme_btn.pack(pady=10)

apply_theme()
root.mainloop()