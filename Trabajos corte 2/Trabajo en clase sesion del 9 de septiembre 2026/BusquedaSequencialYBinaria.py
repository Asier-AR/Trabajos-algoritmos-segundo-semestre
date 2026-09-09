def busqueda_secuencial(lista, elemento):
    contador=1
    for i in range(len(lista)):
        if lista[i] == elemento:
            print(f"Cantidad de busquedas realizadas en la busqueda sequencial: {contador}")
            print(f"El elemento {elemento} se encuentra en el indice: {i}")
            print("-"*50)
            return 1
        
        contador+=1

    print("el elemento no se encuentra en la lista")
    return -1

def busqueda_binaria(lista, elemento):
    izquierda = 0
    derecha = len(lista) - 1
    contador=1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        contador+=1
        if lista[medio] == elemento:
            print(f"Cantidad de busquedas realizadas en la busqueda binaria: {contador}")
            print(f"El elemento {elemento} se encuentra en el indice: {medio}")
            print("-"*50)
            return medio
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    print("el elemento no se encuentra en la lista")
    return -1


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 13, 14, 15,16, 17, 18, 19, 20]
elemento_a_buscar = 20

resultado_secuencial = busqueda_secuencial(lista, elemento_a_buscar)
resultado_binaria = busqueda_binaria(lista, elemento_a_buscar)

print("el primer elemento a buscar es: ", elemento_a_buscar) 
print ("-"*100)

elemento_a_buscar = 1
resultado_secuencial = busqueda_secuencial(lista, elemento_a_buscar)
resultado_binaria = busqueda_binaria(lista, elemento_a_buscar)
print("el segundo elemento a buscar es: ", elemento_a_buscar)
print ("-"*100)

