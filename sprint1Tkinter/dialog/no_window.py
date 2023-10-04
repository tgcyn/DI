from tkinter import Tk, ttk

class WindowNo:
    def __init__(self, root):
        self.root = root
        root.title("CASILLA NO")

        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.label = ttk.Label(self.frame, text="Eres raro")
        self.label.pack()