import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Create window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x260")
window.resizable(False, False)
window.configure(bg="black")

# Heading
title_label = tk.Label(
    window,
    text="Password Generator",
    font=("Arial", 16, "bold"),
    bg="black",
    fg="white"
)
title_label.pack(pady=15)

# Length label
length_label = tk.Label(
    window,
    text="Enter Password Length",
    bg="black",
    fg="white"
)
length_label.pack()

# Length entry
length_entry = tk.Entry(
    window,
    width=25,
    bg="#222222",
    fg="white",
    insertbackground="white"
)
length_entry.pack(pady=5)

# Generate button
generate_button = tk.Button(
    window,
    text="Generate Password",
    command=generate_password,
    bg="#444444",
    fg="white",
    activebackground="#666666",
    activeforeground="white"
)
generate_button.pack(pady=12)

# Password label
password_label = tk.Label(
    window,
    text="Generated Password",
    bg="black",
    fg="white"
)
password_label.pack()

# Password display
password_entry = tk.Entry(
    window,
    width=35,
    bg="#222222",
    fg="white",
    insertbackground="white"
)
password_entry.pack(pady=5)

# Run app
window.mainloop()
