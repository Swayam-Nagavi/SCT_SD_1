import tkinter as tk
from tkinter import ttk

def temperature_converter():
    try:
        temp = float(temperature.get())
        unit = unit_dropdown.get()

        if unit == "Celsius":
            result = f"Fahrenheit : {(temp * 9/5) + 32:.2f} °F \n Kelvin : {temp + 273.15:.2f} K \n"
        elif unit == "Fahrenheit":
            result = f"Celsius : {(temp - 32) * 5/9:.2f} °C \n Kelvin : {(temp - 32) * 5/9 + 273.15:.2f} K \n"
        elif unit == "Kelvin":
            result = f"Celsius : {temp - 273.15:.2f} °C \n Fahrenheit : {(temp - 273.15) * 9/5 + 32:.2f} °F \n"
        else:
            result = "Invalid unit"

        result_label.config(text=result)
    except ValueError:
        result_label.config(text="Enter a valid number")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x400")
# root.config(bg='lightpink')

title_label = tk.Label(root, text="Temperature Converter", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

tk.Label(root,text="From",font=("Arial", 12, "bold")).pack(pady=10)

unit_dropdown = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", font=("Arial", 16,"bold"))
unit_dropdown.set("Celsius")
unit_dropdown.pack(pady=5)

temperature = tk.Entry(root, font=("Arial", 16))
temperature.pack(pady=10)

button = tk.Button(root, text="Convert", command=temperature_converter,font=("Arial", 12, "bold"), bg="lightblue")
button.pack(pady=10)

tk.Label(root,text="To",font=("Arial", 12, "bold")).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 16,"bold"))
result_label.pack(pady=10)

root.mainloop()