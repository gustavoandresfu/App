import tkinter as tk
from controladores.login import Logear


def main():
    

    root = tk.Tk()
    controller = Logear(root)
    controller.run()

if __name__ == "__main__":
    main()

