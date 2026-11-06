class Nodo:
    def __init__(self, c=None):
        self.clave = c; self.izq = None; self.der = None

def alt(n):  return -1 if n is None else n.alt
def fe(n):   return 0 if n is None else alt(n.izq) - alt(n.der)   # factor de equilibrio
def recalc(n): n.alt = 1 + max(alt(n.izq), alt(n.der))

def insertar(n, clave):
    if n is None:                        # llegamos a un hueco: aqui va
        return Nodo(clave)
    if clave < n.clave:
        n.izq = insertar(n.izq, clave)   # el retorno se REENGANCHA
    elif clave > n.clave:
        n.der = insertar(n.der, clave)
    recalc(n)                            # actualiza la altura (NO balancea)
    return n


raiz=None

mejorOrden=[4, 2, 1, 3, 6, 5, 7] 

#en el caso del mejor orden para insertar nuestro arbol quedaria algo asi 

''
a 
''
for x in mejorOrden:
    insertar(raiz, x)
