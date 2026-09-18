def sumaLista (lista):
    if len(lista)==0:
        return 0
    else:
        i=lista.pop(0)
        return i+ sumaLista(lista)

lista=[100, 4, 575, 624, 657, 18, 777, 845, 28, 29]

print (sumaLista(lista.copy()))