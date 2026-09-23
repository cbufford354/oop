import tkinter as tk


def submit():
    result["text"] = f"Hello, {name.get()}!"


root = tk.Tk()

tk.Label(root, text="Name:").grid(row=0, column=0)

name = tk.Entry(root)
name.grid(row=0, column=1)

tk.Button(root, text="Submit", command=submit).grid(row=1, column=0, columnspan=2)

result = tk.Label(root)

result.grid(row=2, column=0, columnspan=2)

root.mainloop()
