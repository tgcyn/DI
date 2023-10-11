import tkinter as tk
from cell import Cell
from tkinter import messagebox
from detail_window import Detail_window

class MainWindow:
    def on_button_click(self, cell):
        root = tk.Toplevel()
        detail_window = Detail_window(root, cell.title, cell.image_tk, cell.description)

    def __init__(self, root):
        root.title("Imágenes")

        self.cells = [ #tal y como defini en cell, el primer parametro es el nombre de la imagen, el segundo la ruta 
            Cell("Libro 1", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\cazadores.jpg", "La historia nos transporta a un mundo secreto poblado por cazadores de sombras, seres mitad ángeles mitad humanos, que protegen a la humanidad de demonios y criaturas sobrenaturales."),
            Cell("Libro 2", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\ecdl.jpg", "La historia sigue a Thomas, quien despierta en un lugar llamado 'El Claro' sin recordar su pasado."),
            Cell("Libro 3", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\harry potter.jpg", "El huérfano Harry Potter descubre su verdadera herencia como mago el día de su undécimo cumpleaños."),
            Cell("Libro 4", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\ljdh.jpg", "Sigue a Katniss Everdeen, una valiente joven que se ofrece como tributo en lugar de su hermana menor en los brutales Juegos del Hambre."),
            Cell("Libro 5", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\percy jackson.jpg", "La historia sigue a Percy Jackson, un joven disléxico y con TDAH, quien descubre que es un semidiós, hijo de Poseidón.")
        ]

        for i, cell in enumerate(self.cells): #para cada elemento i de la lista self.cells 
            label = tk.Label(root, image= cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0) #asigno un lugar en la matriz (fila i, columna 0)
            label.bind("<Button-1>", lambda event, celda = cell: self.on_button_click(celda))
