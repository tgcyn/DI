import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO
from cell import Cell
from detail_window import Detail_window

class MainWindow:
    def on_button_click(self, cell):
        root = tk.Toplevel()
        detail_window = Detail_window(root, cell.title, cell.path, cell.description)

    def __init__(self, root, json_data):
        self.root = root
        root.title("Listado")
        self.datos = [] #creo una lista para ir guardando las celdas

        for dato in json_data:
            #extraigo los datos de cada JSONObject 
            nombre = dato.get("name")
            descripcion = dato.get("description")
                #estos dos pasos son para "descargar" la imagen y no enviarla como un url
            url = dato.get("image_url")
            foto = load_image_from_url(self, url)
            
            #creo una celda para cada dato(object) y la incluyo en una lista
            self.datos.append(Cell(nombre, foto, descripcion))
            
        for i, cell in enumerate(self.datos):
            label = tk.Label(root, image= cell.path, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0) 
            label.bind("<Button-1>", lambda event, celda = cell: self.on_button_click(celda))

def load_image_from_url(self, url):
    response = requests.get(url)
    img_data = Image.open(BytesIO(response.content))
    img = ImageTk.PhotoImage(img_data)  
    return img
