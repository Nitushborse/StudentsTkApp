import tkinter as tk
from tkinter import messagebox
from .componets import Label, Entry, Button
from utils.colors import primary_color
from .navFrame import NavFrame
from .addStudent import AddStudentFrame

class LoginFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.configure(width=1050, height=600, background=primary_color)
        self.pack_propagate(False) 

        self.label = Label(self, text="Welcome Back!",font=("Arial", 20, "bold"))
        self.label.pack(pady=20)

        # Create a frame for the login form
        form_frame = tk.Frame(self, bg=primary_color, relief=tk.RIDGE)
        form_frame.pack(pady=20, padx=20)


        # Email label and entry
        email_label = Label(form_frame, text="Email:", font=("Arial", 12, "bold"))
        email_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        email_entry = Entry(form_frame)
        email_entry.grid(row=0, column=1, padx=10, pady=10)

        # Password label and entry
        password_label = Label(form_frame, text="Password:", font=("Arial", 12, "bold"))
        password_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        password_entry = Entry(form_frame, show="*")
        password_entry.grid(row=1, column=1, padx=10, pady=10)

        # Login button

        login_button = Button(self, text="Login",command=lambda:self.login_function(email_entry, password_entry))
        login_button.pack(pady=20)


    def login_function(self, email_entry,password_entry):
        email = email_entry.get().strip()
        password = password_entry.get().strip()

        if not email or not password:
            messagebox.showwarning("Error", "Both fields are required")
            return
        
        email_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

        if email == "bhavesh" and password == "123":
            messagebox.showinfo("Success", "Login successful!")
            self.parent.switch_frame(AddStudentFrame)  # Switch to NavFrame
            self.parent.switch(NavFrame)
        else:
            messagebox.showerror("Error", "Invalid credentials")

        # Clear input fields
        
            


       