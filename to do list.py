from tkinter import *
import tkinter.messagebox

def entertask():
    def add_task(entry_text):
        if entry_text == "":
            tkinter.messagebox.showwarning(title="Warning!", message="Please enter some text.")
        else:
            listbox_task.insert(END, entry_text)
            root_add_task.destroy()

    root_add_task = Tk()
    root_add_task.title("Add Task")
    entry_task = Text(root_add_task, width=40, height=4)
    entry_task.pack(pady=10)
    button_add = Button(root_add_task, text="Add New Task", width=20, height=2, bg="#4CAF50", fg="white", command=lambda: add_task(entry_task.get("1.0", "end-1c")))
    button_add.pack(pady=10)
    root_add_task.mainloop()

def delete_task():
    selected = listbox_task.curselection()
    if selected:
        listbox_task.delete(selected[0])
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Please select a task to delete.")

def mark_completed():
    selected = listbox_task.curselection()
    if selected:
        task_text = listbox_task.get(selected)
        task_text += " ✔"
        listbox_task.delete(selected)
        listbox_task.insert(selected, task_text)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Please select a task to mark as completed.")
