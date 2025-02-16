import tkinter as tk
from tkinter import messagebox
import math

def on_click(button_text):
    if button_text == "C":
        entry_var.set("")
    elif button_text == "=":
        try:
            expression = entry_var.get()
            entry_var.set(eval(expression))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
    else:
        entry_var.set(entry_var.get() + button_text)

def scientific_function(func):
    try:
        expression = entry_var.get()
        if func in ['sin', 'cos', 'tan', 'log', 'sqrt', 'exp']:
            result = eval(f"math.{func}({expression})")
        elif func == "factorial":
            result = math.factorial(int(expression))
        entry_var.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

root = tk.Tk()
root.title("Scientific Calculator")

tk.Label(root, text="Scientific Calculator", font=("Arial", 16)).pack()
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 14), justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=10, pady=10)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
    ('sin', 'cos', 'tan', 'log'),
    ('sqrt', 'exp', 'factorial', 'C')
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH)
    for btn in row:
        action = lambda x=btn: scientific_function(x) if x in ['sin', 'cos', 'tan', 'log', 'sqrt', 'exp', 'factorial'] else on_click(x)
        tk.Button(frame, text=btn, font=("Arial", 14), command=action, width=6, height=2).pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

root.mainloop()
