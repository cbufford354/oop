import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from time import strftime
from tkinter import filedialog, messagebox


class Text_editor:
    def __init__(self, root):
        # set up the frames
        self.root = root
        self.root.geometry("600x400")
        self.root.title("Colter's IDE")
        self.set_bindings()

        self.title_frame = tk.Frame(bg="lightblue")
        self.title_frame.pack(side="top", fill="x")

        self.text_frame = tk.Frame(bg="red")
        self.text_frame.pack(side="top", fill="both", expand=True)

        tk.Label(self.title_frame, text="Colter's IDE").pack(side="left")
        tk.Button(self.title_frame, text="File").pack(side="left")

        tk.Button(self.text_frame, text="text here").pack()

        # write text to the text area
        self.text_area = tk.Text(self.text_frame)
        self.text_area.pack(expand=1, fill="both")

        text = "This is a trial text"
        self.text_area.insert(tk.END, text)

        # create menu bar
        self.menubar = Menu(self.root)

        # Adding File Menu and commands
        self.file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.file)
        self.file.add_command(label="New File", command=self.new_file)
        self.file.add_command(label="Open...", command=self.open_file)
        self.file.add_command(label="Save", command=self.save_file)
        self.file.add_separator()
        self.file.add_command(label="Exit", command=self.exit_ide)

        # Adding Edit Menu and commands
        self.edit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=self.edit)
        self.edit.add_command(label="Cut", command=None)
        self.edit.add_command(label="Copy", command=None)
        self.edit.add_command(label="Paste", command=None)
        self.edit.add_command(label="Select All", command=None)
        self.edit.add_separator()
        self.edit.add_command(label="Find...", command=None)
        self.edit.add_command(label="Find again", command=None)

        # Adding Help Menu
        self.help_ = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.help_)
        self.help_.add_command(label="Tk Help", command=None)
        self.help_.add_command(label="Demo", command=None)
        self.help_.add_separator()
        self.help_.add_command(label="About Tk", command=None)

        # display Menu
        self.root.config(menu=self.menubar)

    # commands
    def save_file(self, event=None):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))
                messagebox.showinfo("Saved", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")

    def open_file(self, event=None):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    self.text_area.delete("1.0", tk.END)  # Clear the Text widget
                    self.text_area.insert(tk.END, file.read())  # Insert file content
            except Exception as e:
                messagebox.showerror("can't open file smh")

    def new_file(self, event=None):
        # maybe implement save file before making new file later !!
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if file_path:
            try:
                with open(file_path, "w") as file:
                    pass  # create new file
            except Exception as e:
                messagebox.showerror("couldn't create new file")

    # make label where whichever file is open is on text_are!!!!

    def exit_ide(self, event=None):
        self.root.destroy()

    # keyboard bindings
    def set_bindings(self):
        self.root.bind("<Control-q>", self.exit_ide)
        self.root.bind("<Control-s>", self.save_file)
        self.root.bind("<Control-n>", self.new_file)
        self.root.bind("<Control-o>", self.open_file)


if __name__ == "__main__":
    root = tk.Tk()
    ide = Text_editor(root)
    root.mainloop()
