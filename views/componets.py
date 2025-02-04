import tkinter as tk
from tkinter import ttk
from utils.colors import primary_color, secondory_color, text_color

def Label(parent = None, text="add text",bg = primary_color, fg = text_color, variable = None, **kargs):
    label = tk.Label(parent, text=text, bg=bg, fg=fg, variable=variable, **kargs)
    return label

def Entry(parent = None,bg = secondory_color, fg = text_color,variable = None, **kargs):
    style = ttk.Style()
    style.configure(
            "Custom.TEntry",
            fieldbackground=bg, 
            foreground=fg,         
            padding=5,
            
        )
    
    Entry = ttk.Entry(parent, font=("Arial", 14, "bold"), style="Custom.TEntry", **kargs)

    return Entry

def Button(parent = None,text="add text",bg = secondory_color, fg = text_color, **kargs):
    style = ttk.Style()
    style.configure(
        "Custom.TButton", 
        background=bg,
        foreground=fg,
        font=("Arial", 14, "bold"),
        padding=10,
    )

    style.map(
        "Custom.TButton",
        background=[("active", "#005f8a"), ("pressed", "#004f70")] 
    )

    Button = ttk.Button(parent, text=text, style="Custom.TButton", **kargs)

    return Button