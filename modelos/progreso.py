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




