import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def update_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, entry.get())
        entry.delete(0, tk.END)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to update.")

def clear_tasks():
    task_listbox.delete(0, tk.END)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root = tk.Tk()
root.title("To-Do List App")
root.geometry("500x400")
root.configure(bg="#1C1C1C")

entry = tk.Entry(root, width=40, font=('Arial', 14), bg="#2C2C2C", fg="white", insertbackground="white", relief="solid", bd=1)
entry.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

add_button = tk.Button(root, text="Add Task", width=10, font=('Arial', 12), bg="#00BFFF", fg="white", activebackground="#1E90FF", relief="flat", command=add_task)
add_button.grid(row=0, column=3, padx=10)

task_listbox = tk.Listbox(root, height=10, width=50, font=('Arial', 14), bg="#2C2C2C", fg="#F0F0F0", selectbackground="#4682B4", relief="solid", bd=1)
task_listbox.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

update_button = tk.Button(root, text="Update Task", width=12, font=('Arial', 12), bg="#32CD32", fg="white", activebackground="#228B22", relief="flat", command=update_task)
update_button.grid(row=2, column=1, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Task", width=12, font=('Arial', 12), bg="#FF4500", fg="white", activebackground="#FF6347", relief="flat", command=delete_task)
delete_button.grid(row=2, column=2, padx=10, pady=10)

clear_button = tk.Button(root, text="Clear All Tasks", width=14, font=('Arial', 12), bg="#FF8C00", fg="white", activebackground="#FFA500", relief="flat", command=clear_tasks)
clear_button.grid(row=3, column=0, columnspan=4, padx=20, pady=10)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
