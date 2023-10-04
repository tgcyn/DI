from tkinter import Tk, ttk, Button
from yes_window import WindowYes
from no_window import WindowNo

class MainWindow:
    def on_button_click(self):
        pass

    def WY(self): #las funciones siempre reciben en argumento self como mínimo 
        rootYes = Tk() #esto abre una ventana emerjente 
        button1 = WindowYes(rootYes) #esto hace q en esa ventana se visualice el contenido de WindowYes de la clase yes_window
        rootYes.mainloop()
    
    def WN(self): #igual q WN pero con WindowNo
        rootNo = Tk()
        button2 = WindowNo(rootNo)
        rootNo.mainloop()


    def __init__(self,root):
        self.root = root #sirve para conectar lo q suceda en esta pantalla con aquella q lo invoco
        root.title("Casillas S/N")

        self.frame = ttk.Frame(self.root) #es necesario hacer esto para cualquier texto
        self.frame.pack()

        self.label = ttk.Label(self.frame, text="Te gusta el helado") #con label hago que se visualice el texto q deseo, en este caso la pregunta
        self.label.pack()

        self.button1 = ttk.Button(self.frame, text="Si", command=self.WY) #hago q se visualice un primer boton con el mensaje "Si" y con command hago q ejecute la funcion WY
        self.button1.pack(side="left", fill="x", expand=True, anchor="nw")

        self.button2 = ttk.Button(self.frame, text="No", command=self.WN) #hago q se visualice un segundo boton igual q el anterior pero con "No" y WN
        self.button2.pack(side="right", fill="y", expand=True, anchor="nw")

    



