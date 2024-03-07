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

import tkinter as tk
from tkinter import messagebox
from vistas.inicio_vista import Inicio_vista  
from controladores.registro_controlador import Registro_controlador
from controladores.inicio_controlador import Inicio_controlador

class Login_vista:

    def __init__(self, root, controller):

        self.root = root
        self.root.title("Login")
        self.root.geometry("400x300") 
        self.root.resizable(False, False)  
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - self.root.winfo_width()) // 2
        y = (screen_height - self.root.winfo_height()) // 2
        self.root.geometry("+{}+{}".format(x, y))        
        self.root.iconbitmap("recursos/musicar.ico")  
        self.label_usuario = tk.Label(root, text="usuario")
        self.label_clave = tk.Label(root, text="clave")
        self.entry_usuario = tk.Entry(root)
        self.entry_clave = tk.Entry(root, show="*")
        self.button_login = tk.Button(root, text="Login", command=self.on_login_click)
        self.button_registro = tk.Button(root, text="Registro", command=self.on_registro_click)
        #self.button_registro.config(state="disabled")
        self.controller = controller
        self.label_usuario.pack(pady=5)
        self.entry_usuario.pack(pady=5)
        self.label_clave.pack(pady=5)
        self.entry_clave.pack(pady=5)
        self.button_login.pack(pady=10)
        self.button_registro.pack(pady=10)
    
    def on_registro_click(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        Registrar_controler = Registro_controlador(self.root)
        Registrar_controler.run()   

    def on_login_click(self):
        usuario = self.entry_usuario.get()
        clave = self.entry_clave.get()

        try:

            usuario_obj = self.controller.login(usuario, clave) 

            if usuario_obj:  # Si se devuelve un objeto Usuario
                message = "Bienvenido " + str(usuario_obj.nombre)
                messagebox.showinfo("Message", message)
                for widget in self.root.winfo_children():
                    widget.destroy()
                inicio_controller = Inicio_controlador(self.root, usuario_obj)
                inicio_controller.run()
            else:
                message = "Credenciales incorrectas. Inténtelo de nuevo."
                messagebox.showinfo("Message", message)

        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema: {e}")  

