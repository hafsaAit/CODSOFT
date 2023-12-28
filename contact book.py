import tkinter as tk
from tkinter import Label, Entry, Listbox, Scrollbar, Button, messagebox

class ContactBook:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")

        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        self.name_label = Label(self.master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.name_entry = Entry(self.master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = Label(self.master, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.phone_entry = Entry(self.master)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = Label(self.master, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.email_entry = Entry(self.master)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label = Label(self.master, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.address_entry = Entry(self.master)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button = Button(self.master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.view_button = Button(self.master, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.search_label = Label(self.master, text="Search:")
        self.search_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")

        self.search_entry = Entry(self.master)
        self.search_entry.grid(row=6, column=1, padx=10, pady=5)

        self.search_button = Button(self.master, text="Search", command=self.search_contact)
        self.search_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.contact_listbox = Listbox(self.master, width=40, height=10)
        self.contact_listbox.grid(row=8, column=0, columnspan=2, pady=10)

        self.scrollbar = Scrollbar(self.master)
        self.scrollbar.grid(row=8, column=2, pady=10, sticky="ns")

        self.contact_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.contact_listbox.yview)

        self.update_button = Button(self.master, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=9, column=0, columnspan=2, pady=10)

        self.delete_button = Button(self.master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=10, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Name and Phone are required fields.")

    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

    def search_contact(self):
        search_term = self.search_entry.get().lower()
        self.contact_listbox.delete(0, tk.END)

        for contact in self.contacts:
            if (
                    search_term in contact["Name"].lower() or
                    search_term in contact["Phone"].lower()
            ):
                self.contact_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()

        if selected_index:
            selected_contact = self.contacts[selected_index[0]]
            updated_name = simpledialog.askstring("Input", "Enter updated name:", initialvalue=selected_contact["Name"])
            updated_phone = simpledialog.askstring("Input", "Enter updated phone:", initialvalue=selected_contact["Phone"])
            updated_email = simpledialog.askstring("Input", "Enter updated email:", initialvalue=selected_contact["Email"])
            updated_address = simpledialog.askstring("Input", "Enter updated address:", initialvalue=selected_contact["Address"])

            if updated_name and updated_phone:
                self.contacts[selected_index[0]] = {
                    "Name": updated_name,
                    "Phone": updated_phone,
                    "Email": updated_email,
                    "Address": updated_address,
                }
                self.view_contacts()
                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showerror("Error", "Name and Phone are required fields.")
        else:
            messagebox.showerror("Error", "Please select a contact to update.")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()

        if selected_index:
            confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to delete this contact?")
            if confirmed:
                del self.contacts[selected_index[0]]
                self.view_contacts()
                messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)


