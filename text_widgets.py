import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widgets Example")

text=tk.Text(root, height=8)
text.pack()

#1.0 is the position you want to enter the text, 1st line on the 0th character
text.insert("1.0", "Please enter a comment...")
text["state"] = "normal" #"disabled"

text_context = text.get("1.0", "end")
print(text_context)

root.mainloop()