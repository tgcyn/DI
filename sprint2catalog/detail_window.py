import tkinter as tk

class Detail_window:
    def __init__(self, root, title, path, description):
        self.root = root
        root.title("Información")

        #ajustar la posición de la ventana al centro
        anchura = 800
        altura = 150
        self.root.geometry(f"{anchura}x{altura}")
        x = (self.root.winfo_screenwidth() - anchura)/2
        y = (self.root.winfo_screenheight() - altura)/2
        self.root.geometry(f"+{int(x)}+{int(y)}")
       
        
        #para q dentro de la ventana emergente se visualice el título
        self.title = tk.Label(root, text=title)
        self.title.pack()

        #para q dentro de la ventana emergente se visualice la descipción
        self.description = tk.Label(root, text=description) 
        self.description.pack()
        
        #para q dentro de la ventana emergente se visualice la imagen
        self.path = tk.Label(root, image=path) 
        self.path.pack()

       

        




