def binaria_recursiva(v, x, izq=0, der=None):
    if der is None:
        der = len(v) - 1 #el lado derecho se suele inicializar en none

    # Caso base: el elemento no se encuentra en el arreglo
    if izq > der: #ya habra recorrido todos los elementos de la lista para este momento
        return izq #esto se debe a que llegado a ese momento todo lo que este a la izquierda del indice izq va a ser menor que x y todo lo que este a la derecha del indice izq incluyen izq va a ser mayor o igual a X
        #ademas tambien retornara la primera ocurrencia de X
    medio = (izq + der) // 2 #saca el indice de la mitad de la lista
    # Descartar la mitad izquierda (buscar a la derecha)
    if v[medio]>=x: #elimina el costado derecho y evita que la funcion se detenga al encontrar la primera ocurrencia de X
            return binaria_recursiva(v, x, izq, medio - 1)

    else: #elimina el costado izquierdo y se asegura de que la funcion no se detenga al encontrar la primera ocurrencia de XD
        return binaria_recursiva(v, x, medio + 1, der)
    # Descartar la mitad derecha (buscar a la izquierda)

miLista=[1, 2, 2, 3, 2, 4]
numeroAbuscar=0
indice=binaria_recursiva(miLista, numeroAbuscar)

if miLista[indice]==numeroAbuscar:
    print(f"la primera ocurrencia del numero: {numeroAbuscar} ocurre en el indice: indice")

else:
     print(f"el elemento que desea buscar no se encuentra en la lista pero si estuviera deberia estar ubicado en el indice: {indice}")