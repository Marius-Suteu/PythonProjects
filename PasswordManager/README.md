# 🔐 Password Manager with GUI and Encryption

A simple Python password manager with a graphical interface using `Tkinter`, data encryption using `cryptography`, and storage in a local JSON file.

## ✨ Features
- Add and view encrypted passwords via a user-friendly GUI
- Passwords stored securely in `passwords.json`
- Encryption key saved in `secret.key`

## 📂 Project Structure
```
password_manager/
├── main.py               # Main application with GUI
├── passwords.json        # Encrypted passwords (auto-created)
├── secret.key            # Encryption key (auto-created)
```

## 🔧 Requirements
Install required packages:
```bash
pip install cryptography
```
Tkinter is included by default in most Python distributions.

## 🚀 Running the Application
```bash
python main.py
```

## 🛡️ How It Works
- **Encryption:** Uses `Fernet` symmetric encryption (AES under the hood)
- **Storage:** Passwords are saved as encrypted strings in `passwords.json`
- **Key Handling:** If no key is found, a new one is generated and saved to `secret.key`

## 🖥️ User Interface
- Enter site, username, and password
- Click **Add Password** to encrypt and save it
- Click **View Passwords** to decrypt and display stored credentials

## ⚠️ Disclaimer
This project is for learning purposes. For real-world password management, use secure and audited tools such as Bitwarden, 1Password, or KeePass.

## 👨‍💻 Author
Marius Șuteu  
GitHub: [Marius-Suteu](https://github.com/Marius-Suteu)
