#Parte A

# 1 Tengo mil datos ya ordenados y quiero ordenarlos otra vez. ¿Cuál de los tres básicos hace menos trabajo y por qué?
# Dependiendo de como se configure el basico que realizaria menos trabajo seria el buble sort (si este esta optimisado)
# ya que si este se configura con una bandera que revise si se realiza un cambio, solo recorreria la lista una ves  y al ver que no se hicieron cambios dejaria de recorrerla

# 2 Mi Quicksort escoge el primer elemento como pivote. Denme un conjunto de datos que lo haga comportarse pésimo.

# tomare en cuenta que el quicksort esta configurado para crear listas es decir de la siguiente manera

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    

# Los datos que harian que el quicksort se comporte pesimo serian: [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# Esto ocurre porque el 20 es el elemento maximo de toda la lista cosa que haria que todos los elementos menos el 20 se fueran al arreglo izquierdo y el 20 quedaria en el arreglo 
# y lo mismo pasarian con todos demas numeros que pertenecen a la lista y esto haria que el algoritmo pierda una gran parte de su eficiencia
# cabe aclarar que esto pasara con cualquier lista ordenada o inversamente ordenada 


# Quiero buscar cien veces sobre una colección de diez mil elementos desordenados. ¿Ordeno primero y uso binaria, o busco secuencial cien veces? Justifiquen.
# Lo mas eficiente seria ordenar la lista y usar la busqueda binaria cien veces ya que este procedimiento realizaria muchos menos pasos
# que usar la busqueda secuencial 100 veces ya que basicamente recorrerias 100 veces un arreglo de 10.000 elementos que en el peor de los casos te llevaria a recorrer 10.000*100 elementos en total


#Parte B
#Implementen búsqueda secuencial y binaria sobre su colección de registros, contando comparaciones. Produzcan la tabla comparativa para cuatro casos: el primer elemento, uno del medio, el último, y uno que no existe.


#usare los siguientes datos: 

cedulas = [
    100001, 100002, 100003, 100004, 100005,
    100006, 100007, 100008, 100009, 100010,
    200011, 200012, 200013, 200014, 200015,
    200016, 200017, 200018, 200019, 200020,
    300021, 300022, 300023, 300024, 300025,
    400026, 400027, 400028, 400029, 400030
]

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

elementoBuscar= [0]
busqueda_secuencial=(elementoBuscar)
busqueda_binaria(elementoBuscar)
elementoBuscar= [int (len(cedulas)/2)]
busqueda_secuencial=(elementoBuscar)
busqueda_binaria=(elementoBuscar)

