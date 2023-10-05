from dron import dron
from altura import altura
from contenido import contenido
from sist_de_drones import sist_de_drones
from instruccion import instruccion
from mensaje import mensaje
from mov import mov
from men_procesado import men_procesado
from listaDrones import listaDrones
from listaAlturas import listaAlturas
from listaContenido import listaContenido
from listaSistemaDeDrones import listaSistemaDeDrones
from listaInstrucciones import listaInstrucciones
from listaMensaje import listaMensaje
from listaMov import listaMov
from listaMensajeProcesado import listaMensajeProcesado
import xml.etree.ElementTree as ET

class funciones:
    def __init__(self):
        self.lista_dron = listaDrones()
        self.lista_sistemas = listaSistemaDeDrones()
        self.lista_msg = listaMensaje()
        self.lista_msg_procesado = listaMensajeProcesado()

    def leer_xml(self,archivo):
        tree = ET.parse(archivo)
        root = tree.getroot()

        for drones in root.findall("./listaDrones/dron"):
            nuevo_dron = dron(drones.text)
            self.lista_dron.agregar(nuevo_dron)

        for sistema in root.findall("./listaSistemasDrones/sistemaDrones"):
            nombre = sistema.get("nombre")
            alturamax = sistema.find("alturaMaxima")
            cantidadDrones = sistema.find("cantidadDrones")


            lista_contenido_temp = listaContenido()
            lista_alturas_graf = listaAlturas()

            cont = 1
            for contenidos in sistema.findall("contenido"):
                dron_contenido = contenidos.find("dron")

                lista_alturas_temp = listaAlturas()

                if self.validar_dron(dron_contenido.text):
                    for alturas_dron in contenidos.findall("./alturas/altura"):
                        altura_nueva = altura(alturas_dron.get("valor"), alturas_dron.text, dron_contenido.text, cont)
                        lista_alturas_graf.agregar_ordenado(altura_nueva)
                        lista_alturas_temp.agregar(altura_nueva)
                    cont += 1
                    contenido_nuevo = contenido(dron_contenido.text, lista_alturas_temp)
                    lista_contenido_temp.agregar(contenido_nuevo)
                else :
                    print(dron_contenido.text, "no esta definido en la lista drones\n")
            nuevo_sistema = sist_de_drones(nombre, alturamax.text, cantidadDrones.text, lista_contenido_temp, lista_alturas_graf)
            self.lista_sistemas.agregar(nuevo_sistema)

        for mensajes in root.findall("./listaMensajes/Mensaje"):

            sistema_mensaje = mensajes.find("sistemaDrones")
            lista_instruc_temp = listaInstrucciones()
            for instrucciones in mensajes.findall("./instrucciones/instruccion"):
                nueva_instru = instruccion(instrucciones.get("dron"), instrucciones.text)
                lista_instruc_temp.agregar(nueva_instru)
            

            nuevo_msg = mensaje(mensajes.get("nombre"), sistema_mensaje.text, lista_instruc_temp)
            self.lista_msg.agregar(nuevo_msg)
        self.procesar_mensajes()

    def procesar_mensajes(self):
        for mensajes in self.lista_msg:
            mensaje = ""
            lista_movi = listaMov()
            sistema = self.lista_sistemas.obtener_sistema(mensajes.sistema)
            for index, instru in enumerate(mensajes.instrucciones):
                tiempo = 0
                self.movimientos_dron(instru.instruccion, instru.dron, lista_movi, tiempo, index)
                alturas_dron = sistema.contenido.obtener_contenido(instru.dron)
                for alturas in alturas_dron.alturas:
                    if instru.instruccion == alturas.altura:
                        mensaje += alturas.valor
            for index, lista_instru in enumerate(mensajes.instrucciones):
                lista_movi.completar_esperar(lista_instru.dron, lista_instru.instruccion, index)

            tiempo_optimo = lista_movi.obtener_mayor_tiempo()

            nuevo_ms_procesado = men_procesado(mensajes.nombre_msg, mensaje, sistema.nombre, tiempo_optimo, lista_movi)
            self.lista_msg_procesado.agregar(nuevo_ms_procesado)


    def formar_mensaje(self, nombre_msg):
        lista_movimientos = listaMov()
        mensaje = ""
        msg = self.lista_msg.obtener_msg(nombre_msg)
        sistema = self.lista_sistemas.obtener_sistema(msg.sistema)

        for index, lista_instru in enumerate(msg.instrucciones):
            tiempo = 0
            self.movimientos_dron(lista_instru.instruccion, lista_instru.dron, lista_movimientos, tiempo, index)
            alturas_dron = sistema.contenido.obtener_contenido(lista_instru.dron)
            for alturas in alturas_dron.alturas:
                if lista_instru.instruccion == alturas.altura:
                    mensaje += alturas.valor

        for index, lista_instru in enumerate(msg.instrucciones):
            lista_movimientos.completar_esperar(lista_instru.dron, lista_instru.instruccion, index)

        tiempo_optimo = lista_movimientos.obtener_mayor_tiempo()
        
        return sistema.nombre, mensaje, tiempo_optimo

    def graficar_movimientos(self, nombre_msg):
        lista_movimientos = listaMov()
        lista_dron_temp = listaDrones()
        msg = self.lista_msg.obtener_msg(nombre_msg)
        sistema = self.lista_sistemas.obtener_sistema(msg.sistema)

        for index, lista_instru in enumerate(msg.instrucciones):
            tiempo = 0
            self.movimientos_dron(lista_instru.instruccion, lista_instru.dron, lista_movimientos, tiempo, index)
            if self.validar_dron_unico(lista_instru.dron, lista_dron_temp) == False:
                nuevo_dron = dron(lista_instru.dron)
                lista_dron_temp.agregar_unico(nuevo_dron)

        for index, lista_instru in enumerate(msg.instrucciones):
            lista_movimientos.completar_esperar(lista_instru.dron, lista_instru.instruccion, index)


        lista_movimientos.generar_grafica(sistema.cantidad,msg.nombre_msg, lista_dron_temp)
    
    def movimientos_dron(self, altura_, dron_, lista_movi, tiempo, num):
        tiempo_temp = tiempo
        altura_llegar = int(altura_)
        altura_temp = int(lista_movi.obtener_movimientos_dron(dron_))
        ultimo_tiempo = int(lista_movi.obtener_tiempo_dron(dron_))
        indice = int(lista_movi.obtener_indice_dron(dron_, num))
        if ultimo_tiempo > 0:
            tiempo_temp = ultimo_tiempo

        primer_num = int(lista_movi.obtener_numero_dron_primero(dron_))

        numero_ins = int(lista_movi.obtener_numero_dron(dron_))
        if numero_ins != 0:
            num = numero_ins

        if altura_temp < int(altura_):
            while altura_temp < altura_llegar:
                altura_temp += 1
                tiempo_temp += 1
                nuevo_movimiento = mov("Subir", tiempo_temp, dron_, altura_, indice)
                lista_movi.agregar_ordenado(nuevo_movimiento)
            tiempo_temp += 1
            bandera = lista_movi.obtener_tiempo(tiempo_temp)
            if bandera:
                nuevo_movimiento = mov("Esperar", tiempo_temp, dron_, altura_, indice)
                lista_movi.agregar_ordenado(nuevo_movimiento)
                self.movimientos_dron(altura_, dron_, lista_movi, tiempo_temp, indice)
            else :
                nuevo_movimiento = mov("Emitir luz", tiempo_temp, dron_, altura_, indice)
                lista_movi.agregar_ordenado(nuevo_movimiento)
        elif altura_temp > int(altura_):
            while altura_temp > altura_llegar:
                tiempo_temp += 1
                nuevo_movimiento = mov("Bajar", tiempo_temp, dron_, altura_, indice)
                lista_movi.agregar_ordenado(nuevo_movimiento)
                altura_temp -= 1
            
            tiempo_temp += 1
            bandera = lista_movi.obtener_tiempo(tiempo_temp)
            if bandera:
                nuevo_movimiento = mov("Esperar", tiempo_temp, dron_, altura_, indice)
                lista_movi.agregar_ordenado(nuevo_movimiento)
                self.movimientos_dron(altura_, dron_, lista_movi, tiempo_temp, indice)
            else :
                nuevo_movimiento = mov("Emitir luz", tiempo_temp, dron_, altura_, indice)
                lista_movi.agregar_ordenado(nuevo_movimiento)
        elif altura_temp == int(altura_):
            tiempo_temp += 1
            bandera = lista_movi.obtener_tiempo(tiempo_temp)
            if bandera:
                nuevo_movimiento = mov("Esperar", tiempo_temp, dron_, altura_, indice)
                lista_movi.agregar_ordenado(nuevo_movimiento)
                self.movimientos_dron(altura_, dron_, lista_movi, tiempo_temp, indice)
            else:
                nuevo_movimiento = mov("Emitir luz", tiempo_temp, dron_, altura_, indice)
                lista_movi.agregar_ordenado(nuevo_movimiento)
    
    def inicializar_sistema(self):
        self.lista_dron.limpiar_datos()
        self.lista_sistemas.limpiar_datos()
        self.lista_msg.limpiar_datos()
        self.lista_msg_procesado.limpiar_datos()

    def obtener_lista_drones(self):
        return self.lista_dron
    
    def obtener_lista_mensajes(self):
        return self.lista_msg
    
    def generar_xml(self):
        self.lista_msg_procesado.generar_xml(self.lista_msg)

    def obtener_lista_instrucciones_por_mensaje(self, msg):
        for lista in self.lista_msg:
            if lista.nombre_msg == msg:
                return lista
            
        return None

    def validar_dron(self, dron):
        for drones in self.lista_dron:
            if dron == drones.nombre:
                return True
            
        return False

    def validar_dron_unico(self, dron, lista_dron):
        for drones in lista_dron:
            if dron == drones.nombre:
                return True
            
        return False
    
    def agregar_nuevo_dron(self, dron_nuevo):
        if self.validar_dron(dron_nuevo):
            return False
        else :
            nuevo_dron = dron(dron_nuevo)
            self.lista_dron.agregar(nuevo_dron)
            return True
        
    def generar_grafica_sistemas(self):
        self.lista_sistemas.graficar()

