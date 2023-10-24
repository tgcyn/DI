import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO
from cell import Cell
from detail_window import Detail_window

class MainWindow:
    def on_button_click(self, cell):
        root = tk.Toplevel()
        detail_window = Detail_window(root, cell.title, cell.path, cell.description)

    def on_button_clicked(self):
        mensaje = "Este programa ha sido escrito en python" #este es el mensaje q se va a mostrar al abrir la ventana con el message box
        messagebox.showinfo("Acerca del desarrollador", mensaje) #al tener una coma, la primero va a ser el nombre de la ventana y lo segundo el mensaje q se mostrara el ella

    def __init__(self, root, json_data):
        self.root = root
        root.title("Listado")
            
            #ajustar la posición de la ventana al centro
        anchura=150
        altura=230
        self.root.geometry(f"{anchura}x{altura}")
        x = (self.root.winfo_screenwidth() - anchura)/2
        y = (self.root.winfo_screenheight() - altura)/2
        self.root.geometry(f"+{int(x)}+{int(y)}")

            #crear un menu 
        barra_menus = tk.Menu() #instancio q va a haber un menu
       
        menu_archivo = tk.Menu(barra_menus, tearoff=False) #esto va a ser cada uno de los elementos q van a aparecer en el menu
        menu_archivo.add_command(label="Acerca de", command=self.on_button_clicked) #aqui le asigno el valor y lo q va a hacer el elemento
        
        barra_menus.add_cascade(menu=menu_archivo, label="Ayuda") #le doy al menu un nombre y le añado el elemento escrito anteriormente
        root.config(menu=barra_menus) #esto hace q se visualice dicho menu
        
            #visualizar las imagenes
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
