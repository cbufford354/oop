import tkinter as tk


class CounterApp:
    def __init__(self, root):
        self.count = 0

        self.label = tk.Label(root, text="0")
        self.label.pack()

        tk.Button(root, text="Increment", command=self.increment).pack()

    def increment(self):
        self.count += 1
        self.label["text"] = self.count


root = tk.Tk()
CounterApp(root)

root.mainloop()
