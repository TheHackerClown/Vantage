import tkinter as tk
from tkinter import ttk
from pathlib import Path

file_dir = Path(__file__).resolve().parent
vantage = tk.Tk()

vantage.geometry("1920x1080")
# Import the tcl file
vantage.tk.call('source', file_dir / 'assets/theme/forest-dark.tcl')

# Set the theme with the theme_use method
ttk.Style().theme_use('forest-dark')

# A themed (ttk) button
button = ttk.Button(vantage, text="I'm a themed button")
button.pack(pady=20)


vantage.resizable(False,False)
vantage.mainloop()