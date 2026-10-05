


#entrada: [73, 74, 75, 71, 69, 72, 76, 73]
#salida: [1,1,4,2,1,1,0,0]
#decreciente

def dailyTemperatures(T):
    n = len(T)
    res = [0] *n #crea una lista que de n elementos con valor 0
    pila = [] #pila para almacenar los índices
    
    for i in range(n):
        while pila and T[i] > T[pila[-1]]: #revisa que la pila no esté vacía y que la temperatura actual sea mayor que la temperatura en el índice almacenado en la cima de la pila
            idx = pila.pop() #saca el índice de la cima de la pila
            res[idx] = i - idx #calcula la diferencia entre el índice actual y el índice almacenado en la cima de la pila y lo asigna a la posición correspondiente en la lista res
        pila.append(i) #si no se cumple la condición, agrega el índice actual a la pila
    
    return res

miLista = [73, 74, 75, 71, 69, 72, 76, 73]

print (dailyTemperatures(miLista))