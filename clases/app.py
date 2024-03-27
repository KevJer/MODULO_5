from laptop_gaming import Laptop_Gaming
import tkinter as tk
from tkinter import ttk
class App:
    def __init__(self, root):
        self.root = root
        self.laptops = []
        self.imagenes = []
        
        root.title("Ingrear Datos")
        self.setup_ui()
        pass
    
    def setup_ui(self):
        ttk.Label(self.root, text="Marca").grid(row=0,column=0) 
        self.marca = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.marca).grid(row=0, column=1)
       
        ttk.Label(self.root, text="Procesador").grid(row=1,column=0) 
        self.procesador = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.procesador).grid(row=1, column=1)
       
        ttk.Label(self.root, text="Memoria").grid(row=2,column=0) 
        self.memoria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.memoria).grid(row=2, column=1)
        
        ttk.Label(self.root, text="Tarjeta grafica").grid(row=3,column=0) 
        self.tarj_grafica = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.tarj_grafica).grid(row=3, column=1)
       
        ttk.Label(self.root, text="Precio").grid(row=4,column=0) 
        self.precio = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.precio).grid(row=4, column=1)


        ttk.Button(self.root, text="Agregar Laptop", command=self.agregar_laptop ).grid(row=5, column=0)
        pass

    def agregar_laptop(self):
        nueva_laptop = Laptop_Gaming(self.marca.get(), self.procesador.get(), self.memoria.get(), self.tarj_grafica.get(), self.precio.get())
        self.laptops.append(nueva_laptop)
        print(self.laptops[0])
        pass   

root = tk.Tk()
app = App(root)
root.mainloop()