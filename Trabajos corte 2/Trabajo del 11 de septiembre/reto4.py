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




cedulas = [
    100001, 100002, 100003, 100004, 100005,
    100006, 100007, 100008, 100009, 100010,
    200011, 200012, 200013, 200014, 200015,
    200016, 200017, 200018, 200019, 200020,
    300021, 300022, 300023, 300024, 300025,
    400026, 400027, 400028, 400029, 400030
]

elemento_a_buscar=int(input("Ingrese la cedula que desea buscar "))

resultado_secuencial = busqueda_secuencial(cedulas, elemento_a_buscar)
resultado_binaria = busqueda_binaria(cedulas, elemento_a_buscar)

print("el primer elemento a buscar es: ", elemento_a_buscar) 
print ("-"*100)

elemento_a_buscar = 100001 
resultado_secuencial = busqueda_secuencial(cedulas, elemento_a_buscar)
resultado_binaria = busqueda_binaria(cedulas, elemento_a_buscar)
print("el segundo elemento a buscar es: ", elemento_a_buscar)
print ("-"*100)
