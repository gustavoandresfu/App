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

