def binaria_recursiva(v, x, izq=0, der=None):
    if der is None:
        der = len(v) - 1 #el lado derecho se suele inicializar en none

    # Caso base: el elemento no se encuentra en el arreglo
    if izq > der: #ya habra recorrido todos los elementos de la lista para este momento
        return izq, False #esto se debe a que llegado a ese momento todo lo que este a la izquierda del indice izq va a ser menor que x y todo lo que este a la derecha del indice izq incluyen izq va a ser mayor o igual a X

    medio = (izq + der) // 2 #saca el indice de la mitad de la lista

    # Caso base: elemento encontrado
    if v[medio] == x: #devuelve el indice del elemento
        return medio, True
    # Descartar la mitad izquierda (buscar a la derecha)
    elif v[medio] < x:
        return binaria_recursiva(v, x, medio + 1, der)
    # Descartar la mitad derecha (buscar a la izquierda)
    else:
        return binaria_recursiva(v, x, izq, medio - 1)



lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

elementoBuscar=0

indiceElemento, estaLista=binaria_recursiva(lista, elementoBuscar)

if estaLista==True:

    print(f"el elemento : , {elementoBuscar} se encuentra en el indice {indiceElemento} de la lista") 

elif estaLista==False:
    print(f"El elemento buscado no se encuentra en la lista pero si estuviera deberia estar en el indice:  {indiceElemento}")