# Reto 3 — ¿Cuándo NO alcanza una rotación? (reto corchador) · Obligatorio Construya un árbol donde, después de aplicar la rotación correcta en el nodo desbalanceado más profundo, 
# QUEDE otro nodo desbalanceado más arriba. ¿Es posible en una inserción? ¿Y en una eliminación? 
# Pista: En inserción, una sola rotación siempre basta y eso se puede demostrar mirando cómo cambia la altura del subárbol. 
# En eliminación no: la altura puede reducirse y propagar el problema hacia la raíz.


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

def buscar(n, clave, pasos=None):
    if pasos is not None: pasos.append("vacio" if n is None else str(n.clave))
    if n is None or n.clave == clave: return n
    return buscar(n.izq, clave, pasos) if clave < n.clave else buscar(n.der, clave, pasos)

def minimo(n):
    while n.izq is not None: n=n.izq
    return n
 
def maximo(n):
    while n.der is not None: n = n.der
    return n
 
def eliminar(n,clave):
    if n is None: return None
    if clave<n.clave: n.izq=eliminar(n.izq,clave)
    elif clave>n.clave: n.der=eliminar(n.der,clave)
    else: #encontramos el nodo a eliminar
        if n.izq is None: return n.der
        if n.der is None: return n.izq
        suc=minimo(n.der)
        n.clave=suc.clave              # <-- quitado n.nombre
        n.der=eliminar(n.der,suc.clave)
    recalc(n)                          # <-- agregado
    return n



raiz = None
for x in [10, 2, 1, 3, 4, 16, 13, 12, 14, 15, 18, 17]:
    raiz = insertar(raiz, x)

#                   10
#               /         \
#             2           16  
#           /   \       /    \ 
#           1    3     13     18
#                 \   /  \    /  
#                 4  12  14  17 
#                         \   
#                          15                                          
#
#
#
#
#
#
#
#
#
ver("INICIAL", raiz)                      

# Eliminacion
raiz = eliminar(raiz, 1)


#                10
#             /      \
#           2          16 #como quedo despues de eliminar 1
#            \        /   \
#             3     13     18
#              \   /  \    /
#              4  12  14  17
#                       \
#                       15
ver("ELIMINAR 1", raiz)



# Rotacion en el nodo desbalanceado mas profundo (el 2, hijo izquierdo de la raiz)
caso = diagnosticar(raiz.izq) 
print("Diagnostico en 2:", caso)          
raiz.izq = rotar(raiz.izq, caso)
#               10
#            /      \
#          3          16
#         / \        /   \
#        2   4     13     18 #estado del arbol despues de realizar la rotacion hacia la izquierda en 2 y como se puede ver 10 esta desbalan ceado porque la altura en su arbol izquierdo es 2 y en su rama derecha es  4
#                 /  \    /
#                12  14  17
#                      \
#                      15
recalc(raiz)
ver("ROTAR EN 2", raiz)                   



# La rotacion no alcanzo: hay otro nodo desbalanceado mas arriba
caso = diagnosticar(raiz)
print("Diagnostico en raiz:", caso)       
raiz = rotar(raiz, caso)
ver("ROTAR EN 10", raiz)
print("Diagnostico en raiz:", diagnosticar(raiz))   




