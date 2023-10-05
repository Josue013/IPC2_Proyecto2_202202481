import tkinter as tk
from tkinter import ttk, messagebox

class GesMensajes:
    def __init__(self, root, funciones):
        self.root = root
        self.fn = funciones
        self.bandera = False

        self.ventana = tk.Toplevel(self.root, bg="orange")
        self.ventana.resizable(0,0)
        self.ventana.geometry("1280x720")
        self.ventana.pack_propagate(False)


        self.ventana.title("Gestión de mensajes")

        label = tk.Label( self.ventana, text="Gestion de mensajes", font=("bebas",30), bg="orange",pady=10, fg="white")
        label.grid(row=0, column=0)

        self.FrameMensaje = tk.Frame(self.ventana, bg="orange")

        self.FrameMensaje.config(width=1250, height=750)
        self.FrameMensaje.pack_propagate(False)
        self.FrameMensaje.grid_propagate(False)
        self.FrameMensaje.grid(row=1, column=0)

        self.FrameTabla = tk.Frame(self.FrameMensaje, bg="orange")
        self.FrameTabla.pack_propagate(False)
        self.FrameTabla.config(width=625, height=750)
        self.FrameTabla.grid(row=0, column=0, padx=15, pady=15)

        labelmsg = tk.Label( self.FrameTabla, text="=================== Lista de mensajes ===================", font=("bebas",15), bg="orange", pady=15, fg="white"	)
        labelmsg.pack()

        self.tablaListMsg = ttk.Treeview(self.FrameTabla, columns=("col1", "col2"), height=7)
        self.tablaListMsg.column("#0",width=75, anchor="center")
        self.tablaListMsg.column("col1",width=200, anchor="center")
        self.tablaListMsg.column("col2",width=200, anchor="center")
        self.tablaListMsg.heading("#0", text="No.", anchor="center")
        self.tablaListMsg.heading("col1", text="Nombre mensaje", anchor="center")
        self.tablaListMsg.heading("col2", text="Sistema", anchor="center")
        self.tablaListMsg.pack(pady=25)

        self.llenar_tabla_msg()

        self.btnCargarInstrucciones = tk.Button(self.FrameTabla, text="Cargar instrucciones", height= 1, width=15, padx=10, font=("bebas",15), bg="white", command = self.mensaje_seleccionado)
        self.btnCargarInstrucciones.pack()

        Label_Instrucciones = tk.Label( self.FrameTabla, text="=================== Lista de instrucciones ===================", font=("bebas",15), bg="orange", pady=30, fg="white")
        Label_Instrucciones.pack()

        self.tablaInstrucciones= ttk.Treeview(self.FrameTabla, columns=("col1", "col2"), height=6, )
        self.tablaInstrucciones.column("#0", width=75, anchor="center")
        self.tablaInstrucciones.column("col1", width=200, anchor="center")
        self.tablaInstrucciones.column("col2", width=200, anchor="center")
        self.tablaInstrucciones.heading("#0", text="No.", anchor="center")
        self.tablaInstrucciones.heading("col1", text="Dron", anchor="center")
        self.tablaInstrucciones.heading("col2", text="Instruccion", anchor="center")
        self.tablaInstrucciones.pack(pady=2)

        self.Frame_mensaje = tk.Frame(self.FrameMensaje, bg="orange")
        self.Frame_mensaje.pack_propagate(False)
        self.Frame_mensaje.grid_propagate(False)
        self.Frame_mensaje.config(width=625, height=750)
        self.Frame_mensaje.grid(row=0, column=1)

        self.btnProcesar = tk.Button(self.FrameTabla, text="Procesar mensaje", height= 1, width=15, padx=10,font=("bebas",15), bg="white", command = self.procesar)
        self.btnProcesar.pack(pady=25)

        self.FrameDatos = tk.Frame(self.Frame_mensaje,bg="orange")
        self.FrameDatos.pack_propagate(False)
        self.FrameDatos.grid_propagate(False)
        self.FrameDatos.config(width=525, height=350)
        self.FrameDatos.pack(pady=40)

        self.Label_systemName = tk.Label( self.FrameDatos, text="Sistema de drones a utilizar:", font=("bebas",15), bg="orange", fg="white")
        self.Label_systemName.grid(row=0, column=0, padx=45, pady=25)


        self.nombre = tk.StringVar()
        self.nombreSistema = tk.Entry(self.FrameDatos, width=15, font=("bebas",15), justify="left", state="readonly", textvariable=self.nombre)
        self.nombreSistema.grid(row=0, column=1)

        self.label_mensaje = tk.Label( self.FrameDatos, text="===================== MENSAJE =====================", font=("bebas",15), bg="orange", pady=15, fg="white")
        self.label_mensaje.grid(row=1, column=0, columnspan=2)

        self.mensaje = tk.Text(self.FrameDatos, width=50, height=5, font=("bebas",15), state="disabled")
        self.mensaje.grid(row = 2, column=0, columnspan=2, pady=15)


        self.LabelTiempo = tk.Label( self.FrameDatos, text="Tiempo   --------------------->", font=("bebas",15), bg="orange", fg="white")
        self.LabelTiempo.grid(row=3, column=0, padx=45, pady=20)

        self.tiempo = tk.StringVar()
        self.Tiempo = tk.Entry(self.FrameDatos, width=15, font=("bebas",15), justify="left", state="readonly", textvariable=self.tiempo)
        self.Tiempo.grid(row=3, column=1)

        self.graficar = tk.Button(self.Frame_mensaje, text="Generar grafica",  height= 1, width=15, padx=10, font=("bebas",15), bg="white", command = self.graficar)
        self.graficar.pack()

    def llenar_tabla_msg(self):
        lista_msg = self.fn.obtener_lista_mensajes()
        if lista_msg.obtener_size() != 0:
            for index, msg in enumerate(lista_msg):
                self.tablaListMsg.insert("", "end", text=f"{index+1}", values=(f"{msg.nombre_msg}",f"{msg.sistema}"))

    def mensaje_seleccionado(self):
        self.limpiar_tabla(self.tablaInstrucciones)
        item_seleccionado = self.tablaListMsg.focus()
        if item_seleccionado:
            datos = self.tablaListMsg.item(item_seleccionado)
            lista_msg = self.fn.obtener_lista_instrucciones_por_mensaje(datos.get("values")[0])
            for index, ins in enumerate(lista_msg.instrucciones):
                self.tablaInstrucciones.insert("", "end", text=f"{index+1}", values=(f"{ins.dron}",f"{ins.instruccion}"))
        else :
            messagebox.showerror("Error", "Debes seleccinar un mensaje", parent = self.ventana)

    def graficar(self):
        item_seleccionado = self.tablaListMsg.focus()
        if self.bandera:
            if item_seleccionado:
                datos = self.tablaListMsg.item(item_seleccionado)
                self.fn.graficar_movimientos(datos.get("values")[0])
                messagebox.showinfo("Exito", "Grafica generada con exito", parent = self.ventana)
            else :
                messagebox.showerror("Error", "Debes seleccinar un mensaje", parent = self.ventana)
        else :
                messagebox.showerror("Error", "Debes procesar un mensaje", parent = self.ventana)

    def procesar(self):
        item_seleccionado = self.tablaListMsg.focus()
        if item_seleccionado:
            datos = self.tablaListMsg.item(item_seleccionado)
            nombre_sistema, mensaje, tiempo_op = self.fn.formar_mensaje(datos.get("values")[0])
            self.nombre.set(nombre_sistema)
            self.llenar_mensaje(mensaje)      
            self.tiempo.set(tiempo_op)
            self.bandera = True     
        else :
            messagebox.showerror("Error", "Debes seleccinar un mensaje", parent = self.ventana)

    def llenar_mensaje(self, mensaje):
        self.mensaje.config(state="normal")
        self.mensaje.delete("1.0", tk.END)
        self.mensaje.insert("1.0", mensaje)
        self.mensaje.config(state="disabled")

    def limpiar_tabla(self, table):
        for items in table.get_children():
            table.delete(items)
