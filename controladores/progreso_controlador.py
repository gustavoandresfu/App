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