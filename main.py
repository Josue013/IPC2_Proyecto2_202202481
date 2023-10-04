import webbrowser
import os
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from tkinter import messagebox 
from GesDrones import GesDrones
from GesSistemaDrones import GesSistemaDrones
from GesMensajes import GesMensajes

class main:
    def __init__(self, root):
        self.root = root
        self.flag = False

        self.root.title("Interfaz")
        self.root.resizable(0,0)
        self.root.geometry("1280x720")
        self.root.config(bg="orange")
        self.root.config(bd=10)
        self.root.config(relief="groove")

        # configuracion botones de la interfaz 

        self.menu = Menu(root)

        self.label = Label(text="PROYECTO 2 - IPC2 - SECCION D" , font=("bebas",12), bg="white", fg="black" )  
        self.label.pack(side=TOP, fill=X, padx=10, pady=25)

        self.boton_inicializar = Button(root, text="Inicializar" ,font=("bebas",12), bg="white", fg="black", height=1, width=25 , padx=10, pady=10)
        self.boton_cargar_archivo = Button(root, text="Cargar archivo de entrada" ,font=("bebas",12), bg="white", fg="black", height=1, width=25 , padx=10, pady=10, command = self.cargar_archivo)
        self.boton_procesar = Button(root, text="Procesar" ,font=("bebas",12), bg="white", fg="black", height=1, width=25 , padx=10, pady=10)
        self.boton_generar_archivo = Button(root, text="Generar archivo de salida" ,font=("bebas",12), bg="white", fg="black", height=1, width=25 , padx=10, pady=10)
        self.boton_GesDrones = Button(root, text="Gestion de drones" ,font=("bebas",12), bg="white", fg="black", height=1, width=25 , padx=10, pady=10, command = self.GesDrones)
        self.boton_GesSistemaDrones = Button(root, text="Gestion de sistemas de drones" ,font=("bebas",12), bg="white", fg="black", height=1, width=25 , padx=10, pady=10, command = self.GesSistemaDrones)
        self.boton_GesMensajes = Button(root, text="Gestion de mensajes" ,font=("bebas",12), bg="white", fg="black", height=1, width=25 , padx=10, pady=10, command = self.GesMensajes)
        self.boton_ayuda = Button(root, text="Ayuda" ,font=("bebas",12), bg="white", fg="black", height=1, width=25 , padx=10, pady=10)

        self.boton_inicializar.pack(padx=10, pady=10)
        self.boton_cargar_archivo.pack(padx=10, pady=10)
        self.boton_procesar.pack(padx=10, pady=10)
        self.boton_generar_archivo.pack(padx=10, pady=10)
        self.boton_GesDrones.pack(padx=10, pady=10)
        self.boton_GesSistemaDrones.pack(padx=10, pady=10)
        self.boton_GesMensajes.pack(padx=10, pady=10)
        self.boton_ayuda.pack(padx=10, pady=10)


        # Funcion que muestra los datos del estudiante
        def datos_estudiante():
            messagebox.showinfo(title="Datos del estudiante", message="Nombre: Josué Nabí Hurtarte Pinto \nCarnet: 202202481 \nIngenieria en sistemas \nIPC2 Sección D \n4to Semestre" )
            abrir_documentacion()
        self.boton_ayuda.config(command=datos_estudiante)

        # Funcion para abrir documentacion
        def abrir_documentacion():
            pdf_nombre = "Documentacion 202202481.pdf"
            script_dir = os.path.dirname(os.path.abspath(__file__))
            pdf_path = os.path.join(script_dir, pdf_nombre)
            webbrowser.open_new(pdf_path)

    # funcion para cargar archivo
    def cargar_archivo(self):
        self.archivo = filedialog.askopenfilename(filetypes=[("Text files", "*.xml")])
        if self.archivo:
            messagebox.showinfo("Genial!", "Se cargó correctamente el archivo.")
        else:
            messagebox.showerror("Error!", "No se cargó ningún archivo.")

    # funcion gestion de drones
    def GesDrones(self):
        ventana = GesDrones(self.root)

    # funcion gestion de sistema de drones
    def GesSistemaDrones(self):
        ventana = GesSistemaDrones(self.root) 
        
    # funcion gestion de mensajes
    def GesMensajes(self):
        ventana = GesMensajes(self.root) 



root = Tk()
ventana = main(root)

root.mainloop()            