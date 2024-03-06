import tkinter as tk
from vistas.inicio_vista import Inicio_vista

class Inicio_controlador:
    def __init__(self, root, usuario_obj):
        self.root = root
        self.view = Inicio_vista(root, usuario_obj)

    def run(self):
        self.root.mainloop()
