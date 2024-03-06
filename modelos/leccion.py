from modelos.modelo import Modelo
from modelos.plantilla import Plantilla
from modelos.secuencia import Secuencia
from modelos.mensaje import Mensaje


class Leccion():

    def __init__(self, id=None, orden=None, clase=None, mensaje=None,
                  creador=None, plantilla=None,fecha_alta=None, fecha_mod=None):
        self.id = id
        self.orden = orden
        self.clase = clase
        self.creador = creador
        self.secuencia = Secuencia()
        self.plantilla = Plantilla()
        self.mensaje = Mensaje()
        self.plantilla_detalle = []
        self.secuencia_detalle = []
        self.fecha_alta = fecha_alta
        self.fecha_mod = fecha_mod
        self.modelo = Modelo()


    def buscar(self, clase, orden_leccion):
        try:
            conexion= self.modelo.conectar()
            cursor = conexion.cursor()
            query = """SELECT Id,Clase,Plantilla,Orden,Mensaje,Creador,Fecha_alta,Fecha_mov FROM lecciones
                       WHERE Clase = %s and orden = %s;"""
            cursor.execute(query, (clase,orden_leccion,))
            clase_datos = cursor.fetchone()
            if clase_datos:
                self.id = clase_datos[0]
                self.clase = clase
                self.plantilla_detalle = self.plantilla.buscar(clase_datos[2])
                self.secuencia_detalle = self.secuencia.buscar(clase_datos[0])
                self.orden = clase_datos[3]
                self.mensaje = self.mensaje.buscar(clase_datos[4])
                self.creador = clase_datos[5]
                self.fecha_alta = clase_datos[6]
                self.fecha_mod = clase_datos[7]
                return self
            return None

        except Exception as e:
            raise e
        
        finally:
            if conexion:
                conexion.close() 
     

  