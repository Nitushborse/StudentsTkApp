import tkinter as tk
from tkinter import ttk, messagebox
from .componets import Label, Entry, Button
from utils.colors import primary_color, text_color, secondory_color

# class AddStudentFrame(tk.Frame):
#     def __init__(self, parent):
#         super().__init__(parent)

#         self.configure(width=800, height=600, background=primary_color)
#         self.pack_propagate(False)

#         studentName = tk.LabelFrame(self, text="Student Full Name", width=800, background=primary_color, foreground=text_color)
#         studentName.pack(fill="both", padx=5, pady=5)

#         # first name
#         first_name_label = Label(studentName, text="Enter First Name", font=("Arial", 16, "bold"))
#         first_name_label.grid(row=0, column=0)

#         first_name_entry = Entry(studentName)
#         first_name_entry.grid(row=1, column=0)

#         # middle name
#         middle_name_label = Label(studentName, text="Enter Middle Name", font=("Arial", 16, "bold"))
#         middle_name_label.grid(row=0, column=1)

#         middel_name_entry = Entry(studentName)
#         middel_name_entry.grid(row=1, column=1)

#         # last name
#         last_name_label = Label(studentName, text="Enter Last Name", font=("Arial", 16, "bold"))
#         last_name_label.grid(row=0, column=2)

#         last_name_entry = Entry(studentName)
#         last_name_entry.grid(row=1, column=2)

#         for wiedget in studentName.winfo_children():
#             wiedget.grid_configure(padx=10, pady=10)

class AddStudentFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(width=800, height=600, background=primary_color)
        self.pack_propagate(False)

        # Student Name LabelFrame
        self.studentName = tk.LabelFrame(
            self, text="Student Full Name", width=800,
            background=primary_color, foreground=text_color
        )
        self.studentName.pack(fill="both", padx=5, pady=(20,15))

        # Configure grid for the LabelFrame
        for i in range(3):  # Three columns
            self.studentName.grid_columnconfigure(i, weight=1)
        self.studentName.grid_rowconfigure(0, weight=1)  # Row for labels
        self.studentName.grid_rowconfigure(1, weight=1)  # Row for entries

        # First name
        self.first_name_label = Label(self.studentName, text="Enter First Name", font=("Arial", 16, "bold"))
        self.first_name_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.first_name_entry = Entry(self.studentName)
        self.first_name_entry.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Middle name
        self.middle_name_label = Label(self.studentName, text="Enter Middle Name", font=("Arial", 16, "bold"))
        self.middle_name_label.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.middle_name_entry = Entry(self.studentName)
        self.middle_name_entry.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        # Last name
        self.last_name_label = Label(self.studentName, text="Enter Last Name", font=("Arial", 16, "bold"))
        self.last_name_label.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

        self.last_name_entry = Entry(self.studentName)
        self.last_name_entry.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)

        # ---------------------------------------------------------------
        # Student contact LabelFrame
        self.studentContact = tk.LabelFrame(
            self, text="Student Contact and Age", width=800,
            background=primary_color, foreground=text_color
        )
        self.studentContact.pack(fill="both", padx=5, pady=(15,15))

        # Configure grid for the LabelFrame
        for i in range(3):  # Three columns
            self.studentContact.grid_columnconfigure(i, weight=1)
        self.studentContact.grid_rowconfigure(0, weight=1)  # Row for labels
        self.studentContact.grid_rowconfigure(1, weight=1)  # Row for entries

        # email label

        self.email_label = Label(self.studentContact, text="Enter Email", font=("Arial", 16, "bold"))
        self.email_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.email_entry = Entry(self.studentContact)
        self.email_entry.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # mobile number label

        self.mobile_label = Label(self.studentContact, text="Enter Mobile Number", font=("Arial", 16, "bold"))
        self.mobile_label.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.mobile_entry = Entry(self.studentContact)
        self.mobile_entry.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        # mobile number label

        self.age_label = Label(self.studentContact, text="Enter age", font=("Arial", 16, "bold"))
        self.age_label.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

        self.age_entry = Entry(self.studentContact)
        self.age_entry.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)
        # -------------------------------------------------------------------------------




        # course info LabelFrame
        self.courseFrame = tk.LabelFrame(self, text="Course Info", width=800,
            background=primary_color, foreground=text_color)
        self.courseFrame.pack(fill="both", pady=(15,15), padx=5)

        # Configure grid for the LabelFrame
        for i in range(3):  # Three columns
            self.courseFrame.grid_columnconfigure(i, weight=1)
        self.courseFrame.grid_rowconfigure(0, weight=1)  # Row for labels
        self.courseFrame.grid_rowconfigure(1, weight=1)  # Row for entries

        # course combox

        style = ttk.Style()
        style.theme_use('default')  # Ensure compatibility
        style.configure(
            "Custom.TCombobox",
            fieldbackground=secondory_color,  # Background of the entry field
            background=secondory_color,          # Background of the dropdown
            foreground=text_color,       # Text color
        )

        style.map(
            "Custom.TCombobox",
            fieldbackground=[("readonly", secondory_color)],  # Background when readonly
            foreground=[("readonly", text_color)],            # Text color when readonly
        )

        self.course_label = Label(self.courseFrame, text="Select Course", font=("Arial", 16, "bold"))
        self.course_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.courseCombobox = ttk.Combobox(self.courseFrame, values=["MAC", "MBA", "BCA", "BBA"], font=("Arial", 16, "bold"), style="Custom.TCombobox")
        self.courseCombobox.set("MCA")
        self.courseCombobox["state"] = "readonly"
        self.courseCombobox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # year label

        self.year_label = Label(self.courseFrame, text="Enter year", font=("Arial", 16, "bold"))
        self.year_label.grid(row=0, column=1,sticky="nsew", padx=10, pady=10)

        self.year_entry = Entry(self.courseFrame)
        self.year_entry.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        # roll number label

        self.roll_label = Label(self.courseFrame, text="Enter roll.No", font=("Arial", 16, "bold"))
        self.roll_label.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

        self.roll_entry = Entry(self.courseFrame)
        self.roll_entry.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)

        # ---------------------------------------------------------------------------

        # submit button
        self.submit_btn = Button(self, text="Submit",width = 20, command=lambda:self.submit())
        self.submit_btn.pack(fill="y", pady=(30,0))

    def submit(self):
        print("hello")

    