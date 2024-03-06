import mysql.connector
from mysql.connector.locales.eng import client_error


class Modelo:
    def __init__(self):
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database ="stfg"
                

            )
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos:", error)

    def conectar(self):
        return self.db

