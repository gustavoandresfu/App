from modelos.modelo import Modelo
from modelos.nota import Nota
from modelos.tiempo import Tiempo
class Secuencia:

    def __init__(self, id=None, leccion=None, nota=None, tiempo=None):
        self.id = id
        self.leccion = leccion
        self.nota = nota
        self.tiempo = tiempo
        self.modelo = Modelo()

    def buscar(self, leccion):

        try:
            conn = self.modelo.conectar()
            cursor = conn.cursor()
            query = """SELECT a.id, a.Leccion,b.id as id_nota,b.Escala, b.Nombre_latino, b.Nombre_ingles, b.Origen,
                        c.id as id_tiempo,c.Tempo,c.Valor,c.Imagen
                        FROM secuencias a
                        INNER JOIN notas b 
                        ON a.Nota = b.id
                        INNER JOIN tiempos c 
                        ON a.Tiempo = c.Id
                        WHERE a.Leccion = %s order by a.id;"""
            cursor.execute(query, (leccion,))
            secuencia_data = cursor.fetchall()
            secuencias = []
            for secuencia_item in secuencia_data:
                id,leccion,id_nota,escala,nombre_latino,nombre_ingles,\
                    origen,id_tiempo,tempo,valor,imagen = secuencia_item
                nota = Nota(id_nota,escala,nombre_latino,nombre_ingles,origen)
                tiempo = Tiempo(id_tiempo,tempo,valor,imagen)
                secuencia = Secuencia(None, leccion,nota,tiempo)
                secuencias.append(secuencia)
            return secuencias
        
        except Exception as e:
            raise e         

        finally:
            if conn:
                conn.close()
