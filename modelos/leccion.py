# MIT License
# 
# Copyright (c) 2024 Gustavo Futo
# 
# Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia
# de este software y de los archivos de documentación asociados (el "Software"), para
# tratar el Software sin restricciones, incluyendo sin limitación los derechos
# de uso, copia, modificación, fusión, publicación, distribución, sublicencia
# y/o venta de copias del Software, y para permitir a las personas a las que se les
# proporcione el Software a hacer lo mismo, sujeto a las siguientes condiciones:
# 
# El aviso de copyright anterior y este aviso de permisos se incluirán en
# todas las copias o partes sustanciales del Software.
# 
# EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O
# IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD,
# APTITUD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS
# TITULARES DEL COPYRIGHT O LOS AUTORES SERÁN RESPONSABLES DE NINGÚN RECLAMO,
# DAÑO U OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O CUALQUIER
# OTRA FORMA, DERIVADA DE, FUERA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U
# OTRAS NEGOCIACIONES EN EL SOFTWARE.

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
     

  