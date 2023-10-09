import tkinter as tk
from cell import Cell
from tkinter import messagebox

class MainWindow:
    def on_button_click(self, cell):
        message = "Has hecho click en la celda " + cell.title #importo el nombre de la imagen con cell.title
        messagebox.showinfo("Información", message) #para mostrar el mensaje cnd clico en cada celda

    def __init__(self,root):
        root.title("Imágenes")

        self.cells = [ #tal y como defini en cell, el primer parametro es el nombre de la imagen, el segundo la ruta 
            Cell("Libro 1", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\edited\\cazadores.jpg"), #cada celda es un elemento de la lista
            Cell("Libro 2", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\edited\\ecdl.jpg"),
            Cell("Libro 3", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\edited\\harry potter.jpg"),
            Cell("Libro 4", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\edited\\ljdh.jpg"),
            Cell("Libro 5", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\edited\\percy jackson.jpg")
        ]

        for i, cell in enumerate(self.cells): #para cada elemento i de la lista self.cells 
            label = tk.Label(root, image= cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0) #asigno un lugar en la matriz (fila i, columna 0)
            label.bind("<Button-1>", lambda event, celda = cell: self.on_button_click(celda))
