class inventario:
    class Pila:
    
        def __init__(self):self.items = []
        def apilar(self,x):self.items.append(x)
        def desapilar(self):
            if self.vacia():return None
            return self.items.pop()
        def cima(self):return None if self.vacia() else self.items[-1]
        def vacia(self):return len(self.items) == 0
    
    
    def __init__(self, elementos=None):
        self.lista=elementos if elementos is not None else {}
        self.historial=self.Pila()

    def Existe(self, Nombre):
        if Nombre not in self.lista:
            return False
        else: return True

    def agregarElemento(self, Nombre, Precio, Cantidad):
        existe=self.Existe(Nombre)
        if existe:
            self.lista[Nombre]["cantidad"]+=Cantidad

        else: self.lista[Nombre]={"precio": Precio, "cantidad": Cantidad}
        self.historial.apilar(("agregar", Nombre, Precio, Cantidad, existe))

    def mostrarInventario(self):
        for i in self.lista:
            print(f"Nombre: {i}")
            print (f"Precio: {self.lista[i]["precio"]}")
            print (f"Cantidad: {self.lista[i]["cantidad"]}")
            print ("-"*50)
        

  

    def venta(self,Nombre, cantidad):
        if not self.Existe or self.lista[Nombre]["cantidad"]<cantidad:
            print("No existe el articulo o no hay suficiente stock ")
            return        

        self.lista[Nombre]["cantidad"]-=cantidad
        self.historial.apilar(("venta", Nombre, cantidad))

    def ultimaAccion(self):
        print (f"La ultima accion fue: {self.historial.cima()}")
        print ("")
    def revertir (self):
        if self.historial.vacia():
            print("No hay ninguna accion guardada")
            return
        registro=self.historial.desapilar()

        if registro[0]=="agregar":
            _, Nombre, Precio, Cantidad, Existe=registro

            if Existe== True:
                self.lista[Nombre]["cantidad"]-=Cantidad
            else:
              del self.lista[Nombre]
        elif registro[0]=="venta":
            _, Nombre, Cantidad=registro

            self.lista[Nombre]["cantidad"]+=Cantidad

registro= {"Manzana": { "precio": 1500,"cantidad": 10}, "Pera":{"precio": 1500, "cantidad": 20} }
Inventario= inventario(registro)

Inventario.ultimaAccion()

Inventario.agregarElemento("Manzana", 1500, 10)
Inventario.mostrarInventario()
Inventario.ultimaAccion()
Inventario.venta("Manzana", 10)
Inventario.ultimaAccion()
Inventario.mostrarInventario()
Inventario.revertir()
Inventario.ultimaAccion()

