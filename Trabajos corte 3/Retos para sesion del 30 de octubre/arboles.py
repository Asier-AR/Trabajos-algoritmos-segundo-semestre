class Nodo:
    def __init__(self, clave, nombre=""):
        self.clave = clave; 
        self.nombre = nombre
        self.izq = None; 
        self.der = None
        
def insertar(n, clave, nombre=""):
    if n is None: return Nodo(clave, nombre)
    if clave < n.clave: n.izq = insertar(n.izq, clave, nombre)   # el retorno se REENGANCHA
    elif clave > n.clave: n.der = insertar(n.der, clave, nombre)
     # clave repetida: no se inserta
    return n

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
 
def eliminar(n, clave):
    if n is None: return None
    if clave < n.clave: n.izq = eliminar(n.izq, clave)
    elif clave > n.clave: n.der = eliminar(n.der, clave)
    else: #encontramos el nodo a eliminar
        if n.izq is None: return n.der
        if n.der is None: return n.izq
        suc=minimo(n.der)
        n.clave,n.nombre=suc.clave,suc.nombre
        n.der=eliminar(n.der,suc.clave)
    return n
def inorden(n, s):
    if n is None: return
    inorden(n.izq, s); s.append(n.clave); inorden(n.der, s)
    
def altura(n):
    if n is None: return -1
    return 1 + max(altura(n.izq), altura(n.der))

def listarOrdenado(n): #imprime el codigo y nombre empezando primero por la rama izquierda para luego imprimir el codigo y nombre de la raiz y por ultimo hacer lo mismo con la rama derecha
    if n is None: return
    listarOrdenado(n.izq)
    print(f"{n.clave} - {n.nombre}")
    listarOrdenado(n.der)

def informeCodigo(n, codigo):
    pasos=[]
    r=buscar(n, codigo, pasos)

    comparaciones=len(pasos)if r else len(pasos)-1 #se elimina la comparacion que se hace al final cuando el arbol ya es vacio porque en teoria en ese momento no se hace ninguna comparacion real

    if r:
        print(f"{r.nombre} ({comparaciones} comparaciones)")
    else:
        print(f"Código {codigo} no encontrado ({comparaciones} comparaciones)")

def enRango(n, a, b):
    if n==None: return  0
    visitados= 1 #inicia en uno porque se visita el nodo raiz

    if n.clave>a: #si la clave es mayor que a pasara  a recorrer su lado izquierdo en ya que ahi se guardan los valores mas pequeños que la clave
        visitados+= enRango(n.izq, a, b)

    if a<= n.clave<=b: #si la clave se encuentra entre los 2 printeara su clave
        print(n.clave)

    if n.clave<b: #si la clave es menor que b, va a buscar en los nodos derechos que son los mayores a la clave
        visitados+=enRango(n.der, a, b)

    return visitados

def esBST(n, inferior=None, superior=None):
    if n is None: return True

    if inferior is not None and n.clave<=inferior: return False

    if superior is not None and n.clave>=superior: return False

    return esBST(n.izq, inferior, n.clave) and esBST(n.der, n.clave, superior)



# -----------------------------INICIO DEL MAIN--------------------------------------------------------------------------------------------------------------------------------------------


raiz=None

objetos=[[3 , "matemáticas discretas"],
         [2 , "cálculo integral"],
         [1 , "inteligencia artificial"],
         [4 , "álgebra lineal"],
         [10 , "computador portátil dell"],
         [8 , "macbook pro"],
         [7 , "ipad air"],
         [6 , "calculadora científica"],
         [5 , "raspberry pi 4"],
         [9 , "mouse"]]

for objeto in objetos:
    raiz=insertar(raiz, objeto[0], objeto[1])


listarOrdenado(raiz)
informeCodigo(raiz, 7)
informeCodigo(raiz, 99)

visitados=enRango(raiz, 5, 10)

print(f"nodos visitados: {visitados}")

malo = Nodo(50)
malo.izq = Nodo(30)
malo.izq.der = Nodo(60)
print(esBST(malo))      # False  (correcto)
print(esBST(raiz))      # True   (tu árbol de recursos)

