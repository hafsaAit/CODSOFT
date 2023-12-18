import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")
        return

    operator = operator_var.get()

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Cannot divide by zero.")
            return

    result_label.config(text=f"Result: {result:.2f}")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Entry widgets for user input
entry_num1 = tk.Entry(window, width=10)
entry_num1.grid(row=0, column=0, padx=10, pady=10)

