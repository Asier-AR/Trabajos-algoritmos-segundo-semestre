#Quis sesion del 30 de octubre


class Nodo:
    def __init__(self, c=None):
        self.clave = c; self.izq = None; self.der = None; self.alt = 0

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

def rotarDerecha(y):
    #        y                x
    #       / \              / \
    #      x   C    ==>     A   y
    #     / \                  / \
    #    A   B                B   C
    x = y.izq; B = x.der
    x.der = y; y.izq = B
    recalc(y); recalc(x)
    return x

def rotarIzquierda(x):
    #      x                  y
    #     / \                / \
    #    A   y      ==>     x   C
    #       / \            / \
    #      B   C          A   B
    y = x.der; B = y.izq
    y.izq = x; x.der = B
    recalc(x); recalc(y)
    return y

def inorden(n, s):
    if n is None: return
    inorden(n.izq, s); s.append(n.clave); inorden(n.der, s)

def preorden(n, s):
    if n is None: return
    s.append(f"{n.clave}(fe={fe(n)})"); preorden(n.izq, s); preorden(n.der, s)

def ver(titulo, raiz):
    s = []; preorden(raiz, s)
    t = []; inorden(raiz, t)
    print(f"{titulo:10s} preorden: {' '.join(s)}")
    print(f"{'':10s} inorden:  {t}  altura={alt(raiz)}")

def diagnosticar(arbol):
    Fe = fe(arbol)

    if -1 <= Fe <= 1:
        return "Equilibrado"

    if Fe >= 2:                          # pesado a la izquierda
        if fe(arbol.izq) >= 0:
            return "LL"
        else:
            return "LR"
    else:                                # pesado a la derecha
        if fe(arbol.der) <= 0:
            return "RR"
        else:
            return "RL"

def rotar(arbol, diagnostico):
    if diagnostico == "LL":
        return rotarDerecha(arbol)
    if diagnostico == "RR":
        return rotarIzquierda(arbol)
    if diagnostico == "LR":
        arbol.izq = rotarIzquierda(arbol.izq); recalc(arbol)
        return rotarDerecha(arbol)
    if diagnostico == "RL":
        arbol.der = rotarDerecha(arbol.der); recalc(arbol)
        return rotarIzquierda(arbol)
    return arbol

raiz=None
for x in range(3):
    dato = int(input("Por favor ingrese el numero que desea insertar: "))
    raiz = insertar(raiz, dato)

ver("ANTES", raiz)
caso = diagnosticar(raiz)
print("Diagnostico:", caso)
raiz = rotar(raiz, caso)
ver("DESPUES", raiz)

