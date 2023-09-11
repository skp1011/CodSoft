import tkinter as tk
from tkinter import messagebox

# -----------------add a new task to the to-do list---------------------------
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task to add.")

# ------------------delete a selected task from the to-do list-----------------
def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Select a task to delete.")

#  -------------------update/edit the selected task----------------------------
def update_task():
    try:
        index = listbox.curselection()
        updated_task = entry.get()
        if updated_task:
            listbox.delete(index)
            listbox.insert(index, updated_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter an updated task.")
    except:
        messagebox.showwarning("Warning", "Select a task to update.")

# ---------------------mark the selected task as done-----------------------------
def mark_as_done():
    try:
        index = listbox.curselection()
        task = listbox.get(index)
        updated_task = task + " (Done)"
        listbox.delete(index)
        listbox.insert(index, updated_task)
    except:
        messagebox.showwarning("Warning", "Select a task to mark as done.")

# ----------------------Creating the main window-----------------------------------
window = tk.Tk()
window.title("To-Do List")


# Creating the to-do list
listbox = tk.Listbox(window, width=50, height=10, font=("Arial", 12))
listbox.pack(pady=20)

# ---------------------Creating the scrollbar---------------------------------------
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#------------------- Adding the scrollbar to the to-do list-------------------------
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# -------------------Creating the task entry field----------------------------------
entry = tk.Entry(window, font=("Arial", 12))
entry.pack(pady=20)

# -------------------Creating buttons to add, delete, update, and mark as done tasks-
add_button = tk.Button(window, text="Add the task", command=add_task)
add_button.pack(pady=15)
delete_button = tk.Button(window, text="Delete the task", command=delete_task)
delete_button.pack(pady=10)
update_button = tk.Button(window, text="Update the task", command=update_task)
update_button.pack(pady=15)
mark_done_button = tk.Button(window, text="Mark the task as Done", command=mark_as_done)
mark_done_button.pack(pady=15)

# -------------------Starting the GUI main loop--------------------------------------
window.mainloop()