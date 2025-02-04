import tkinter as tk
from .componets import Label
from utils.colors import primary_color

class ListAllStudents(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(height=600, width=800, background=primary_color)
        self.pack_propagate(False)

        self.frame = tk.Frame(self, background=primary_color)
        self.frame.pack(fill="both")

