import tkinter as tk
from tkinter import messagebox, ttk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("500x400")
        self.root.configure(bg='#f0f8ff')

        # Password Length Input
        self.label_frame = tk.Frame(self.root, bg='#f0f8ff')
        self.label_frame.pack(pady=20)

        self.length_label = tk.Label(self.label_frame, text="Password Length:", bg='#f0f8ff', font=('Arial', 12))
        self.length_label.grid(row=0, column=0, padx=10)

        self.length_entry = tk.Entry(self.label_frame, width=10, font=('Arial', 12), bd=3)
        self.length_entry.grid(row=0, column=1, padx=10)

        # Complexity Selection
        self.complexity_label = tk.Label(self.label_frame, text="Complexity Level:", bg='#f0f8ff', font=('Arial', 12))
        self.complexity_label.grid(row=1, column=0, padx=10)

        self.complexity_var = tk.StringVar(value='Low')
        self.complexity_menu = ttk.Combobox(self.label_frame, textvariable=self.complexity_var, values=['Low', 'Medium', 'High'], state='readonly')
        self.complexity_menu.grid(row=1, column=1, padx=10)

        # Generate Button
        self.button_frame = tk.Frame(self.root, bg='#f0f8ff')
        self.button_frame.pack(pady=10)

        self.generate_button = tk.Button(self.button_frame, text="Generate Password", command=self.generate_password, bg='#90ee90', font=('Arial', 12))
        self.generate_button.grid(row=0, column=0, padx=5)

        # Result Display
        self.result_frame = tk.Frame(self.root, bg='#f0f8ff')
        self.result_frame.pack(pady=20)

        self.result_label = tk.Label(self.result_frame, text="Generated Password:", bg='#f0f8ff', font=('Arial', 12))
        self.result_label.grid(row=0, column=0, padx=10)

        self.password_entry = tk.Entry(self.result_frame, width=40, font=('Arial', 12), bd=3, state='readonly')
        self.password_entry.grid(row=0, column=1, padx=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                raise ValueError("Password length must be at least 1")

            complexity = self.complexity_var.get()
            if complexity == 'Low':
                password_characters = string.ascii_letters + string.digits
            elif complexity == 'Medium':
                password_characters = string.ascii_letters + string.digits + string.punctuation[:10]  # Limited special characters
            elif complexity == 'High':
                password_characters = string.ascii_letters + string.digits + string.punctuation  # Full set of special characters

            password = ''.join(random.choice(password_characters) for _ in range(length))

            self.password_entry.config(state='normal')
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
            self.password_entry.config(state='readonly')
        except ValueError as e:
            messagebox.showwarning("Invalid Input", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
