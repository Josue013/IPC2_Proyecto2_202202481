from nodo import nodo

class listaContenido:
    def __init__(self):
        self.primero = None
        self.size = 0

    def agregar(self, contenido):
        nuevo_nodo = nodo(tipo_dato = contenido)

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
        
    def obtener_size(self):
        return self.size
    
    def obtener_contenido(self, dron_buscado):
        actual = self.primero

        while actual != None:
            if actual.tipo_dato.dron == dron_buscado:
                return actual.tipo_dato
            actual = actual.siguiente

        return None
    
    def graficar(self):
        texto = """<TR>\n<TD border="1" bgcolor="#ed4d02">Altura</TD>"""

        actual = self.primero

        while actual != None:
            texto += f"""<TD border="1" bgcolor="#ed4d02">{actual.tipo_dato.dron}</TD>\n"""
            actual = actual.siguiente
        texto += "</TR>"
        
        return texto
       