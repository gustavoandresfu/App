from modelos.modelo import Modelo
import bcrypt
import random
import string

class Usuario:
    def __init__(self, id=None, tipo=None, nombre=None, apellido=None, email=None,
                 clave=None, token = None,fecha_alta=None, fecha_mod=None):
        self.id = id
        self.tipo = tipo
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.clave = clave
        self.token = token
        self.fecha_alta = fecha_alta
        self.fecha_mod = fecha_mod
        self.modelo = Modelo()


    def validar(self, usuario_parametro, clave):
        try:
            conexion = self.modelo.conectar()
            cursor = conexion.cursor()
            query = "SELECT clave FROM usuarios WHERE email = %s"
            cursor.execute(query, (usuario_parametro,))
            clave_guardada = cursor.fetchone()
            cursor.close()

            if clave_guardada:
                clave_guardada = clave_guardada[0].encode('utf-8')
                if bcrypt.checkpw(clave.encode('utf-8'), clave_guardada):
                     return self.buscar_por_email(usuario_parametro)

            return None

        except Exception as e:
            raise e
        
        finally:
            if conexion:
                conexion.close()  
         
    def crear_usuario(self, nombre, apellido,email, clave):
        try:
            conexion = self.modelo.conectar()
            cursor = conexion.cursor()
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(clave.encode('utf-8'), salt)
            token = self.generar_token(64)
            query = "INSERT INTO usuarios (tipo,nombre, apellido, email, clave, token) VALUES (1,%s, %s,%s, %s,%s)"
            cursor.execute(query, (nombre, apellido, email, hashed_password,token))
            conexion.commit()
            cursor.close()

            return True  
        

        except Exception as e:
            raise e   

    def buscar_por_email(self,email):
        try:
            conexion = Modelo().conectar()
            cursor = conexion.cursor()
            query = "SELECT * FROM usuarios WHERE email = %s"
            cursor.execute(query, (email,))
            usuario_data = cursor.fetchone()
            cursor.close()

            if usuario_data:
                return Usuario(*usuario_data)

        except Exception as e:
            return None
        
        finally:
            if conexion:
                conexion.close()

        return None
    def generar_token(self,longitud):
        caracteres = string.ascii_letters + string.digits  
        token = ''.join(random.choice(caracteres) for i in range(longitud))
        return token
