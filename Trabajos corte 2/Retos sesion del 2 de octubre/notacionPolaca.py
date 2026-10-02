class Pila:
    def __init__(self):self.items = []
    def apilar(self,x):self.items.append(x)
    def desapilar(self):
        if self.vacia():return None
        return self.items.pop()
    def cima(self):return None if self.vacia() else self.items[-1]
    def vacia(self):return len(self.items) == 0

#se va a evaluar la expresion 3+5 que en notacion polaca se escribiria 3 5 +


 







def lector(pila):
    elemento=pila.desapilar()
    if elemento in ("+", "-", "*", "/"):
        derecho= lector(pila)
        izquierdo= lector (pila)
    if elemento=="+":
        return  izquierdo+derecho
    elif elemento=="-":
        return izquierdo- derecho
    elif elemento=="*":
        return izquierdo * derecho
    elif elemento=="/":
        return izquierdo / derecho

    return float(elemento) #es por la division
    


ejemplo=Pila()

ejemplo.apilar(3)
ejemplo.apilar(5)
ejemplo.apilar("-")
ejemplo.apilar(6)
ejemplo.apilar("*")
ejemplo.apilar(1)
ejemplo.apilar("+")

print (lector(ejemplo))
    

        

