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
class Clase:

    def __init__(self, id=None, orden=None, tipo=None, nombre=None, descripcion=None, 
                 creador=None, fecha_alta=None, fecha_mod=None, lecciones=None):
        
        self.id = id
        self.orden = orden
        self.tipo = tipo
        self.nombre = nombre
        self.descripcion = descripcion
        self.creador = creador
        self.fecha_alta = fecha_alta
        self.fecha_mod = fecha_mod
        self.leccion = lecciones
        self.modelo = Modelo()

    def buscar(self):
        try:
            conexion= self.modelo.conectar()
            cursor = conexion.cursor()
            query = """SELECT Id, Orden, Nombre, Descripcion FROM clases 
                       order by orden LIMIT 1;"""
            cursor.execute(query,)
            clase_datos = cursor.fetchone()
            cursor.close()

            if clase_datos:
                self.id = clase_datos[0]
                self.orden = clase_datos[1]
                self.nombre = clase_datos[2]
                self.descripcion = clase_datos[3]
                return self
            return None
        except Exception as e:
            raise e
        finally:
            if conexion:
                conexion.close()

    def buscar_clase_practica(self):
        try:
            conexion= self.modelo.conectar()
            cursor = conexion.cursor()
            query = """SELECT Id, Orden, Nombre, Descripcion FROM clases WHERE
                       tipo = 2 order by orden LIMIT 1;"""
            cursor.execute(query,)
            clase_datos = cursor.fetchone()
            cursor.close()

            if clase_datos:
                # Crear una instancia de la clase y asignar los datos recuperados
                self.id = clase_datos[0]
                self.orden = clase_datos[1]
                self.nombre = clase_datos[2]
                self.descripcion = clase_datos[3]
                return self
            return None

        except Exception as e:
            raise e
        
        finally:
            if conexion:
                conexion.close()            

    
