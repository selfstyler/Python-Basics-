import tkinter as tk
import random

# Initialize main window
root = tk.Tk()
root.title("ROCK_PAPER_SCISSOR")
root.geometry("350x450")
root.resizable(False, False)

# Entry (Display) — Not used for input now, but will display result
entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, font=("Arial", 16), bd=4, relief=tk.RIDGE, justify="center")
entry.pack(pady=30, fill="both", padx=20)

# Choices for computer
item_list = ["Rock", "Paper", "Scissor"]

# Function to play the game
def play_game(user_choice):
    comp_choice = random.choice(item_list)

    result = f"User: {user_choice}\nComputer: {comp_choice}\n"

    if user_choice == comp_choice:
        result += "\nResult: TIE"
    elif user_choice == "Rock":
        if comp_choice == "Paper":
            result += "\nResult: YOU LOSE"
        else:
            result += "\nResult: YOU WIN"
    elif user_choice == "Paper":
        if comp_choice == "Rock":
            result += "\nResult: YOU WIN"
        else:
            result += "\nResult: YOU LOSE"
    elif user_choice == "Scissor":
        if comp_choice == "Paper":
            result += "\nResult: YOU WIN"
        else:
            result += "\nResult: YOU LOSE"
    else:
        result = "\nInvalid Choice"

    entry_text.set(result)

# Buttons for user input
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", font=("Arial", 14), width=10, command=lambda: play_game("Rock"))
paper_btn = tk.Button(button_frame, text="Paper", font=("Arial", 14), width=10, command=lambda: play_game("Paper"))
scissor_btn = tk.Button(button_frame, text="Scissor", font=("Arial", 14), width=10, command=lambda: play_game("Scissor"))

rock_btn.grid(row=0, column=0, padx=5, pady=5)
paper_btn.grid(row=0, column=1, padx=5, pady=5)
scissor_btn.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Exit button

exit_btn = tk.Button(root, text="Exit", font=("Arial", 12), command=root.destroy)
exit_btn.pack(pady=10)

# Run the app
root.mainloop()
