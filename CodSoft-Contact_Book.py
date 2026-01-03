import tkinter as tk
from tkinter import messagebox

contacts = []

# Add contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone are required")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    clear_fields()
    refresh_list()
    messagebox.showinfo("Success", "Contact added successfully")

# View contacts
def refresh_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Search contact
def search_contact():
    query = search_entry.get().lower()
    contact_list.delete(0, tk.END)

    for contact in contacts:
        if query in contact["name"].lower() or query in contact["phone"]:
            contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Select contact
def select_contact(event):
    try:
        index = contact_list.curselection()[0]
        contact = contacts[index]

        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)

        name_entry.insert(0, contact["name"])
        phone_entry.insert(0, contact["phone"])
        email_entry.insert(0, contact["email"])
        address_entry.insert(0, contact["address"])
    except:
        pass

# Update contact
def update_contact():
    try:
        index = contact_list.curselection()[0]
        contacts[index]["name"] = name_entry.get()
        contacts[index]["phone"] = phone_entry.get()
        contacts[index]["email"] = email_entry.get()
        contacts[index]["address"] = address_entry.get()

        refresh_list()
        clear_fields()
        messagebox.showinfo("Success", "Contact updated successfully")
    except:
        messagebox.showerror("Error", "Please select a contact to update")

# Delete contact
def delete_contact():
    try:
        index = contact_list.curselection()[0]
        contacts.pop(index)
        refresh_list()
        clear_fields()
        messagebox.showinfo("Success", "Contact deleted successfully")
    except:
        messagebox.showerror("Error", "Please select a contact to delete")

# Clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Create window
window = tk.Tk()
window.title("Contact Book")
window.geometry("650x450")
window.configure(bg="black")
window.resizable(False, False)

# Title
title = tk.Label(
    window,
    text="Contact Book",
    font=("Arial", 18, "bold"),
    bg="black",
    fg="white"
)
title.pack(pady=10)

# Input frame
input_frame = tk.Frame(window, bg="black")
input_frame.pack()

def label(text):
    return tk.Label(input_frame, text=text, bg="black", fg="white")

label("Name").grid(row=0, column=0, sticky="w")
label("Phone").grid(row=1, column=0, sticky="w")
label("Email").grid(row=2, column=0, sticky="w")
label("Address").grid(row=3, column=0, sticky="w")

name_entry = tk.Entry(input_frame, width=30, bg="#222", fg="white", insertbackground="white")
phone_entry = tk.Entry(input_frame, width=30, bg="#222", fg="white", insertbackground="white")
email_entry = tk.Entry(input_frame, width=30, bg="#222", fg="white", insertbackground="white")
address_entry = tk.Entry(input_frame, width=30, bg="#222", fg="white", insertbackground="white")

name_entry.grid(row=0, column=1, pady=3)
phone_entry.grid(row=1, column=1, pady=3)
email_entry.grid(row=2, column=1, pady=3)
address_entry.grid(row=3, column=1, pady=3)

# Buttons
button_frame = tk.Frame(window, bg="black")
button_frame.pack(pady=10)

btn_style = {"bg": "#333", "fg": "white", "width": 12}

tk.Button(button_frame, text="Add", command=add_contact, **btn_style).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Update", command=update_contact, **btn_style).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete", command=delete_contact, **btn_style).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Clear", command=clear_fields, **btn_style).grid(row=0, column=3, padx=5)

# Search
search_frame = tk.Frame(window, bg="black")
search_frame.pack(pady=5)

tk.Label(search_frame, text="Search (Name or Phone):", bg="black", fg="white").pack(side="left")
search_entry = tk.Entry(search_frame, bg="#222", fg="white", insertbackground="white")
search_entry.pack(side="left", padx=5)
tk.Button(search_frame, text="Search", command=search_contact, bg="#444", fg="white").pack(side="left")

# Contact list
contact_list = tk.Listbox(window, width=70, height=10, bg="#111", fg="white")
contact_list.pack(pady=10)
contact_list.bind("<<ListboxSelect>>", select_contact)

# Run app
window.mainloop()
