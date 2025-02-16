import tkinter as tk
from tkinter import ttk

def convert():
    try:
        value = float(entry.get())
        unit_from = from_var.get()
        unit_to = to_var.get()
        
        base_units = {
            "Kilometers": 1000, "Meters": 1, "Centimeters": 0.01, "Miles": 1609.34, "Yards": 0.9144, "Feet": 0.3048, "Inches": 0.0254,
            "Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495,
            "Celsius": (lambda c: c + 273.15), "Fahrenheit": (lambda f: (f - 32) * 5/9 + 273.15), "Kelvin": (lambda k: k)
        }
        
        if unit_from in ["Celsius", "Fahrenheit", "Kelvin"] and unit_to in ["Celsius", "Fahrenheit", "Kelvin"]:
            kelvin = base_units[unit_from](value)
            result.set(round(base_units[unit_to](kelvin) if callable(base_units[unit_to]) else kelvin, 4))
        elif unit_from in base_units and unit_to in base_units:
            result.set(round(value * (base_units[unit_to] / base_units[unit_from]), 4))
        else:
            result.set("Invalid Conversion")
    except ValueError:
        result.set("Invalid Input")

root = tk.Tk()
root.title("Universal Unit Converter")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

ttk.Label(root, text="Universal Unit Converter", font=("Arial", 16, "bold"), background="#f0f0f0").pack(pady=10)

ttk.Label(root, text="Enter Value:", font=("Arial", 12)).pack()
entry = ttk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

from_var = tk.StringVar(value="Kilometers")
to_var = tk.StringVar(value="Meters")
options = ["Kilometers", "Meters", "Centimeters", "Miles", "Yards", "Feet", "Inches", "Kilograms", "Grams", "Pounds", "Ounces", "Celsius", "Fahrenheit", "Kelvin"]

ttk.Label(root, text="From:", font=("Arial", 12)).pack()
from_menu = ttk.Combobox(root, textvariable=from_var, values=options, font=("Arial", 12), state="readonly")
from_menu.pack(pady=5)

ttk.Label(root, text="To:", font=("Arial", 12)).pack()
to_menu = ttk.Combobox(root, textvariable=to_var, values=options, font=("Arial", 12), state="readonly")
to_menu.pack(pady=5)

result = tk.StringVar()
result_label = ttk.Label(root, textvariable=result, font=("Arial", 14, "bold"), background="#f0f0f0")
result_label.pack(pady=10)

ttk.Button(root, text="Convert", command=convert).pack(pady=10)

root.mainloop()
