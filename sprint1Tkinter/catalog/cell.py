import tkinter as tk
from PIL import Image, ImageTk

class Cell:
    def __init__(self, title, path): #a cada celda telgo q enviarle dos valores
        self.title = title #el primero q va a ser el nombre con el q identifico a la imagen
        self.path = path #el segundo q es la ruta de donde tengo guardada la imagen
        
        img = Image.open(self.path) #le asigno a una variable la imagen original
        img_red = img.resize((100,100),Image.Resampling.LANCZOS) #creo una segunda variable para guardar la imagen redimensionada

        self.image_tk = ImageTk.PhotoImage(img_red) #le asigno a image.tk (q es la imagen q se muestra) la imagen redimensionada