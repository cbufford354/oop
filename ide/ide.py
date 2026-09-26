import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from time import strftime

# set up the frames
root = tk.Tk()
root.geometry("600x400")
root.title("Colter's IDE")

title_frame = tk.Frame(root, bg="lightblue")
title_frame.pack(side="top", fill="x")

text_frame = tk.Frame(root, bg="red")
text_frame.pack(side="top", fill="both", expand=True)


tk.Label(title_frame, text="Colter's IDE").pack(side="left")
tk.Button(title_frame, text="File").pack(side="left")

tk.Button(text_frame, text="text here").pack()

# write text to the text area
text_area = tk.Text(text_frame)
text_area.pack(expand=1, fill="both")

text = "This is a trial text"
text_area.insert(tk.END, text)

# create menu bar
menubar = Menu(root)

# Adding File Menu and commands
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file)
file.add_command(label="New File", command=None)
file.add_command(label="Open...", command=None)
file.add_command(label="Save", command=None)
file.add_separator()
file.add_command(label="Exit", command=root.destroy)

# Adding Edit Menu and commands
edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Cut", command=None)
edit.add_command(label="Copy", command=None)
edit.add_command(label="Paste", command=None)
edit.add_command(label="Select All", command=None)
edit.add_separator()
edit.add_command(label="Find...", command=None)
edit.add_command(label="Find again", command=None)

# Adding Help Menu
help_ = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_)
help_.add_command(label="Tk Help", command=None)
help_.add_command(label="Demo", command=None)
help_.add_separator()
help_.add_command(label="About Tk", command=None)

# display Menu
root.config(menu=menubar)


root.mainloop()
