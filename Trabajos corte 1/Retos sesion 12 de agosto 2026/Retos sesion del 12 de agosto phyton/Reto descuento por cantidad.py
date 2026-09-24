cantidad=int(input("Ingrese la cantidad de productos que va a comprar "))
valorTotal=0
for i in range(cantidad):
    nombreProducto=str(input("ingrese el nombre del producto ")) 
        

    precioUnitario=int(input("Ingrese el precio unitario "))
        

    cantidadCompra=int(input("Ingrese la cantidad comprada "))

    subtotal=precioUnitario* cantidadCompra #operacion para encontrar el subtotal 
    valorTotal=valorTotal + subtotal #acumula el subtotal de los productos para hallar el valor total
        
    #la razon por la que no guardo los nombres es porque el reto no estipula que sea necesario mostrarselos al cliente

if (valorTotal>300000):
    
    print("Aplicando descuento del 10%")

    valorFinal= valorTotal-(valorTotal*0.1)

    print("El valor antes del descuento era de ", valorTotal, "$ y despues del descuento es de ", valorFinal, "$ ")
    

elif (valorTotal<=300000 and valorTotal>=150000):
    
    print ("Aplicando descuento del 5%")

    valorFinal= valorTotal-(valorTotal*0.05)

    print ("El valor antes del descuento era de ", valorTotal, "$ y despues del descuento es de ", valorFinal, "$ ")
    

else: 
    
    print ("El valor de su compra es de ", valorTotal, "$")
