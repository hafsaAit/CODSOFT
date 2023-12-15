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
window = Tk()
window.title("To-Do App")

frame_task = Frame(window, bg="#FFD700")
frame_task.pack(pady=10)

listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font="Helvetica")
listbox_task.pack(side=LEFT)

scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=RIGHT, fill=Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

button_add = Button(window, text="Add New Task", width=20, height=2, bg="#4CAF50", fg="white", command=entertask)
button_add.pack(pady=10)

button_delete = Button(window, text="Remove Selected Task", width=20, height=2, bg="#FF6347", fg="white", command=delete_task)
button_delete.pack(pady=10)

button_mark = Button(window, text="Complete Selected Task", width=20, height=2, bg="#1E90FF", fg="white", command=mark_completed)
button_mark.pack(pady=10)

window.mainloop()
