import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO
from cell import Cell
from detail_window import Detail_window

class MainWindow:
    def __init__(self, root, json_data):
        self.root = root
        root.title("Listado")

        for dato in enumerate(json_data):
            #extraigo los datos de cada JSONObject 
            nombre = dato.get("name")
            descripcion = dato.get("description")
                #estos dos pasos son para "descargar" la imagen y no enviarla como un url
            url = dato.get("image_url")
            foto = load_image_from_url(url)

            #creo una celda para cada dato(object) a la q le envio los datos
            dato = Cell(nombre, foto, descripcion)
          # detail_window = Detail_window(root, dato.title, dato.path, dato.description)
            
def load_image_from_url(self,url):
    response = requests.get(url)
    img_data = Image.open(BytesIO(response.content))
    img = ImageTk.PhotoImage(img_data)  
    return img



 
