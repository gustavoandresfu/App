from modelos.clase import Clase
from vistas.clase_vista import Clase_vista

class Clase_controlador:
    def __init__(self, usuario):
      
        try:
            
            self.model = Clase()
            obj_clase = self.model.buscar()
            self.view = Clase_vista(obj_clase, usuario)
            
        except Exception as e:
            raise e    



