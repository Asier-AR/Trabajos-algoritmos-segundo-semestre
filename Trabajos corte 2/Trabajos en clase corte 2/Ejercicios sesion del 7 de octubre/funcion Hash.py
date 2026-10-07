import random  


def funcionHash(cadena):
    valor=0
    p=31
    for i in range(len(cadena)):
        valor += (ord(cadena[i]) - ord('a') + 1) * (p ** i)
    return valor % 1000
print(funcionHash("ana"))
print (funcionHash("naa"))
