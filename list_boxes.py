import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("widget Example")

programming_languages = ("C", "Go", "Javascript", "Perl", "Python", "Java")

langs = tk.StringVar(value=programming_languages)
langs_select = tk.Listbox(root, listvariable=langs, height=6)
langs_select.pack()

def handle_selection_change(event):
    selected_indicies = langs_select.curselection()
    for i in selected_indicies:
        print(langs_select.get(i))


langs_select.bind("<<ListboxSelect>>", handle_selection_change)

root.mainloop()