import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactManagerGUI:
    button_width = 20  # Define button width as a class variable
    font_style = ("Helvetica", 12)  # Define font style

    def __init__(self, master, bg_color="#fffee0"):
        self.master = master
        self.master.title("Contact Management System")
        self.master.geometry("500x500")
        self.master.configure(bg=bg_color)
        self.master.resizable(False, False)  # Disable window resizing

        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        self.add_button = tk.Button(self.master, text="Add a New Contact", font=self.font_style, bg="#ff8000", fg="white", command=self.add_contact, width=self.button_width)
        self.add_button.pack(pady=10)

        self.view_button = tk.Button(self.master, text="View Contact", font=self.font_style, bg="#4caf50", fg="white", command=self.view_contacts, width=self.button_width)
        self.view_button.pack(pady=10)

        self.edit_button = tk.Button(self.master, text="Edit Contact", font=self.font_style, bg="#008CBA", fg="white", command=self.edit_contact, width=self.button_width)
        self.edit_button.pack(pady=10)

        self.delete_button = tk.Button(self.master, text="Delete Contact", font=self.font_style, bg="#f44336", fg="white", command=self.delete_contact, width=self.button_width)
        self.delete_button.pack(pady=10)

        self.database_button = tk.Button(self.master, text="View Database", font=self.font_style, bg="#009688", fg="white", command=self.view_database, width=self.button_width)
        self.database_button.pack(pady=10)

    def add_contact(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Contact")
        add_window.geometry("500x500")
        add_window.configure(bg="#fffee0")
        add_window.resizable(False, False)  # Disable window resizing

        tk.Label(add_window, text="Name:", bg="#fffee0", font=self.font_style).pack(pady=5)
        name_entry = tk.Entry(add_window, font=self.font_style)
        name_entry.pack()

        tk.Label(add_window, text="Phone Number:", bg="#fffee0", font=self.font_style).pack(pady=5)
        phone_entry = tk.Entry(add_window, font=self.font_style)
        phone_entry.pack()

        tk.Label(add_window, text="E-mail Address:", bg="#fffee0", font=self.font_style).pack(pady=5)
        email_entry = tk.Entry(add_window, font=self.font_style)
        email_entry.pack()

        add_button = tk.Button(add_window, text="Add", font=self.font_style, bg="#ff8000", fg="white", command=lambda: self.save_contact(name_entry.get(), phone_entry.get(), email_entry.get(), add_window), width=self.button_width)
        add_button.pack(pady=10)

    def save_contact(self, name, phone, email, window):
        if not name or not phone or not email:
            messagebox.showerror("Error", "Please fill in all the fields.")
            return
        if not phone.isdigit():
            messagebox.showerror("Error", "Phone number should contain only digits.")
            return

        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        messagebox.showinfo("Success", "Contacts added successfully.")
        window.destroy()

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts to display.")
            return

        view_window = tk.Toplevel(self.master)
        view_window.title("View Contact List")
        view_window.geometry("500x500")
        view_window.configure(bg="#fffee0")
        view_window.resizable(False, False)  # Disable window resizing

        for contact in self.contacts:
            tk.Label(view_window, text=f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}", bg="#fffee0", font=self.font_style).pack(pady=5)

    def edit_contact(self):
        edit_window = tk.Toplevel(self.master)
        edit_window.title("Edit Existing Contacts")
        edit_window.geometry("500x500")
        edit_window.configure(bg="#fffee0")
        edit_window.resizable(False, False)  # Disable window resizing

        if not self.contacts:
            messagebox.showinfo("Info", "No contacts to edit.")
            edit_window.destroy()
            return

        tk.Label(edit_window, text="Enter the Name of Contact to Edit:", bg="#fffee0", font=self.font_style).pack(pady=5)
        name_entry = tk.Entry(edit_window, font=self.font_style)
        name_entry.pack()

        edit_button = tk.Button(edit_window, text="Edit", font=self.font_style, bg="#008CBA", fg="white", command=lambda: self.open_edit_window(name_entry.get(), edit_window), width=self.button_width)
        edit_button.pack(pady=10)

    def open_edit_window(self, name, window):
        for contact in self.contacts:
            if contact.name == name:
                edit_window = tk.Toplevel(self.master)
                edit_window.title("Edit Contact")
                edit_window.geometry("500x500")
                edit_window.configure(bg="#fffee0")
                edit_window.resizable(False, False)  # Disable window resizing

                tk.Label(edit_window, text="New Name:", bg="#fffee0", font=self.font_style).pack(pady=5)
                new_name_entry = tk.Entry(edit_window, font=self.font_style)
                new_name_entry.pack()

                tk.Label(edit_window, text="New Phone Number:", bg="#fffee0", font=self.font_style).pack(pady=5)
                new_phone_entry = tk.Entry(edit_window, font=self.font_style)
                new_phone_entry.pack()

                tk.Label(edit_window, text="New Email-Address:", bg="#fffee0", font=self.font_style).pack(pady=5)
                new_email_entry = tk.Entry(edit_window, font=self.font_style)
                new_email_entry.pack()

                save_button = tk.Button(edit_window, text="Save", font=self.font_style, bg="#ff8000", fg="white", command=lambda: self.save_edit(contact, new_name_entry.get(), new_phone_entry.get(), new_email_entry.get(), window, edit_window), width=self.button_width)
                save_button.pack(pady=10)
                return

        messagebox.showerror("Error", "Contact not found.")
        window.destroy()

    def save_edit(self, contact, new_name, new_phone, new_email, window, edit_window):
        contact.name = new_name
        contact.phone = new_phone
        contact.email = new_email
        messagebox.showinfo("Success", "Contact updated successfully.")
        window.destroy()
        edit_window.destroy()

    def delete_contact(self):
        delete_window = tk.Toplevel(self.master)
        delete_window.title("Delete Contact")
        delete_window.geometry("500x500")
        delete_window.configure(bg="#fffee0")
        delete_window.resizable(False, False)  # Disable window resizing

        if not self.contacts:
            messagebox.showinfo("Info", "No contacts to delete.")
            delete_window.destroy()
            return

        tk.Label(delete_window, text="Enter the Name of Contact to Delete:", bg="#fffee0", font=self.font_style).pack(pady=5)
        name_entry = tk.Entry(delete_window, font=self.font_style)
        name_entry.pack()

        delete_button = tk.Button(delete_window, text="Delete", font=self.font_style, bg="#f44336", fg="white", command=lambda: self.confirm_delete(name_entry.get(), delete_window), width=self.button_width)
        delete_button.pack(pady=10)

    def confirm_delete(self, name, window):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                messagebox.showinfo("Success", "Contact deleted successfully.")
                window.destroy()
                return

        messagebox.showerror("Error", "Contact not found.")
        window.destroy()

    def view_database(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts to stored.")
            return

        database_window = tk.Toplevel(self.master)
        database_window.title("Viewing Contacts Database")
        database_window.geometry("500x500")
        database_window.configure(bg="#fffee0")
        database_window.resizable(False, False)  # Disable window resizing

        for i, contact in enumerate(self.contacts):
            tk.Label(database_window, text=f"Contact {i+1}:", bg="#fffee0", font=("Helvetica", 12, "bold")).pack(pady=5)
            tk.Label(database_window, text=f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}", bg="#fffee0", font=("Helvetica", 12)).pack(pady=5)

def main():
    root = tk.Tk()
    contact_manager = ContactManagerGUI(root, bg_color="#fffee0")
    root.mainloop()

if __name__ == "__main__":
    main()
