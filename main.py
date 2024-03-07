# Copyright (c) 2024 Gustavo Futo
#
# Este programa es software libre; puedes redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General de GNU tal como se publica por
# la Free Software Foundation, ya sea la versión 3 de la Licencia, o
# (a tu elección) cualquier versión posterior.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; sin incluso la garantía implícita de
# COMERCIALIZACIÓN o IDONEIDAD PARA UN PROPÓSITO PARTICULAR. Consulta los
# detalles de la Licencia Pública General de GNU para obtener más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General de GNU
# junto con este programa. Si no, consulta <https://www.gnu.org/licenses/>.


import tkinter as tk
from controladores.login import Logear


def main():
    

    root = tk.Tk()
    controller = Logear(root)
    controller.run()

if __name__ == "__main__":
    main()

