import tkinter as tk
import random

# Choices
choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

# Determine winner
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer Choice: {computer_choice}")

    if user_choice == computer_choice:
        result_label.config(text="Result: It's a Tie!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Scissors" and computer_choice == "Paper") or
        (user_choice == "Paper" and computer_choice == "Rock")
    ):
        result_label.config(text="Result: You Win!")
        user_score += 1
    else:
        result_label.config(text="Result: You Lose!")
        computer_score += 1

    score_label.config(
        text=f"Score  |  You: {user_score}  Computer: {computer_score}"
    )

# Create window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("500x420")
window.configure(bg="black")
window.resizable(False, False)

# Title
title_label = tk.Label(
    window,
    text="Rock Paper Scissors Game",
    font=("Arial", 18, "bold"),
    bg="black",
    fg="white"
)
title_label.pack(pady=15)

# Instructions
instruction_label = tk.Label(
    window,
    text="Choose Rock, Paper, or Scissors",
    bg="black",
    fg="white"
)
instruction_label.pack()

# Buttons frame
button_frame = tk.Frame(window, bg="black")
button_frame.pack(pady=15)

rock_btn = tk.Button(
    button_frame,
    text="Rock",
    width=10,
    bg="#333333",
    fg="white",
    command=lambda: play("Rock")
)
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(
    button_frame,
    text="Paper",
    width=10,
    bg="#333333",
    fg="white",
    command=lambda: play("Paper")
)
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(
    button_frame,
    text="Scissors",
    width=10,
    bg="#333333",
    fg="white",
    command=lambda: play("Scissors")
)
scissors_btn.grid(row=0, column=2, padx=10)

# Display choices
user_choice_label = tk.Label(
    window,
    text="Your Choice: ",
    bg="black",
    fg="white"
)
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(
    window,
    text="Computer Choice: ",
    bg="black",
    fg="white"
)
computer_choice_label.pack(pady=5)

# Result
result_label = tk.Label(
    window,
    text="Result: ",
    font=("Arial", 14, "bold"),
    bg="black",
    fg="white"
)
result_label.pack(pady=10)

# Score
score_label = tk.Label(
    window,
    text="Score  |  You: 0  Computer: 0",
    font=("Arial", 12),
    bg="black",
    fg="white"
)
score_label.pack(pady=10)

# Run window
window.mainloop()
