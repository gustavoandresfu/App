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
