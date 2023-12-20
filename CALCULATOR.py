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

operator_var = tk.StringVar()
operator_var.set("+")  # default operator

operator_menu = tk.OptionMenu(window, operator_var, "+", "-", "*", "/")
operator_menu.grid(row=0, column=1, padx=10, pady=10)

entry_num2 = tk.Entry(window, width=10)
entry_num2.grid(row=0, column=2, padx=10, pady=10)

# Button to perform calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=0, columnspan=3, pady=10)

# Label to display the result
result_label = tk.Label(window, text="Result: ")
result_label.grid(row=2, column=0, columnspan=3, pady=10)

# Run the Tkinter event loop
window.mainloop()


