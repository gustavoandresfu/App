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
class Plantilla:
    
    def __init__(self, id=None, id_plantilla=None,nota=None,color=None,
                 posicion_x=None, posicion_y=None,origen=None):
        self.id = id
        self.id_plantilla=id_plantilla
        self.nota=nota
        self.color=color
        self.posicion_x=posicion_x
        self.posicion_y=posicion_y
        self.origen = origen
        self.modelo = Modelo()
        self.plantilla_detalles = []


    def buscar(self,plantilla):

        try:
            connection = self.modelo.conectar()
            cursor = connection.cursor()
            query = """SELECT Nombre_latino as nota, color_nota as color, posicion_x, posicion_y,Origen
                        FROM plantillas p 
                        INNER JOIN plantilla_detalle pd
                        ON p.Id  = pd.id_plantilla 
                        INNER JOIN notas n 
                        ON pd.nota  = n.Id 
                        WHERE p.Id = %s;"""
            cursor.execute(query, (plantilla,))
            plantilla_detalle_data = cursor.fetchall()


            for plantilla_detalle_item in plantilla_detalle_data:
                nota,color,posicion_x, posicion_y, origen = plantilla_detalle_item
                plantilla = Plantilla(None, None,nota,color,posicion_x, posicion_y, origen)
                self.plantilla_detalles.append(plantilla)
   
            return self.plantilla_detalles

        except Exception as e:
            raise e

        finally:
            if connection:
                connection.close() 

