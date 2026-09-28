import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from time import strftime
from tkinter import filedialog, messagebox


class Text_editor:
    def __init__(self):
        # set up the frames
        self.root = root
        self.root.geometry("600x400")
        self.root.title("Colter's IDE")

        self.title_frame = tk.Frame(bg="lightblue")
        title_frame.pack(side="top", fill="x")

        self.text_frame = tk.Frame(bg="red")
        self.text_frame.pack(side="top", fill="both", expand=True)

        tk.Label(self.title_frame, text="Colter's IDE").pack(side="left")
        tk.Button(self.title_frame, text="File").pack(side="left")

        tk.Button(self.text_frame, text="text here").pack()

        # write text to the text area
        self.text_area = tk.Text(self.text_frame)
        text_area.pack(expand=1, fill="both")

        text = "This is a trial text"
        self.text_area.insert(tk.END, text)

        # create menu bar
        self.menubar = Menu(self.root)

        # Adding File Menu and commands
        self.file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(
            label="File", menu=file
        )  # adding file menue to menubar under root
        self.file.add_command(label="New File", command=None)
        self.file.add_command(label="Open...", command=None)
        self.file.add_command(
            label="Save", command=save_file
        )  # dont include parenthesis or it will auto run
        self.file.add_separator()
        self.file.add_command(label="Exit", command=root.destroy)

        # Adding Edit Menu and commands
        self.edit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=edit)
        self.edit.add_command(label="Cut", command=None)
        self.edit.add_command(label="Copy", command=None)
        self.edit.add_command(label="Paste", command=None)
        self.edit.add_command(label="Select All", command=None)
        self.edit.add_separator()
        self.edit.add_command(label="Find...", command=None)
        self.edit.add_command(label="Find again", command=None)

        # Adding Help Menu
        self.help_ = Menu(self.menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_)
        self.help_.add_command(label="Tk Help", command=None)
        self.help_.add_command(label="Demo", command=None)
        self.help_.add_separator()
        self.help_.add_command(label="About Tk", command=None)

        # display Menu
        self.root.config(menu=menubar)

        # commands
        def save_file():
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            )
            if file_path:
                try:
                    with open(file_path, "w") as file:
                        file.write(text_area.get(1.0, tk.END))
                    messagebox.showinfo("Saved", "File saved successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Could not save file: {e}")


if __name__ == "__main__":
    root.mainloop()
    root = tk.Tk()
    ide = Text_editor(root)
