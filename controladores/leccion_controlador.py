from modelos.leccion import Leccion


class Leccion_controlador:
    def __init__(self):
        try:
            self.detalle = Leccion()
        except Exception as e:
            raise e


    def buscar_leccion(self,clase_num, leccion_orden): 
        try:   
            return self.detalle.buscar(clase_num, leccion_orden)
        except Exception as e:
            raise e



