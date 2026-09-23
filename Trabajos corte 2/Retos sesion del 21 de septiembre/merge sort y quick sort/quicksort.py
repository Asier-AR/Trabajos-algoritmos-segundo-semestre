def quicksort(arr, bajo=0, alto=None):
    if alto is None:
        alto = len(arr) - 1
    if bajo < alto:
        p = particionLamuto(arr, bajo, alto) #elegimos el pivote
        quicksort(arr, bajo, p - 1)
        quicksort(arr, p + 1, alto)

def particionLamuto(arr, bajo, alto  ): #es un metodo para no crear listas y es un poco mas facil de comprender
    pivote=arr[alto] #elegimos el pivote como el ultimo elemento del arreglo
    i=bajo-1         #frontera de menores que el pivote

    for j in range (bajo, alto):
        if arr[j]<=pivote:
            i+=1
            arr[i], arr[j]= arr[j], arr[i] #aqui realizamos el cambio

    arr[i+1], arr[alto]= arr[alto], arr[i+1] #coloca el pivote en su lugar
    return i+1


def particionHoare(arr, bajo, alto): #es otro metodo para no crear mas listas pero es un poco mas confuso
    pivote=arr[bajo] #agarramos el primer elemento de la lista
    i,j =bajo-1, alto+1
    while True:
        i += 1
        while arr[i] < pivote:
            i += 1
        j -= 1
        while arr[j] > pivote:
            j -= 1
        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]





lista1=[2,2,3,2,2,0]
quicksort(lista1)

print (lista1)