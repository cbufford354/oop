import tkinter as tk


def key_pressed(event):
    print(event.keysym)
    status.config(text=f"Youp pressed:{event.keysym}")


root = tk.Tk()
root.title = "Event Loop"

status = tk.Label(root, text="Pres a key", font=("Arial", 18))
status.pack(padx=30, pady=30)

root.bind("<Key>", key_pressed)

root.mainloop()
