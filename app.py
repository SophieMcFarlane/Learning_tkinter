import tkinter as tk
from tkinter import ttk

def greet():
    print(f"Hello, {user_name.get() or 'World'}")

#Root window 
root = tk.Tk()
root.title("Greeter")
#Makes window a fixed size
#root.geometry("600x400")
#pack puts the label into the parent
#creates variable for entry field
user_name = tk.StringVar()

input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.pack(fill="both")

name_label = ttk.Label(input_frame, text="Name: ")
name_label.pack(side="left", padx=(0, 10))
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
name_entry.pack(side="left")
#So we can type name straight away 
name_entry.focus()

buttons = ttk.Frame(root, padding=(20, 10))
buttons.pack(fill="both")

greet_button = ttk.Button(buttons, text="Greet", command=greet)
#default is side=top, left will anchor it to the left so buttons are side by side
#fill=y makes button uses all vertical space that has been reserved for it 
#expand asks window for more space, so will expand when you expand the whole window 
greet_button.pack(side="left")

quit_button = ttk.Button(buttons, text="Quit", command=root.destroy)
quit_button.pack(side="right")

#Pauses python whilst tkinters event loop runs 
root.mainloop()