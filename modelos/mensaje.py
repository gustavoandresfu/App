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
class Mensaje:

    def __init__(self, id=None, texto=None, media=None):
        self.id = id
        self.texto = texto
        self.media = media
        self.modelo = Modelo()

   
    def buscar(self,mensaje):

        try:
            connection = self.modelo.conectar()
            cursor = connection.cursor()
            query = """SELECT texto, media FROM mensajes  WHERE Id = %s;"""
            cursor.execute(query, (mensaje,))
            mensaje_datos = cursor.fetchone()

            if mensaje_datos:
                self.texto = mensaje_datos[0]
                self.media = mensaje_datos[1]
                return self
            return None
   
        except Exception as e:
            raise e
        finally:
            if connection:
                connection.close()      
