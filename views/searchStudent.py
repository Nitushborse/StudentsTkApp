# # import tkinter as tk
# # from .componets import Button, Label, Entry
# # from utils.colors import primary_color, secondory_color, text_color
# # from tkinter import ttk


# # class SearchStudentFrame(tk.Frame):
# #     def __init__(self, parent,text = "add text", btntext = "add text",func = None):
# #         super().__init__(parent)

# #         self.configure(width=800, height=600, background=primary_color)
# #         self.pack_propagate(False)

# #         self.frame = tk.Frame(self, background=primary_color)
# #         self.frame.pack(padx=20, pady=20)

# #         for i in range(3):  # Three columns
# #             self.frame.grid_columnconfigure(i, weight=1)
# #         self.frame.grid_rowconfigure(0, weight=1)  # Row for labels
# #         self.frame.grid_rowconfigure(1, weight=1)  # Row for entries
# #         self.frame.grid_rowconfigure(2, weight=1)  # Row for button

# #         self.label = Label(self.frame, text=text, font = ("Arial", 30, "bold"))
# #         self.label.grid(row=0, column=0, columnspan=3, sticky="w")

# #         self.value = Entry(self.frame)
# #         self.value.grid(row=1, column=0)

# #         # course combox

# #         style = ttk.Style()
# #         style.theme_use('default')  # Ensure compatibility
# #         style.configure(
# #             "Custom.TCombobox",
# #             fieldbackground=secondory_color,  # Background of the entry field
# #             background=secondory_color,          # Background of the dropdown
# #             foreground=text_color,       # Text color
# #         )

# #         style.map(
# #             "Custom.TCombobox",
# #             fieldbackground=[("readonly", secondory_color)],  # Background when readonly
# #             foreground=[("readonly", text_color)],            # Text color when readonly
# #         )

        
# #         self.courseCombobox = ttk.Combobox(self.frame, values=["Roll.No", "Name","Id", "Email"], font=("Arial", 16, "bold"), style="Custom.TCombobox")
# #         self.courseCombobox.set("roll.No")
# #         self.courseCombobox["state"] = "readonly"
# #         self.courseCombobox.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

# #         self.searchbtn = Button(self.frame, text="Search")
# #         self.searchbtn.grid(row=2, column=1, columnspan=3)

# import tkinter as tk
# from .componets import Button, Label, Entry
# from utils.colors import primary_color, secondory_color, text_color
# from tkinter import ttk

# class SearchStudentFrame(tk.Frame):
#     def __init__(self, parent, text="Search Student", btntext="Search", func=None):
#         super().__init__(parent)

#         self.configure(width=800, height=600, background=primary_color)
#         self.pack_propagate(False)

#         # Main frame
#         self.frame = tk.Frame(self, background=primary_color)
#         self.frame.pack(padx=30, pady=30, fill="both", expand=True)

#         # Configure grid for better layout
#         self.frame.grid_columnconfigure(0, weight=1)
#         self.frame.grid_columnconfigure(1, weight=1)
#         self.frame.grid_columnconfigure(2, weight=1)
#         self.frame.grid_rowconfigure(0, weight=1)  # Row for title
#         self.frame.grid_rowconfigure(1, weight=1)  # Row for input fields
#         self.frame.grid_rowconfigure(2, weight=1)  # Row for button

#         # Title Label
#         self.label = Label(
#             self.frame, 
#             text=text, 
#             font=("Arial", 30, "bold")
#         )
#         self.label.grid(row=0, column=0, columnspan=3, pady=(0, 20), sticky="ew")

#         # Input Entry
#         self.value = Entry(
#             self.frame
#         )
#         self.value.grid(row=1, column=0, padx=10, pady=10, sticky="w")

#         # Combobox for options
#         style = ttk.Style()
#         style.theme_use('default')
#         style.configure(
#             "Custom.TCombobox",
#             fieldbackground=secondory_color,
#             background=secondory_color,
#             foreground=text_color,
#             arrowcolor=text_color
#         )

#         self.courseCombobox = ttk.Combobox(
#             self.frame, 
#             values=["Roll.No", "Name", "Id", "Email"], 
#             font=("Arial", 16, "bold"), 
#             style="Custom.TCombobox"
#         )
#         self.courseCombobox.set("Roll.No")
#         self.courseCombobox["state"] = "readonly"
#         self.courseCombobox.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

#         # Search Button
#         self.searchbtn = Button(
#             self.frame, 
#             text=btntext, 

#         )
#         self.searchbtn.grid(row=2, column=0, columnspan=3, pady=(20, 0), sticky="n")




    
import tkinter as tk
from .componets import Button, Label, Entry
from utils.colors import primary_color, secondory_color, text_color
from tkinter import ttk

class SearchStudentFrame(tk.Frame):
    def __init__(self, parent, text="Search Students", btntext="Search", func=None):
        super().__init__(parent)

        self.configure(width=800, height=600, background=primary_color)
        self.pack_propagate(False)

        # Header frame for title
        self.header_frame = tk.Frame(self, background=primary_color)
        self.header_frame.pack(fill="x", pady=(10, 20))

        self.label = Label(
            self.header_frame, 
            text=text, 
            font=("Arial", 30, "bold")
        )
        self.label.pack()

        # Search frame for inputs
        self.search_frame = tk.Frame(self, background=primary_color)
        self.search_frame.pack(padx=20, pady=10, fill="x")

        self.value = Entry(
            self.search_frame
        )
        self.value.grid(row=0, column=0, padx=(70,10), pady=10)

        # Course combobox
        style = ttk.Style()
        style.theme_use('default')
        style.configure(
            "Custom.TCombobox",
            fieldbackground=secondory_color,
            background=secondory_color,
            foreground=text_color,
            arrowcolor=text_color
        )

        self.courseCombobox = ttk.Combobox(
            self.search_frame, 
            values=["Roll.No", "Name", "Id", "Email"], 
           
            style="Custom.TCombobox",
            font=("Arial", 18, "bold")
        )
        self.courseCombobox.set("Roll.No")
        self.courseCombobox["state"] = "readonly"
        self.courseCombobox.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Search button
        self.searchbtn = Button(
            self.search_frame, 
            text=btntext,
        )
        self.searchbtn.grid(row=0, column=2, padx=10, pady=10)

        # Table frame for displaying results
        self.table_frame = tk.Frame(self, background=primary_color)
        self.table_frame.pack(padx=20, pady=(20, 10), fill="both", expand=True)

        self.placeholder_label = Label(
            self.table_frame, 
            text="Here we display the student that we search in the tree view"
        )
        self.placeholder_label.pack(expand=True, fill="both")