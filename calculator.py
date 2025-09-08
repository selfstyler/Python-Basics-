import tkinter as tk

# App window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry widget for display
expression = ""
entry_text = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_text, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(expand=True, fill="both")

# Function to update expression
def press(num):
    global expression
    expression += str(num)
    entry_text.set(expression)

# Function to evaluate expression
def equalpress():
    try:
        global expression
        result = str(eval(expression))
        entry_text.set(result)
        expression = result
    except:
        entry_text.set("Error")
        expression = ""

# Function to clear entry
def clear():
    global expression
    expression = ""
    entry_text.set("")

# Buttons layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for char in row:
        if char == "=":
            btn = tk.Button(frame, text=char, font=("Arial", 18), command=equalpress)
        elif char == "C":
            btn = tk.Button(frame, text=char, font=("Arial", 18), command=clear)
        else:
            btn = tk.Button(frame, text=char, font=("Arial", 18), command=lambda ch=char: press(ch))
        btn.pack(side="left", expand=True, fill="both")

root.mainloop()
