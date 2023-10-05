import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
import subprocess

class GesSistemaDrones:
    def __init__(self, raiz, funciones, bandera):
        self.raiz = raiz
        self.funciones = funciones
        self.flag = bandera
        self.ventana = tk.Toplevel(self.raiz, bg="orange", )
        self.ventana.resizable(0,0)
        self.ventana.geometry("800x400")

        self.ventana.title("Gestion de sistema de drones")
        self.ventana.config(bg="orange", bd=10, relief="groove", pady=20)
        label = tk.Label( self.ventana, text="Gestion de sistema de drones", font=("bebas",40), bg="orange", pady=20)
        label.pack(padx=10, pady=25)

        self.btnGrafica = tk.Button(self.ventana, text="Generar grafica",  height= 2, width=15, padx=5, pady=5, font=("bebas",15), bg="#FF5B0E", fg="black", command = self.generar_grafica)
        self.btnGrafica.pack()

    def generar_grafica(self):
        if self.flag:
            self.funciones.generar_grafica_sistemas()
            messagebox.showinfo("Genial!", "La grafica se ha generado exitosamente", parent = self.ventana)
        else :
            messagebox.showwarning("Error!", "Debes de procesar el archivo.")   
