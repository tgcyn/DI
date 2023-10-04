from tkinter import Tk, ttk

class WindowYes:
    def __init__(self, root):
        self.root = root
        root.title("CASILLA SI")

        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.label = ttk.Label(self.frame, text="Felicidades")
        self.label.pack()
