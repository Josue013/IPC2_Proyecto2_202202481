from nodo import nodo
import os

class listaSistemaDeDrones:

    def __init__(self):
        self.primero = None
        self.size = 0
    
    def agregar(self, sistema_drones):
        nuevo_nodo = nodo(tipo_dato = sistema_drones)

        if self.primero is None:
            self.primero = nuevo_nodo
            self.size += 1
            return
        
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = nuevo_nodo
        self.size += 1

    def __iter__(self):
        self.actual = self.primero
        return self

    def __next__(self):
        if self.actual is not None:
            valor_actual = self.actual.tipo_dato
            self.actual = self.actual.siguiente
            return valor_actual
        else:
            raise StopIteration
        
    def obtener_sistema(self, sistema):
        actual = self.primero

        while actual != None:
            if actual.tipo_dato.nombre == sistema:
                return actual.tipo_dato
            actual = actual.siguiente

        return None
        
    def obtener_size(self):
        return self.size
    
    def limpiar_datos(self):
        while self.primero != None:
            actual = self.primero
            self.primero = self.primero.siguiente
            del actual
        self.size = 0
    
    def graficar(self):
        contador = 0
        texto = """digraph G {\ncharset="UTF-8" """

        actual = self.primero

        while actual != None:
            texto += f"""a{contador} [ shape="none" fontname="bebas" label=<\n
            <TABLE border="0" cellspacing="0.5" cellpadding="10" bgcolor="black">\n
                <TR><TD colspan="{int(actual.tipo_dato.cantidad)+1}" border="1" bgcolor="#FF5B0E">{actual.tipo_dato.nombre}</TD></TR>\n"""
            texto += actual.tipo_dato.contenido.graficar()
            texto += actual.tipo_dato.lista_graf.graficar()
            texto += "</TABLE>>]\n"
            contador += 1
            actual = actual.siguiente
        texto += "}"

        f = open('bb.dot', 'w', encoding="utf-8")
        f.write(texto)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f'dot -Tpng bb.dot -o Grafica_Sistema_de_drones.png')
