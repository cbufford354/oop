import tkinter as tk

root = tk.Tk()
root.title = "Calculator"
calc_label = tk.Label(root, text="Calculator")
calc_label.pack(padx=10, pady=10)

tk.Button(root).grid(row=1, column=0, columnspan=2)


root.mainloop()
