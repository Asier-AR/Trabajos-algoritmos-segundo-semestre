#Parte A — La cola de atención ( Implementen la cola de espera de su sistema, sobre lista enlazada, con encolar, desencolar, consultar el frente y saber cuántos hay. Encolar y desencolar deben costar O de uno los dos, y el tamaño también

class cola:
    class Nodo:
        def __init__(self, dato):
            self.dato= dato
            self.siguiente= None
    
    
    def __init__(self): self.frente = None; self.final = None; self.n = 0

    
    def encolar(self, x):
        nuevo = self.Nodo(x)
        if self.final is None: self.frente = self.final = nuevo   # cola vacia
        else: self.final.siguiente = nuevo; self.final = nuevo
        self.n += 1
 
    def desencolar(self):
        if self.frente is None: return None
        x = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None: self.final = None    
        self.n -= 1
        return x

    def Frente (self):
        if self.frente is None: 
            return None
       

        return self.frente.dato
    def Tamaño (self):
        contador=0
        if self.frente is None:
            return None
        else:
            return self.n
        
        


Cola= cola()
Cola.encolar(1)
Cola.encolar(2)


print (Cola.Frente())
Cola.Tamaño()

Cola.desencolar()
Cola.encolar(1)
Cola.encolar(4)
a=Cola.Tamaño()
for i in range(a):
    Cola.desencolar()

print(f"El tamaño de la cola es de {Cola.Tamaño()}")
print (f"El frente de la cola es el elemento {Cola.Frente()}")

for i in range (10):
    Cola.encolar(i)

print (f"El tamaño de la cola es de {Cola.Tamaño()}")
print (f"El frente de la cola es el elemento {Cola.Frente()}")