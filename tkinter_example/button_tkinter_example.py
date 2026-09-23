import tkinter as tk


def say_hello():
    label.config(text="You clicked the button!")


# Setting it up
root = tk.Tk()
root.title("Button Example")

# Making a label
label = tk.Label(root, text="Click it")
label.pack(padx=20, pady=10)

# Making a Button
button = tk.Button(root, text="click me now", command=say_hello)
button.pack(pady=10)

root.mainloop()
