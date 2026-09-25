import tkinter as tk


class Text_file:
    def __init__(self):
        pass


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

text_area = tk.Text(text_frame)
text_area.pack(expand=1, fill="both")

# write text to the text area
text = "This is a trial text"
text_area.insert(tk.END, text)
root.mainloop()
