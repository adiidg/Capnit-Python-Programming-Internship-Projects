import tkinter as tk
from tkinter import messagebox

def click(event):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + event.widget.cget("text"))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        messagebox.showerror("Error", "Invalid Input")

root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="#2E2E2E")

entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid", bg="#D9D9D9", fg="black", justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

button_colors = {
    '/': '#FF9500', '*': '#FF9500', '-': '#FF9500', '+': '#FF9500', '=': '#FF9500', 
    'C': '#FF3B30', '0': '#505050', '1': '#505050', '2': '#505050', '3': '#505050',
    '4': '#505050', '5': '#505050', '6': '#505050', '7': '#505050', '8': '#505050', 
    '9': '#505050'
}

row_value = 1
col_value = 0

for button in buttons:
    b = tk.Button(root, text=button, font=('Arial', 18), width=4, height=2, bg=button_colors[button], fg="white", bd=0)
    b.grid(row=row_value, column=col_value, padx=5, pady=5)
    
    if button == "=":
        b.bind('<Button-1>', lambda event: calculate())
    elif button == "C":
        b.bind('<Button-1>', lambda event: clear())
    else:
        b.bind('<Button-1>', click)
    
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

root.mainloop()
