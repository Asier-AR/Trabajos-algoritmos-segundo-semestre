def potencia (a, b):
    if b==0:
        return 1
    elif b % 2==0:
        mitad=potencia(a, b/2) #este es el metodo que pidio la profesora
        return mitad*mitad
    else:
        return a* potencia(a, b-1)


base= 3

elevado= 12

print (potencia(base, elevado))