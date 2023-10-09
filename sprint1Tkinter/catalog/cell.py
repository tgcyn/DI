import tkinter as tk
from PIL import Image, ImageTk

class Cell:
    def __init__(self, title, path): #a cada celda telgo q enviarle dos valores
        self.title = title #el primero q va a ser el nombre con el q identifico a la imagen
        self.path = path #el segundo q es la ruta de donde tengo guardada la imagen
        self.image_tk = ImageTk.PhotoImage(file = self.path)

        
