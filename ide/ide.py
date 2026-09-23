import tkinter as tk


class Text_file:
    def __init__(self):
        pass


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


root.mainloop()
