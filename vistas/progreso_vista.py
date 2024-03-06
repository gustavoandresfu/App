import tkinter as tk
#from controladores.progreso_controlador import Progreso_controlador

class Progreso_vista:
    def __init__(self, progreso_clase, progreso_practica):
        
        root = tk.Toplevel()
        self.root = root
        self.root.title("PROGRESO")
        self.root.geometry("400x300")  
        self.root.resizable(False, False) 
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - self.root.winfo_width()) // 2
        y = (screen_height - self.root.winfo_height()) // 2
        self.root.geometry("+{}+{}".format(x, y))
        self.root.iconbitmap("recursos/musicar.ico") 
        label_inicio = tk.Label(root, text="¡Bienvenido a tu progreso!")
        label_inicio.pack()

         # Barra de progreso clases
        bar_width_1 = 300
        progreso_val_1 = progreso_clase

        label_1 = tk.Label(self.root, text="Progreso en clases:")
        label_1.pack(padx=20, pady=20)

        canvas1 = tk.Canvas(self.root, width=bar_width_1, height=20, bg='gray')
        canvas1.pack(padx=20)

        progreso_bar_1 = canvas1.create_rectangle(0, 0, int(progreso_val_1 * bar_width_1 / 100), 20, fill='blue')

        # Barra de progreso practicas
        bar_width_2 = 300
        progreso_val_2 = progreso_practica

        label_2 = tk.Label(self.root, text="Progreso en lecciones de práctica:")
        label_2.pack(padx=20, pady=20)

        canvas2 = tk.Canvas(self.root, width=bar_width_2, height=20, bg='gray')
        canvas2.pack(padx=20)

        progreso_bar_2 = canvas2.create_rectangle(0, 0, int(progreso_val_2 * bar_width_2 / 100), 20, fill='green')

        self.root.mainloop()

