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
from controladores.clase_controlador import Clase_controlador
from controladores.practica_controlador import Practica_controlador
from controladores.progreso_controlador import Progreso_controlador

class Inicio_vista:
    def __init__(self, root, usuario_obj):
        

        usuario = usuario_obj.id #me manejo por id el resto de la aplicación
        self.root = root
        self.root.title("Inicio")
        self.root.geometry("400x300")
        self.root.resizable(False, False)         
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - self.root.winfo_width()) // 2
        y = (screen_height - self.root.winfo_height()) // 2
        self.root.geometry("+{}+{}".format(x, y))
        self.root.iconbitmap("recursos/musicar.ico") 
        label_inicio = tk.Label(root, text="¡Bienvenido al sistema!")
        label_inicio.pack(pady=10)
        button_frame = tk.Frame(root)
        button_frame.pack(side=tk.BOTTOM, pady=10) 

        button_clase = tk.Button(button_frame, text="Clase", width=15, height=5, command=lambda: self.on_clase_click(usuario))
        button_clase.pack(side=tk.LEFT, padx=5)  

        button_practica = tk.Button(button_frame, text="Práctica", width=15, height=5, command=lambda: self.on_practica_click(usuario))
        button_practica.pack(side=tk.LEFT, padx=5)  

        button_progreso = tk.Button(button_frame, text="Progreso", width=15, height=5, command=lambda: self.on_progreso_click(usuario))
        
        button_progreso.pack(side=tk.LEFT, padx=5) 
        
   
    def on_clase_click(self, usuario):
            
            try:
                             
                clase_vista = Clase_controlador(usuario)

            except Exception as e:
                messagebox.showerror("Error", f"Hubo un problema: {e}")
                   


    def on_practica_click(self,usuario):

            try:
                practica_vista = Practica_controlador(usuario)
            
            except Exception as e:

                messagebox.showerror("Error", f"Hubo un problema: {e}")    
        

    def on_progreso_click(self,usuario):
            
            try:
            
                progreso_vista = Progreso_controlador()
                progreso_vista.mostrar(usuario)
            
            except Exception as e:

                messagebox.showerror("Error", f"Hubo un problema: {e}")    
 

    def main():
        root = tk.Tk()
        inicio_vista = Inicio_vista()
        root.mainloop()

    if __name__ == "__main__":
        main()
