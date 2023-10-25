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
            

            #scrollbar
        self.canvas = tk.Canvas(self.root) #para crear el rectangulo en el q se veran las imagenes
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview) #con esto creamos la barra de desplazamiento y le damos una orientacion
        self.scrollable_frame = tk.Frame(self.canvas) #contenedor del canvas

        self.scrollable_frame.bind( #esto es para q cada vez q el frame cambie de tamaño, se actualiza la region de desplazamiento
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw") #coloca el frame dentro del canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set) #para q se actualice la barra de desplazamiento cnd se desplace el canvas 

      # for i, cell in enumerate(self.datos) es otra forma de ponerlo, pero NUNCA puedo tratar de operar sin indice (i) habiendo puesto un enumerate 
        for cell in self.datos: # ^ for cell in enumerate(self.datos) ESTÁ MAL
            self.add_item(cell)
                  
        self.canvas.grid(row=0, column=0, sticky="nsew") #coloca el canvas en la ventana principal y permite q se expanda con la ventana
        self.scrollbar.grid(row=0, column=1, sticky="ns") #coloca la barra de desplazamiento al lado del canvas, permite q se expanda en vertical

        self.root.grid_rowconfigure(0, weight=1) #la fila va a pesar 1 y permite q se redimensione con la ventana
        self.root.grid_columnconfigure(0, weight=1) #mismo q lo anterior pero con columna
    
    def add_item(self, cell): #este metodo permite visualizar las imagenes a la vez q las encapsula dentro del frame
        frame = tk.Frame(self.scrollable_frame)
        frame.pack(pady=10)

        label = tk.Label(frame, image=cell.path, text=cell.title, compound=tk.BOTTOM)
        label.grid(row=0, column=0) 
        label.bind("<Button-1>", lambda event, celda = cell: self.on_button_click(celda))


def load_image_from_url(self, url):
    response = requests.get(url)
    img_data = Image.open(BytesIO(response.content))
    img = ImageTk.PhotoImage(img_data)  
    return img
