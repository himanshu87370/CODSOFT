import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("600x400")
        self.root.configure(bg='#f0f8ff')

        # Initialize contact storage
        self.contacts = {}

        # Create UI components
        self.title_label = tk.Label(self.root, text="Contact Book", bg='#f0f8ff', font=('Arial', 16))
        self.title_label.pack(pady=10)

        # Add Contact
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact, bg='#90ee90', font=('Arial', 12))
        self.add_button.pack(pady=5)

        # View Contacts
        self.view_button = tk.Button(self.root, text="View Contacts", command=self.view_contacts, bg='#add8e6', font=('Arial', 12))
        self.view_button.pack(pady=5)

        # Search Contact
        self.search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact, bg='#ffb6c1', font=('Arial', 12))
        self.search_button.pack(pady=5)

        # Update Contact
        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact, bg='#ffd700', font=('Arial', 12))
        self.update_button.pack(pady=5)

        # Delete Contact
        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact, bg='#ff6347', font=('Arial', 12))
        self.delete_button.pack(pady=5)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:")
        if not name or name in self.contacts:
            messagebox.showwarning("Warning", "Contact already exists or invalid name.")
            return

        phone = simpledialog.askstring("Input", "Enter phone number:")
        email = simpledialog.askstring("Input", "Enter email:")
        address = simpledialog.askstring("Input", "Enter address:")

        if phone and email and address:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            messagebox.showinfo("Info", "Contact added successfully!")
        else:
            messagebox.showwarning("Warning", "All fields must be filled.")

    def view_contacts(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("Contact List")
        view_window.geometry("400x300")
        view_window.configure(bg='#f0f8ff')

        if not self.contacts:
            tk.Label(view_window, text="No contacts available.", bg='#f0f8ff', font=('Arial', 12)).pack(pady=10)
            return

        tree = ttk.Treeview(view_window, columns=("Phone"), show='headings')
        tree.heading("Phone", text="Phone Number")
        tree.pack(fill=tk.BOTH, expand=True)

        for name, details in self.contacts.items():
            tree.insert("", tk.END, values=(details['phone']))

    def search_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name or phone number to search:")
        if not name:
            messagebox.showwarning("Warning", "Search term cannot be empty.")
            return

        found = False
        for contact_name, details in self.contacts.items():
            if name.lower() in contact_name.lower() or name in details['phone']:
                contact_info = f"Name: {contact_name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}"
                messagebox.showinfo("Contact Found", contact_info)
                found = True
                break
        
        if not found:
            messagebox.showinfo("Not Found", "No contact found with that name or phone number.")

    def update_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to update:")
        if name not in self.contacts:
            messagebox.showwarning("Warning", "Contact does not exist.")
            return

        phone = simpledialog.askstring("Input", "Enter new phone number (leave empty to keep current):")
        email = simpledialog.askstring("Input", "Enter new email (leave empty to keep current):")
        address = simpledialog.askstring("Input", "Enter new address (leave empty to keep current):")

        if phone:
            self.contacts[name]['phone'] = phone
        if email:
            self.contacts[name]['email'] = email
        if address:
            self.contacts[name]['address'] = address
        
        messagebox.showinfo("Info", "Contact updated successfully!")

    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to delete:")
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Info", "Contact deleted successfully!")
        else:
            messagebox.showwarning("Warning", "Contact does not exist.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
