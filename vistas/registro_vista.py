import tkinter as tk
from tkinter import messagebox

class Registro_vista:

    def __init__(self, root, controller):

        self.root = root
        self.root.title("Inicio")
        self.root.geometry("400x500")
        self.root.resizable(False, False)         
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - self.root.winfo_width()) // 2
        y = (screen_height - self.root.winfo_height()) // 2
        self.root.geometry("+{}+{}".format(x, y))
        self.root.iconbitmap("recursos/musicar.ico") 
        label_inicio = tk.Label(root, text="¡Bienvenido al sistema!")

        self.root = root
        self.label_nombre = tk.Label(root, text="Nombre")
        self.label_apellido = tk.Label(root, text="Apellido")
        self.label_usuario = tk.Label(root, text="Email")
        self.label_clave = tk.Label(root, text="clave")
        self.label_clave2 = tk.Label(root, text="repetir clave")
        self.label_codigo = tk.Label(root, text="codigo")

        self.entry_nombre = tk.Entry(root)
        self.entry_apellido = tk.Entry(root)         
        self.entry_usuario = tk.Entry(root)
        self.entry_clave = tk.Entry(root, show="*")
        self.entry_clave2 = tk.Entry(root, show="*")
        self.entry_codigo = tk.Entry(root)
        self.button_registro = tk.Button(root, text="Registrarse", command=self.on_registro_click)
        self.controller = controller

        self.label_nombre.pack(pady=5)
        self.entry_nombre.pack(pady=5)
        self.label_apellido.pack(pady=5)
        self.entry_apellido.pack(pady=5)

        self.label_usuario.pack(pady=5)
        self.entry_usuario.pack(pady=5)
        self.label_clave.pack(pady=5)
        self.entry_clave.pack(pady=5)
        self.label_clave2.pack(pady=5)
        self.entry_clave2.pack(pady=5)
        self.button_registro.pack(pady=5)

    def on_registro_click(self):
        usuario = self.entry_usuario.get()
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        clave = self.entry_clave.get()
        clave2 = self.entry_clave2.get()
        
        if clave == clave2:
            message = "Son iguales"
            messagebox.showinfo("Message", message)
            registrado = self.controller.registrar(nombre, apellido, usuario, clave)
            if registrado:
                message = "Se ha registrado, por favor reinicie la aplicacion"
                messagebox.showinfo("Message", message)
            
        else:
            message = "No Son iguales"
            messagebox.showinfo("Message", message) 


    def main(self):
        
        self.root.mainloop()


