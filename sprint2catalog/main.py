from tkinter import Tk
from loadingWindow import loadingWindow, launch_main_window

if __name__ == "__main__":
    root = Tk()
    app = loadingWindow(root)
    root.mainloop()