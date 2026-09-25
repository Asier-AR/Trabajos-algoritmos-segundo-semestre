import time
def bucket_sort(arr, numBuckets=5):
    contador=0
    if len(arr) == 0: #revisa que el arreglo no este vacio
        return arr

    min_value = min(arr) #agarra el valor mas pequeño de la lista
    max_value = max(arr) #agarra el valor mas grande de la lista
    bucket_range = (max_value - min_value) / numBuckets#determina el rango que es igual a la resta del valor mas grande con el valor mas pequeño dividiendolo en la longitud del arreglo

    buckets = [[] for _ in range(numBuckets)] #crea una lista de listas cuya cantidad de listas en su interior va a ser igual a los elementos en la listas

    for num in arr: 
        contador+=1
        index = int((num - min_value) / bucket_range)
        if index ==numBuckets: #se asegura que el indice no sea igual a la longitud de la lista y lo reduce para evitar errores
            index -=1
        buckets[index].append(num) #añade el numero del arreglo en una de las cubetas

    sorted_arr = [] #el arreglo ordenado
    for bucket in buckets: #recorre todas las cubetas en la lista cubetas
        contador+=1
        sorted_arr.extend(sorted(bucket)) #une las cubetas en el arreglo de forma ordenada
    print (f"el numero de iteraciones fue de {contador}")
    return sorted_arr


lista=[1,4,5,6,7,1,23,51,61,23,51,32,5,6,1,4,5,6,7,1,23,51,61,23,51,32,5,6]
inicio=time.perf_counter()
ordenado=bucket_sort(lista)
final=time.perf_counter()

duracion= final- inicio
print (ordenado)
print(f"le tomo {duracion} segundos en hacer la funcion")


inicio=time.perf_counter()
ordenado2=bucket_sort(lista, 20)
final=time.perf_counter()

duracion=final-inicio

print(ordenado2)
print(f"le tomo {duracion} en hacer el proceso")


# 1 que es n en esa secuencia 
# N  vendria siendo la cantidad de elementos que se le pasa a esa secuencia
# 2 Cuantas veces se ejecuta el proceso si se duplican los datos
# Se jecuta un poco menos del doble si se duplican los datos
# 3 Dentro de la secuensia se invoca otro proceso, cuantos procesos se invocan
# Se invoca el sort por cada cubeta que se crea, por lo que si se crean 5 cubetas se invoca 5 veces el sort y si se crean 20 cubetas se invoca 20 veces el sort
# 4  que sitpo de estrucutura de datos se utiliza 
# se utilizan arrelos o listas

