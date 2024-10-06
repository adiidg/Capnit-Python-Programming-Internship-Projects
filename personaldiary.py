import tkinter as tk
from tkinter import messagebox, filedialog

def save_entry():
    text = diary_text.get("1.0", tk.END)
    if text.strip():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt")],
                                                 title="Save Diary Entry")
        if file_path:
            with open(file_path, "w") as file:
                file.write(text)
            messagebox.showinfo("Success", "Diary entry saved successfully!")
    else:
        messagebox.showwarning("Input Error", "Diary entry is empty! Please write something before saving.")

def open_entry():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Files", "*.txt")],
                                           title="Open Diary Entry")
    if file_path:
        with open(file_path, "r") as file:
            text = file.read()
            diary_text.delete("1.0", tk.END)
            diary_text.insert(tk.END, text)

root = tk.Tk()
root.title("Personal Diary")
root.geometry("600x500")
root.configure(bg="#1C1C1C")

diary_text = tk.Text(root, wrap="word", font=("Arial", 14), bg="#2C2C2C", fg="#F0F0F0", insertbackground="#FFD700", 
                     width=50, height=20, padx=15, pady=15)
diary_text.pack(padx=15, pady=15, fill="both", expand=True)

button_frame = tk.Frame(root, bg="#1C1C1C")
button_frame.pack(pady=10)

save_button = tk.Button(button_frame, text="💾 Save Entry", font=("Arial", 14), bg="#FF6347", fg="white", 
                        activebackground="#FF4500", activeforeground="white", padx=15, pady=10, command=save_entry)
save_button.grid(row=0, column=0, padx=20, pady=10)

open_button = tk.Button(button_frame, text="📂 Open Entry", font=("Arial", 14), bg="#4682B4", fg="white", 
                        activebackground="#4169E1", activeforeground="white", padx=15, pady=10, command=open_entry)
open_button.grid(row=0, column=1, padx=20, pady=10)

root.mainloop()
