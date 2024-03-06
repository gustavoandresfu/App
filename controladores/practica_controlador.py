from modelos.clase import Clase
from vistas.practica_vista import Practica_vista

class Practica_controlador:
    def __init__(self, usuario):
      
        self.model = Clase()
        obj_clase = self.model.buscar_clase_practica()
        self.view = Practica_vista(obj_clase, usuario)



