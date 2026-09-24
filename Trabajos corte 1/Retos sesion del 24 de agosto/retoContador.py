class objeto:
    contador=0
    def __init__(self): #constructor de la clase que se efectua de forma automatica cada que se crea un nuevo objeto
        objeto.contador+=1
    def obtenerContador(self):
        return objeto.contador





objeto1=objeto()
objeto2=objeto()
objeto3=objeto()
print (objeto1.obtenerContador())
print (objeto2.obtenerContador() )