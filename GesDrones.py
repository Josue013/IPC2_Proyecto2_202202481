import tkinter as tk
import tkinter.font as font
from tkinter import ttk, messagebox

class GesDrones:

    def __init__(self, frame=None, lista=None, funciones=None):
        self.frame = frame
        self.lista = lista
        self.funciones = funciones

        self.ventana = tk.Toplevel(self.frame, bg="orange")
        self.ventana.resizable(0,0)  
        
        self.ventana.title("Gestión de drones")
        self.ventana.config(bg="orange")
        self.ventana.config(bd=10)
        self.ventana.config(relief="groove")

        label = tk.Label(self.ventana, text="Gestion de drones", font=("bebas",15), bg="white", fg="black")
        label.pack(side="top", fill="x", pady=10)  

        self.contenido = tk.Frame(self.ventana, bg="orange")

        self.contenido.config(width=1280, height=720, pady=50, padx=90)
        self.contenido.pack_propagate(False)
        self.contenido.grid_propagate(False)
        self.contenido.pack()

        self.frame_table = tk.Frame(self.contenido, bg="#FF5B0E", padx=20)
        self.frame_table.pack_propagate(False)
        self.frame_table.grid_propagate(False)
        self.frame_table.config(width=520, height=400, pady=50, padx=50)
        self.frame_table.grid(row=0, column=0)

        self.table = ttk.Treeview(self.frame_table, columns=("col1"), height=550)

        self.table.column("#0",width=220, anchor="center")
        self.table.column("col1",width=220, anchor="center")
        self.table.heading("#0", text="Numero", anchor="center")
        self.table.heading("col1", text="Nombre del dron", anchor="center")
        self.llenar_tabla()
        self.table.pack()

        self.frame_add = tk.Frame(self.contenido, bg="#FF5B0E", padx=20)
        self.frame_add.pack_propagate(False)
        self.frame_add.grid_propagate(False)
        self.frame_add.config(width=520, height=400)
        self.frame_add.place(anchor="center")
        self.frame_add.grid(row=0, column=1)

        label1 = tk.Label( self.frame_add, text="Agregar Dron", font=("bebas",12), fg="black")
        label1.pack(side="top", fill="x", padx = 20, pady=20)

        self.agregar = tk.Entry(self.frame_add, width=25, font=("Arial",12), bg="white", fg="black", justify="center")
        self.agregar.pack()

        button = tk.Button(self.frame_add, text="Agregar",
            highlightbackground='black', height= 1, width=20, font=("bebas",12), bg="white", fg="black", command = self.guardar_dron)
        button.pack(anchor="s", side="bottom", pady=140)

    # funcion para guardar un nuevo dron
    def guardar_dron(self):
        if self.agregar.get() == '':
            messagebox.showerror("Error", "Debes llenar el espacio.", parent = self.ventana)
        else :
            if self.funciones.agregar_nuevo_dron(self.agregar.get()):
                messagebox.showinfo("Exito", "Se ha agregado el dron correctamente.", parent = self.ventana)
                self.limpiar_tabla()
                self.llenar_tabla()
            else:
                messagebox.showerror("Error", "Ya existe un dron con ese nombre.", parent = self.ventana)

    # funcion para llenar la tabla
    def llenar_tabla(self):
        if self.lista != 0:
            for index, drones in enumerate(self.lista):
                self.table.insert("", "end", text=f"{index+1}", values=(f"{drones.nombre}"))

    # funcion para limpiar la tabla
    def limpiar_tabla(self):
        for items in self.table.get_children():
            self.table.delete(items)
        self.agregar.delete(0, 'end')

        
