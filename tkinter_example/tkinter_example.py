import tkinter as tk  # need every time

root = tk.Tk()
root.title = "FOO BAR BAZ"
label = tk.Label(root, text="Hello World")
label.pack(padx=20, pady=20)

root.mainloop()  # need every time
