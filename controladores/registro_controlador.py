from modelos.usuario import Usuario
from vistas.registro_vista import Registro_vista

class Registro_controlador:
    def __init__(self, root):
        self.root = root
        self.model = Usuario()
        self.root.title("Registro")
        self.root.geometry("400x300") 
        self.root.resizable(False, False)  
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - self.root.winfo_width()) // 2
        y = (screen_height - self.root.winfo_height()) // 2
        self.root.geometry("+{}+{}".format(x, y))        
        self.root.iconbitmap("recursos/musicar.ico")  
        self.view = Registro_vista(root, self)


    def registrar(self, nombre, apellido, usuario, clave):
        return self.model.crear_usuario(nombre, apellido, usuario, clave)

    def run(self):
        self.root.mainloop()

