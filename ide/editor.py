import tkinter as tk
from tkinter import filedialog, messagebox
from documents import Document


class EditorView:
    """Creates and manages the visual components of the editor."""

    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.title("Colter's IDE")

        # Frames
        self.title_frame = tk.Frame(root, bg="lightblue")
        self.title_frame.pack(side="top", fill="x")

        self.text_frame = tk.Frame(root)
        self.text_frame.pack(side="top", fill="both", expand=True)

        # Title
        tk.Label(self.title_frame, text="Colter's IDE").pack(side="left")

        # Text area
        self.text_area = tk.Text(self.text_frame, undo=True)
        self.text_area.pack(expand=True, fill="both")

    def create_menus(self, controller):
        """Creates menus and connects them to controller methods."""

        menubar = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)

        file_menu.add_command(label="New File", command=controller.new_file)
        file_menu.add_command(label="Open...", command=controller.open_file)
        file_menu.add_command(label="Save", command=controller.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=controller.exit_ide)

        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        edit_menu.add_command(
            label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>")
        )
        edit_menu.add_command(
            label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>")
        )
        edit_menu.add_command(
            label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>")
        )
        edit_menu.add_command(label="Select All", command=controller.select_all)

        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)

        help_menu.add_command(
            label="About Tk",
            command=lambda: messagebox.showinfo("About", "Colter's IDE"),
        )

        self.root.config(menu=menubar)


class EditorController:
    """Handles user actions and file operations."""

    def __init__(self, root, view):
        self.root = root
        self.view = view
        self.document = Document()  # creating document object

        # Keyboard shortcuts
        self.root.bind("<Control-q>", self.exit_ide)
        self.root.bind("<Control-s>", self.save_file)
        self.root.bind("<Control-n>", self.new_file)
        self.root.bind("<Control-o>", self.open_file)

        self.root.protocol("WM_DELETE_WINDOW", self.exit_ide)

    def save_file(self, event=None):

        file_path = self.document.file_path

        if file_path is None:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            )

        if not file_path:
            return False

        try:
            # Get text from the GUI
            self.document.content = self.view.text_area.get("1.0", "end-1c")

            # Save using the Document class
            self.document.save(file_path)

            self.view.text_area.edit_modified(False)
            self.root.title(f"{file_path} - Colter's IDE")

            return True

        except OSError as error:
            messagebox.showerror("Error", f"Could not save file: {error}")
            return False

    def open_file(self, event=None):
        if not self.prompt_save_changes():
            return

        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if not file_path:
            return

        try:
            # Read file using Document
            self.document = Document()
            self.document.load(file_path)

            # Display document contents in GUI
            self.view.text_area.delete("1.0", "end")
            self.view.text_area.insert("1.0", self.document.content)

            self.view.text_area.edit_modified(False)
            self.root.title(f"{file_path} - Colter's IDE")

        except (OSError, UnicodeError) as error:
            messagebox.showerror("Error", f"Could not open file: {error}")

    def new_file(self, event=None):
        if not self.prompt_save_changes():
            return
        self.document = Document()
        self.view.text_area.delete("1.0", "end")
        self.view.text_area.edit_modified(False)
        self.root.title("Untitled - Colter's IDE")

    def prompt_save_changes(self):
        """Returns True if it is safe to continue, False if canceled."""

        if not self.view.text_area.edit_modified():
            return True

        answer = messagebox.askyesnocancel(
            title="Save File", message="You have unsaved changes. Save them?"
        )

        if answer is None:
            return False

        if answer:
            return self.save_file()

        return True

    def select_all(self):
        self.view.text_area.tag_add("sel", "1.0", "end-1c")
        self.view.text_area.mark_set("insert", "1.0")
        self.view.text_area.see("insert")

    def exit_ide(self, event=None):
        if self.prompt_save_changes():
            self.root.destroy()


class TextEditor:
    """Coordinates the editor components and starts the application."""

    def __init__(self, root):
        self.root = root

        self.view = EditorView(root)
        self.controller = EditorController(root, self.view)

        self.view.create_menus(self.controller)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    editor.run()
