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
class Progreso:
    
    def __init__(self, id=None, usuario=None, leccion=None, fecha=None):
        self.id = id
        self.usuario = usuario
        self.leccion = leccion
        self.fecha = fecha
        self.modelo = Modelo()

    def buscar_progreso_clases(self, usuario):
        try:
            conectar = self.modelo.conectar()
            cursor = conectar.cursor()
            query = """
            SELECT (
                (SELECT count(a.usuario) FROM progreso a
                INNER JOIN clases b 
                ON a.Clase = b.Id
                WHERE b.Tipo = 1
                AND a.usuario = %s) 
                / 
                (SELECT COUNT(*) FROM clases where tipo = 1)
                ) * 100 as porcentaje_cumplimiento;
            """
            cursor.execute(query,(usuario,))
            result = cursor.fetchone()
            return result[0]
        
        except Exception as e:
            raise e

        finally:
            if conectar:
                conectar.close()

    def buscar_progreso_practicas(self, usuario):
        try:
            conectar = self.modelo.conectar()
            cursor = conectar.cursor()
            query = """
            SELECT (
                (SELECT count(a.usuario) FROM progreso a
                INNER JOIN clases b 
                ON a.Clase = b.Id
                WHERE b.Tipo = 2
                AND a.usuario = %s) 
                / 
                (SELECT COUNT(*) FROM clases a 
                 INNER JOIN lecciones b 
                ON a.Id = b.clase
                where a.tipo = 2)
                ) * 100 as porcentaje_cumplimiento;
            """
            cursor.execute(query,(usuario,))
            result = cursor.fetchone()
            return result[0]
        
        except Exception as e:
            raise e

        finally:
            if conectar:
                conectar.close()                
    
    def guardar(self, usuario, clase, leccion):
        try:
            conectar = self.modelo.conectar()
            cursor = conectar.cursor()
            select_query = """
            SELECT COUNT(*) 
            FROM progreso 
            WHERE usuario = %s AND clase = %s AND leccion = %s
            """
            select_valores = (usuario, clase, leccion)
            cursor.execute(select_query, select_valores)
            existe_registro = cursor.fetchone()[0]

            if existe_registro == 0:
                insert_query = """
                INSERT INTO progreso (usuario, clase, leccion)
                VALUES (%s, %s, %s)
                """
                insert_valores = (usuario, clase, leccion)
                cursor.execute(insert_query, insert_valores)
                conectar.commit()
                return True
            else:
                return False

        except Exception as e:
            raise e

        finally:
            if conectar:
                conectar.close()




