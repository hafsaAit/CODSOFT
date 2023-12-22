import tkinter as tk
from tkinter import Entry, IntVar, Label, StringVar, Button, messagebox
import random
import string

def generate_password():
    password_length = length_var.get()

    if password_length <= 0:
        result_var.set("Invalid length. Please enter a positive integer.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for _ in range(password_length))

    result_var.set(generated_password)
    result_label.config(fg="red", bd=5, relief="solid")

def copy_to_clipboard():
    generated_password = result_var.get()
    window.clipboard_clear()
    window.clipboard_append(generated_password)
    window.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Label and Entry for password length
length_label = Label(window, text="Enter Password Length:")
length_label.grid(row=0, column=0, pady=(15, 5), sticky='w')

length_var = IntVar()
length_entry = Entry(window, textvariable=length_var, width=5)
length_entry.grid(row=0, column=1, pady=(15, 5))

# Button to generate password
generate_button = Button(window, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white")
generate_button.grid(row=1, column=0, pady=(10, 15))

# Label to display the generated password
result_var = StringVar()
result_label = Label(window, textvariable=result_var, wraplength=300, justify='center', font=('Helvetica', 12))
result_label.grid(row=2, column=0, pady=(5, 15))

# Button to copy password to clipboard
copy_button = Button(window, text="Copy to Clipboard", command=copy_to_clipboard, bg="#008CBA", fg="white")
copy_button.grid(row=1, column=1, pady=(10, 15), padx=(0, 10))

# Run the Tkinter event loop
window.mainloop()
