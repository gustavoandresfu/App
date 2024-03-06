from modelos.usuario import Usuario
from modelos.progreso import Progreso
from vistas.progreso_vista import Progreso_vista

class Progreso_controlador:
        
    def __init__(self):
        pass

    def mostrar(self,usuario):  

        self.model = Progreso()
        self.view = Progreso_vista(self.progreso_clase(usuario), self.progreso_practica(usuario))

    def guardar(self, usuario, clase, leccion):
        
        self.model = Progreso()
        return self.model.guardar(usuario,clase, leccion)
    
    def progreso_clase(self, usuario):

        self.model = Progreso()
        return self.model.buscar_progreso_clases(usuario)
    
    def progreso_practica(self, usuario):
        self.model = Progreso()
        return self.model.buscar_progreso_practicas(usuario)