import tkinter as tk


def greet():
    name = name_var.get()
    message_var.set(f"Hello,{name}")


root = tk.Tk()
root.title("Greeting")

name_var = tk.StringVar()
message_var = tk.StringVar(value="enter your name")

# pack() it al in there!
tk.Label(root, text="Name:").pack()
tk.Entry(root, textvariable=name_var).pack()
tk.Button(root, text="Greet", command=greet).pack()
tk.Label(root, textvariable=message_var).pack()

root.mainloop()
