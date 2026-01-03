import tkinter as tk

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.resizable(False, False)
root.configure(bg="black")

# Entry box
expression = ""

def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# StringVar for display
input_text = tk.StringVar()

entry = tk.Entry(
    root,
    textvariable=input_text,
    font=("Arial", 24),
    bd=10,
    insertwidth=2,
    width=14,
    borderwidth=4,
    bg="black",
    fg="white",
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, pady=20)

# Button style
btn_bg = "#1e1e1e"
btn_fg = "white"

def create_button(text, row, col, cmd):
    return tk.Button(
        root,
        text=text,
        padx=20,
        pady=20,
        font=("Arial", 14),
        bg=btn_bg,
        fg=btn_fg,
        command=cmd
    ).grid(row=row, column=col, padx=5, pady=5)

# Buttons
create_button("7", 1, 0, lambda: press(7))
create_button("8", 1, 1, lambda: press(8))
create_button("9", 1, 2, lambda: press(9))
create_button("/", 1, 3, lambda: press("/"))

create_button("4", 2, 0, lambda: press(4))
create_button("5", 2, 1, lambda: press(5))
create_button("6", 2, 2, lambda: press(6))
create_button("*", 2, 3, lambda: press("*"))

create_button("1", 3, 0, lambda: press(1))
create_button("2", 3, 1, lambda: press(2))
create_button("3", 3, 2, lambda: press(3))
create_button("-", 3, 3, lambda: press("-"))

create_button("0", 4, 0, lambda: press(0))
create_button(".", 4, 1, lambda: press("."))
create_button("=", 4, 2, equal)
create_button("+", 4, 3, lambda: press("+"))

create_button("C", 5, 0, clear)

root.mainloop()
