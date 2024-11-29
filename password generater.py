import tkinter as tk
import random
import string
from tkinter import messagebox

def generate_password():
    length = int(length_entry.get())
    characters = ""
    if include_uppercase.get():
        characters += string.ascii_uppercase
    if include_lowercase.get():
        characters += string.ascii_lowercase
    if include_numbers.get():
        characters += string.digits
    if include_special.get():
        characters += string.punctuation
    if exclude_similar.get():
        characters = characters.replace('l', '').replace('1', '').replace('I', '').replace('O', '').replace('0', '')
    
    if characters:
        password = ''.join(random.choice(characters) for i in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    else:
        messagebox.showwarning("Warning", "Please select at least one character set")

def accept_password():
    password = password_entry.get()
    if password:
        messagebox.showinfo("Success", f"Your password has been successfully generated:\n{password}")
    else:
        messagebox.showwarning("Warning", "No password generated")

def reset_fields():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    include_uppercase.set(False)
    include_lowercase.set(False)
    include_numbers.set(False)
    include_special.set(False)
    exclude_similar.set(False)

root = tk.Tk()
root.title("Password Generator")
root.geometry("450x550")
root.resizable(False, False)
root.configure(bg="grey")

frame = tk.Frame(root, padx=10, pady=10, bg="grey")
frame.pack(expand=True)

title_label = tk.Label(frame, text="Password Generator", font=("Helvetica", 18, "bold"), bg="grey", fg="white")
title_label.pack(pady=10)

username_label = tk.Label(frame, text="Username:", font=("Helvetica", 12), bg="grey", fg="white")
username_label.pack(pady=5)
username_entry = tk.Entry(frame, width=30, font=("Helvetica", 12))
username_entry.pack(pady=5)

length_label = tk.Label(frame, text="Password Length:", font=("Helvetica", 12), bg="grey", fg="white")
length_label.pack(pady=5)
length_entry = tk.Entry(frame, width=30, font=("Helvetica", 12))
length_entry.pack(pady=5)

include_uppercase = tk.BooleanVar()
tk.Checkbutton(frame, text="Include Uppercase Letters", variable=include_uppercase, font=("Helvetica", 12), bg="grey", fg="white", selectcolor="#333333").pack(anchor='w')

include_lowercase = tk.BooleanVar()
tk.Checkbutton(frame, text="Include Lowercase Letters", variable=include_lowercase, font=("Helvetica", 12), bg="grey", fg="white", selectcolor="#333333").pack(anchor='w')

include_numbers = tk.BooleanVar()
tk.Checkbutton(frame, text="Include Numbers", variable=include_numbers, font=("Helvetica", 12), bg="grey", fg="white", selectcolor="#333333").pack(anchor='w')

include_special = tk.BooleanVar()
tk.Checkbutton(frame, text="Include Special Characters", variable=include_special, font=("Helvetica", 12), bg="grey", fg="white", selectcolor="#333333").pack(anchor='w')

exclude_similar = tk.BooleanVar()
tk.Checkbutton(frame, text="Exclude Similar Characters", variable=exclude_similar, font=("Helvetica", 12), bg="grey", fg="white", selectcolor="#333333").pack(anchor='w')

generate_button = tk.Button(frame, text="Generate Password", font=("Helvetica", 12), command=generate_password, bg="#4CAF50", fg="white")
generate_button.pack(pady=10)

password_label = tk.Label(frame, text="Generated Password:", font=("Helvetica", 12), bg="grey", fg="white")
password_label.pack(pady=5)
password_entry = tk.Entry(frame, width=30, font=("Helvetica", 12))
password_entry.pack(pady=5)

accept_button = tk.Button(frame, text="Accept", font=("Helvetica", 12), command=accept_password, bg="#4CAF50", fg="white")
accept_button.pack(pady=5)

reset_button = tk.Button(frame, text="Reset", font=("Helvetica", 12), command=reset_fields, bg="#f44336", fg="white")
reset_button.pack(pady=5)

root.mainloop()
