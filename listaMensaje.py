from nodo import nodo

class listaMensaje:
    def __init__(self):
        self.primero = None
        self.size = 0

    def agregar(self, mensaje):
        nuevo_nodo = nodo(tipo_dato = mensaje)

        if self.size == 0:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
        
            actual = self.primero
            anterior = None
            while actual is not None and actual.tipo_dato.nombre_msg.lower() < nuevo_nodo.tipo_dato.nombre_msg.lower():
                anterior = actual
                actual = actual.siguiente
            if anterior is None:
                nuevo_nodo.siguiente = self.primero
                self.primero = nuevo_nodo
            else:
                nuevo_nodo.siguiente = actual
                anterior.siguiente = nuevo_nodo

        self.size += 1

    def obtener_msg(self, msg):
        actual = self.primero

        while actual != None:
            if actual.tipo_dato.nombre_msg == msg:
                return actual.tipo_dato
            actual = actual.siguiente

        return None

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
    
    def limpiar_datos(self):
        while self.primero != None:
            actual = self.primero
            self.primero = self.primero.siguiente
            del actual
        self.size = 0

