import json
import os
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

# Calea catre fisiere
DATA_FILE = "passwords.json"
KEY_FILE = "secret.key"

# ------------------ Criptare ------------------
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

def load_key():
    return open(KEY_FILE, "rb").read()

def encrypt_password(password, key):
    return Fernet(key).encrypt(password.encode()).decode()

def decrypt_password(encrypted_password, key):
    return Fernet(key).decrypt(encrypted_password.encode()).decode()

# ------------------ JSON ------------------
def load_passwords():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_passwords(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# ------------------ Functionalitati ------------------
def add_password_gui():
    site = site_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if not site or not username or not password:
        messagebox.showwarning("Empty Fields", "Please fill in all fields.")
        return

    encrypted = encrypt_password(password, key)
    passwords = load_passwords()
    passwords.append({"site": site, "username": username, "password": encrypted})
    save_passwords(passwords)
    messagebox.showinfo("Saved", "Password saved successfully!")
    site_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def view_passwords_gui():
    passwords = load_passwords()
    if not passwords:
        messagebox.showinfo("No Passwords", "No saved passwords found.")
        return

    result = ""
    for entry in passwords:
        decrypted = decrypt_password(entry["password"], key)
        result += f"Site: {entry['site']}\nUsername: {entry['username']}\nPassword: {decrypted}\n\n"

    messagebox.showinfo("Saved Passwords", result)

def exit_app():
    root.destroy()

# ------------------ Interfata Grafica ------------------
if not os.path.exists(KEY_FILE):
    generate_key()
key = load_key()

root = tk.Tk()
root.title("Password Manager")
root.geometry("350x250")
root.config(bg="#f0f0f0")

# Etichete si campuri
site_label = tk.Label(root, text="Site:", bg="#f0f0f0")
site_label.pack()
site_entry = tk.Entry(root, width=40)
site_entry.pack(pady=2)

username_label = tk.Label(root, text="Username:", bg="#f0f0f0")
username_label.pack()
username_entry = tk.Entry(root, width=40)
username_entry.pack(pady=2)

password_label = tk.Label(root, text="Password:", bg="#f0f0f0")
password_label.pack()
password_entry = tk.Entry(root, show="*", width=40)
password_entry.pack(pady=2)

# Butoane
tk.Button(root, text="Add Password", command=add_password_gui, bg="#4caf50", fg="white").pack(pady=5)
tk.Button(root, text="View Passwords", command=view_passwords_gui, bg="#2196f3", fg="white").pack(pady=5)
tk.Button(root, text="Exit", command=exit_app, bg="#f44336", fg="white").pack(pady=5)

root.mainloop()
