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



