import random

valor = int(input("Ingrese el valor de su compra "))

while valor < 0:
    print("No se puede tener un valor negativo ingrese un valor valido")
    valor = int(input())

if valor > 50000:
    print("precio minimo alcanzado realizando giro de ruleta")
    numeroAleatorio1 = random.randint(1, 4)  # Genera un número aleatorio entre 1 y 4

    if numeroAleatorio1 == 1:
        print("Has sacado la bolita roja descuento de 10%")
        valorFinal = valor - (valor * 0.1)

    elif numeroAleatorio1 == 2:
        print("Has sacado la bolita azul descuento de 30%")
        valorFinal = valor - (valor * 0.3)

    elif numeroAleatorio1 == 3:
        print("Has sacado la bolita amarilla descuento de 50%")
        valorFinal = valor - (valor * 0.5)

    elif numeroAleatorio1 == 4:
        valorFinal = 0

    print("El precio inicial era de", valor, "$ pero despues del descuento tendra que pagar", valorFinal, "$")

else:
    print ("No se ha alcanzado el umbral minimo su compra es de", valor, "$")