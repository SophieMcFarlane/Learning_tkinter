import tkinter as tk
from tkinter import ttk

def greet():
    print(f"Hello, {user_name.get() or 'World'}")

#Root window 
root = tk.Tk()
root.title("Greeter")
root.columnconfigure(0, weight=1)
#Makes window a fixed size
#root.geometry("600x400")
#pack puts the label into the parent
#creates variable for entry field
user_name = tk.StringVar()

input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.grid(row=0, column=0, sticky="EW")

name_label = ttk.Label(input_frame, text="Name: ")
name_label.grid(row=0, column=0,padx=(0, 10))
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
name_entry.grid(row=0, column=1)
#So we can type name straight away 
name_entry.focus()

buttons = ttk.Frame(root, padding=(20, 10))
#Makes both column have same weight so both buttons take up 50% of the space
buttons.columnconfigure(0, weight=1)
buttons.columnconfigure(1, weight=1)
#Sticky tells the button where to stick to, EW means east and west so left and right
buttons.grid(row=1, column=0,sticky="EW")

greet_button = ttk.Button(buttons, text="Greet", command=greet)
#default is side=top, left will anchor it to the left so buttons are side by side
#fill=y makes button uses all vertical space that has been reserved for it 
#expand asks window for more space, so will expand when you expand the whole window 
greet_button.grid(row=0, column=0, sticky="EW")

quit_button = ttk.Button(buttons, text="Quit", command=root.destroy)
quit_button.grid(row=0, column=1, sticky="EW")

#Pauses python whilst tkinters event loop runs 
root.mainloop()