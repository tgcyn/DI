import tkinter as tk
from PIL import Image, ImageTk

class Detail_window:
    def __init__(self, root, title, path, description):
        self.root = root
        
        #para q dentro de la ventana emergente se visualice el título
        self.title = tk.Label(root, text=title) #creo un Label q contenga el titulo q le haya dado a la celda, en este caso Libro + nº
        self.title.pack()

        #para q dentro de la ventana emergente se visualice la imagen
        self.path = tk.Label(root, image=path) #creo un Label q contenga la imagen del libro
        self.path.pack()
        
        #para q dentro de la ventana emergente se visualice la descipción
        self.description = tk.Label(root, text=description) #creo un texto q contenga la descrición del libro
        self.description.pack()
        
        root.title(title)

        




