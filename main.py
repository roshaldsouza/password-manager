from tkinter import Tk, Label, Entry, Button, messagebox, Frame, simpledialog
from crypto import Crypto
from pwned import is_password_pwned
from database import init_db, add_password

class PasswordManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("400x300")
        
        # Initialize DB
        init_db()
        
        # Master Key Setup
        self.master_key = self.get_master_key()
        self.setup_ui()

    def get_master_key(self):
        """Prompt for master password securely"""
        key = simpledialog.askstring("Master Password", "Set your master password:", show='*')
        if not key:
            messagebox.showerror("Error", "Master password is required!")
            self.root.destroy()
            exit()
        return key

    def setup_ui(self):
        # Main Frame
        self.main_frame = Frame(self.root)
        self.main_frame.pack(pady=20)
        
        # Service
        Label(self.main_frame, text="Service:").grid(row=0, column=0)
        self.service_entry = Entry(self.main_frame)
        self.service_entry.grid(row=0, column=1)
        
        # Username
        Label(self.main_frame, text="Username:").grid(row=1, column=0)
        self.username_entry = Entry(self.main_frame)
        self.username_entry.grid(row=1, column=1)
        
        # Password
        Label(self.main_frame, text="Password:").grid(row=2, column=0)
        self.password_entry = Entry(self.main_frame, show="*")
        self.password_entry.grid(row=2, column=1)
        
        # Buttons
        Button(self.root, text="Save Password", command=self.save_password).pack(pady=10)

    def save_password(self):
        service = self.service_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not all([service, username, password]):
            messagebox.showerror("Error", "All fields are required!")
            return
        
        if is_password_pwned(password):
            messagebox.showwarning("Warning", "This password has been compromised!")
            return
        
        encrypted = Crypto(self.master_key).encrypt(password)
        add_password(service, username, encrypted)
        messagebox.showinfo("Success", "Password saved securely!")

if __name__ == "__main__":
    root = Tk()
    app = PasswordManagerGUI(root)
    root.mainloop()