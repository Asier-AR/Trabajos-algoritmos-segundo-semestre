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

mejorOrden=[4, 2, 1, 3, 6, 5,  7] 
mejorOrden2=[4, 6, 5, 7, 2, 1, 3]
mejorOrden3=[4, 2, 6, 1, 5, 3, 7]

#en el caso del mejor orden para insertar nuestro arbol quedaria algo asi con cualquiera de los 3 ordenes anteriormente nombrados 


#                   4                                       
#                 /   \                 #lo que tienen en comun todos los ordenes es que el primero siempre es el 4 seguido del 2 0 el 6 ya despues de eso el orden de sus hijos es indiferente
#                2     6 
#               / \   / \
#              1   3 5   7

                            
                            
                            
                            
                            
                            

peorOrden=[1,2,3,4,5,6,7]

#en el caso del peor orden para insertar nuestro arbol quedaria algo asi 

#                     1 
#                      \ 
#                       2
#                        \
#                         3
#                          \
#                           4
#                            \
#                             5
#                              \
#                               6
#                                \
#                                 7



