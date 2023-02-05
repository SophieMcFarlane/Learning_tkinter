import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Example")

initial_value = tk.StringVar(value=20)
spin_box = ttk.Spinbox(
    root,
    #from_=0,
    #to=30,
    values=(5,10,15,20),
    textvariable=initial_value,
    wrap=False
)
spin_box.pack()

print(spin_box.get())

root.mainloop()