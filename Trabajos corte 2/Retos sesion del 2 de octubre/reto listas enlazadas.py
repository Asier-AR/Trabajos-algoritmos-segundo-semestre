class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class Pila:
    def __init__(self):
        self.tope = None      # cabeza de la lista = tope de la pila
        self.tamano = 0

    def apilar(self, x):
        # el nuevo nodo apunta al tope anterior y pasa a ser el tope: O(1)
        self.tope = Nodo(x, self.tope)
        self.tamano += 1

    def desapilar(self):
        if self.vacia():
            return None
        dato = self.tope.dato
        self.tope = self.tope.siguiente   # el tope pasa al siguiente nodo: O(1)
        self.tamano -= 1
        return dato

    def cima(self):
        return None if self.vacia() else self.tope.dato

    def vacia(self):
        return self.tope is None

    def size(self):
        return self.tamano


def balanceados(s):
    p = Pila()
    pares = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in '([{':
            p.apilar(c)
        elif c in ')]}':
            if p.desapilar() != pares[c]:
                return False
    return p.vacia()  