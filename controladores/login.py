from modelos.usuario import Usuario
from vistas.login_vista import Login_vista

class Logear:
    def __init__(self, root):
        self.root = root
        self.model = Usuario()
        self.view = Login_vista(root, self)


    def login(self, username, password):
        return self.model.validar(username, password)

    def run(self):
        self.root.mainloop()

