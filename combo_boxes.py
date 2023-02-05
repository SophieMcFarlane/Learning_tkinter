import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Example")

selected_weekday = tk.StringVar()
weekday = ttk.Combobox(root, textvariable=selected_weekday)
weekday["values"] = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
weekday["state"] = "readonly"
weekday.pack()

def handle_selection(event):
    print("Today is ", selected_weekday.get())
    print("But we're gonna change it to Friday.")
    selected_weekday.set("Friday")
    print(weekday.current())

#When something is selected, run the handle_selection function
weekday.bind("<<comboboxSelected>>", handle_selection)

root.mainloop()

print(selected_weekday.get(), "was selected")