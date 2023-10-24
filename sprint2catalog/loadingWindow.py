import tkinter as tk
import threading
import requests
from window import MainWindow


class loadingWindow:
    def __init__(self,root):
        self.finished = False
        self.root = root
        self.root.title("Cargando...")
        
        #ajustar posición de la ventana al centro y darle unas dimensiones
            #los screen dan las dimensiones de la pantalla
            #los req dan las dimensiones de la ventana
        anchura=170
        altura=120
        self.root.geometry(f"{anchura}x{altura}") #esto es para darle unas dimensiones fijas a la pantalla
        x = (self.root.winfo_screenwidth() - anchura)/2
        y = (self.root.winfo_screenheight() - altura)/2
        self.root.geometry(f"+{int(x)}+{int(y)}") #con la f indicamos q lo q esta entre llaves se va a tomar por el valor de la variable
        self.root.resizable(False, False) #esto impide q se pueda redimensionar la ventana

        #añado un texto para indicar q estoy haciendo
        self.label = tk.Label(self.root, text="Cargando datos...", font=("Arial", 14)) #con font le doy una fuente y un tamaño especificos
        self.label.pack(side=tk.TOP, pady=10)
    
        #permite obtener el valor de una opcion pasada al widget, en este caso el color de fondo
        label_bg_color = self.label.cget("bg") 

        #con esto creo la circunferencia, le asigno un tamaño concreto y el color q extraigo con cget
        self.canvas = tk.Canvas(self.root, width=60, bg=label_bg_color)
        self.canvas.pack()

        #con los siguientes pasos vamos a dibujar la circunferencia
        self.progress = 0
        self.draw_progress_circle(self.progress)
        self.update_progress_circle()

        #creo un hilo secundario para hacer la peticion de red
        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()
        if self.thread.is_alive():
            self.check_Thread()



#ESTAS DOS FUNCIONES SIRVEN PARA DIBUJAR LA CIRCUNFERENCIA E IR VIENDO SU EVOLUCION
    def draw_progress_circle(self, progress):
        self.canvas.delete("progress") #con esto eliminamos el elemento asociado q este asociado, en este caso progress
        angle = int(360 * (progress/100))

        #con esto dibujamos el arco de la circunferencia
            #los numeros son las coordenadas del cuadrado q contiene a la circunferencia, siendo las dos primeras las del punto superior izquierdo, y los otras las del punto inferior derecho 
            #start es el punto en el q empieza a dibujarse
            #extent indica el tramo de circunferencia q se va a visualizar cada vez, en este caso le hemos asignado un valor con la variable angle calculada más arriba
            #tags es el nombre q le damos a la figura
            #tk.ARC indica q es una circunferencia y no un circulo
        self.canvas.create_arc(10, 10, 35, 35, 
                                start=0, extent=angle, tags="progress", outline='green', width=4, style=tk.ARC)
                                
    def update_progress_circle(self):
        if self.progress<90:
            self.progress += 10
        else:
            if self.progress>89 and self.progress<=100: #con esto ralentizo el tiempo del ultimo tramo de la circunferencia
                self.progress += 1 #le asigno q el progreso sea de 1 en 1 
            else:
                self.progress = 0

        self.draw_progress_circle(self.progress)
        self.root.after(100, self.update_progress_circle) #vuelve a llamar a la funcion especificada cada los milisegundos especificados (100 y update_progress_circle en este caso)
    

#AQUI LANZO EL HILO SECUNDARIO
    #con esto envio el contenido del json a una ventana emerjente 
    def fetch_json_data(self):
        response = requests.get("https://raw.githubusercontent.com/tgcyn/DI/main/recursos/catalog.json")
        if response.status_code == 200:
            self.json_data = response.json()
            self.finished = True
    
    def check_Thread(self):
        if self.finished:
            self.root.destroy()
            launch_main_window(self.json_data)
        else:
            self.root.after(100, self.check_Thread)
    
    #con esto creo dicha ventana
def launch_main_window(json_data):
    root = tk.Tk()
    app = MainWindow(root,json_data)
    root.mainloop()

