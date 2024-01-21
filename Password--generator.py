
import tkinter as tk
from tkinter import Label, Entry, Button, StringVar
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.password_var = StringVar()

        # Label and Entry for password length
        self.length_label = Label(self.master, text="Password Length:")
        self.length_label.pack(pady=5)

        self.length_entry = Entry(self.master)
        self.length_entry.pack(pady=5)

        # Button to generate password
        self.generate_button = Button(self.master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        # Label to display generated password
        self.password_label = Label(self.master, text="Generated Password:")
        self.password_label.pack(pady=5)

        # Entry to show generated password
        self.password_entry = Entry(self.master, textvariable=self.password_var, state='readonly', width=30)
        self.password_entry.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Password length must be greater than 0.")
            
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_var.set(password)
        except ValueError as e:
            self.password_var.set("Invalid length. " + str(e))

def main():
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
