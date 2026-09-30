import time


#Parte B
#Implementen búsqueda secuencial y binaria sobre su colección de registros, contando comparaciones. Produzcan la tabla comparativa para cuatro casos: 
# el primer elemento, uno del medio, el último, y uno que no existe.


#usare los siguientes datos: 

cedulas = [
    100001, 100002, 100003, 100004, 100005,
    100006, 100007, 100008, 100009, 100010,
    200011, 200012, 200013, 200014, 200015,
    200016, 200017, 200018, 200019, 200020,
    300021, 300022, 300023, 300024, 300025,
    400026, 400027, 400028, 400029, 400030
]

cedulas1 = [
    200018, 100004, 400028, 200012, 100008, 
    300024, 100002, 200015, 400026, 100009, 
    200019, 300022, 100006, 300021, 200017, 
    100003, 400030, 200014, 100005, 300025, 
    200011, 400029, 100001, 200013, 100010, 
    300023, 200020, 400027, 200016, 100007
]

def busqueda_secuencial(lista, elemento):
    contador=1
    for i in range(len(lista)):
        if lista[i] == elemento:
            print(f"Cantidad de busquedas realizadas en la busqueda sequencial: {contador}")
            print(f"El elemento {elemento} se encuentra en el indice: {i}")
            print("-"*100)
            return 1
        
        contador+=1
    print(f"Cantidad de busquedas realizadas en la busqueda sequencial: {contador}")
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
            print("-"*100)
            return medio
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    print(f"Cantidad de busquedas realizadas en la busqueda binaria: {contador}")
    print("el elemento no se encuentra en la lista")
    return -1

print (("="*25),"Parte B","="*25)

elementoBuscar= cedulas [0]
busqueda_secuencial(cedulas,elementoBuscar)
busqueda_binaria(cedulas, elementoBuscar)

elementoBuscar= cedulas [int (len(cedulas)/2)]
busqueda_secuencial(cedulas,elementoBuscar)
busqueda_binaria(cedulas, elementoBuscar)

elementoBuscar=cedulas [len (cedulas)-1]
busqueda_secuencial(cedulas,elementoBuscar)
busqueda_binaria(cedulas, elementoBuscar)

elementoBuscar= -1
busqueda_secuencial(cedulas,elementoBuscar)
busqueda_binaria(cedulas, elementoBuscar)

#Parte C

#Los tres ordenamientos básicos Implementen Bubble, Selection e Insertion sobre sus registros, con contadores de comparaciones e intercambios. 
#Reporten los resultados con datos desordenados y con datos ya ordenados, y expliquen la diferencia.

def insertion_sort(arr):
    comparaciones=0
    desplazamiento=0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparaciones+=1
            if arr[j] > key:
            
                arr[j + 1] = arr[j]
                desplazamiento+=1
                j -= 1
            else:
                break

        arr[j + 1] = key
    print(f"Comparaciones realizadas selection sort:  {comparaciones}.")
    print(f"intercambios realizados por insertion sort: {desplazamiento}")
    return arr

def selection_sort(arr):
    n = len(arr)
    comparaciones = 0
    desplazamiento=0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparaciones += 1
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:  # evita intercambios innecesarios
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            desplazamiento+=1

    print(f"Comparaciones realizadas selection sort:  {comparaciones}.")
    print(f"Intercambios hechos por selection sort: {desplazamiento}")
    return arr

def bubble_sort_optimisado(arr):
    n = len(arr)
    comparaciones = 0
    desplazamiento= 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparaciones += 1  # Contador para medir las comparaciones
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                desplazamiento+=1
                swapped = True
        
        # Bandera: si no hubo intercambios en la pasada completa, corta
        if not swapped:
            break
    
    print(f"Comparaciones realizadas bubble sort:  {comparaciones}.")
    print(f"Intercambios realizados por buble sort: {desplazamiento}")
    return arr

print (("="*25),"Parte C","="*25)

print (("="*25),"Prueba con lista ordenadas","="*25)

print (("="*25),"Insertion sort","="*25)
insertion_sort(cedulas.copy())
print("")

print (("="*25),"Selection sort","="*25)
selection_sort(cedulas.copy())
print("") 

print (("="*25),"Bubble sort","="*25)
bubble_sort_optimisado(cedulas.copy())
print("")

print (("="*25),"Prueba con lista desordenada","="*25)

print (("="*25),"Insertion sort","="*25)
insertion_sort(cedulas1.copy())
print("")

print (("="*25),"Selection sort","="*25)
selection_sort(cedulas1.copy())
print("") 

print (("="*25),"Bubble sort","="*25)
bubble_sort_optimisado(cedulas1.copy())
print("")

#La diferencia entre los 3 es que insertion sort hace la misma cantidad de intercambios que bubble sort, pero con una menor cantidad de comparaciones.
#mientras que selection sort hace la mayor cantidad de comparaciones pero la menor cantidad de intercambios

# Parte D:

# Un ordenamiento avanzado y la medición Implementen Merge o Quicksort, midan el tiempo contra uno de los básicos para tres tamaños distintos de entrada 
# y produzcan la tabla. En el archivo de respuestas, expliquen en cinco líneas por qué los tiempos crecen distinto.

print (("="*25),"Parte D","="*25)

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
def bubble_sort_optimisadoSinPrints(arr): #es un buble sort que no printea las comparaciones
    n = len(arr)
    comparaciones = 0
    desplazamiento= 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparaciones += 1  # Contador para medir las comparaciones
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                desplazamiento+=1
                swapped = True
        
        # Bandera: si no hubo intercambios en la pasada completa, corta
        if not swapped:
            break
    

    return arr

tamano_1 = [
    100004, 200018, 100002, 200012, 100009, 
    200015, 100006, 200019, 100001, 200011, #lista de 20 elementos
    100008, 200020, 100003, 200014, 100010, 
    200017, 100005, 200016, 100007, 200013
]

tamano_2 = [
    300028, 100005, 200014, 400039, 100002, 
    200020, 300021, 100009, 400034, 200011, 
    300025, 100008, 400037, 200018, 100001, 
    300029, 200016, 400040, 100004, 300023, 
    200012, 400032, 100007, 300030, 200019,  #lista de 40 elementos
    400036, 100003, 200015, 300022, 400031, 
    100010, 200017, 300026, 400035, 100006, 
    200013, 300027, 400038, 300024, 400033
]

tamano_3 = [
    500052, 200014, 100003, 400038, 300021, 
    600060, 200018, 500043, 100009, 300027, 
    400032, 600055, 100001, 500049, 200012, 
    300025, 400036, 600058, 200020, 100007, 
    500041, 300023, 400034, 600051, 100005, 
    200016, 500047, 300029, 400040, 600054, 
    200011, 100002, 500045, 300022, 400031,  #lista de 60 elementos
    600057, 100008, 200019, 500050, 300028, 
    400037, 600053, 200015, 100004, 500044, 
    300026, 400035, 600059, 100010, 200017, 
    500048, 300030, 400033, 600052, 100006, 
    200013, 500042, 500046, 400039, 600056
]

print (("="*25),"Tamaño 1","="*25)
print("")

inicio= time.perf_counter()
quicksort(tamano_1.copy())
final= time.perf_counter()
duracion=final-inicio 

inicio1=time.perf_counter()
bubble_sort_optimisadoSinPrints(tamano_1.copy())
final1= time.perf_counter()
duracion1=final1-inicio1

print(f"Tiempo que le tomo al quicksort: {duracion:.10f}" )
print(f"Tiempo que le tomo al bubble sort: {duracion1:.10f}")

print (("="*25),"Tamaño 2","="*25)
print("")

inicio= time.perf_counter()
quick_sort(tamano_2.copy())
final= time.perf_counter()
duracion=final-inicio 

inicio1=time.perf_counter()
bubble_sort_optimisadoSinPrints(tamano_2.copy())
final1= time.perf_counter()
duracion1=final1-inicio1

print(f"Tiempo que le tomo al quicksort: {duracion:.10f}" )
print(f"Tiempo que le tomo al bubble sort: {duracion1:.10f}")

print (("="*25),"Tamaño 3","="*25)
print("")

inicio= time.perf_counter()
quick_sort(tamano_3.copy())
final= time.perf_counter()
duracion=final-inicio 

inicio1=time.perf_counter()
bubble_sort_optimisadoSinPrints(tamano_3.copy())
final1= time.perf_counter()
duracion1=final1-inicio1

print(f"Tiempo que le tomo al quicksort: {duracion:.10f}" )
print(f"Tiempo que le tomo al bubble sort: {duracion1:.10f}")

#Los tiempos crecen distintos por la complejidad de ambas funciones (aunque tambien depende del tipo de equipo que corra el codigo)
# porque la complejidad de bubble sort es de O(n al cuadrado en todos sus casos 
# y Quick sort tiene una complejidad de O(n log n) en su caso promedio y en su peor de O(n al cuadrado)
# en conclucion la mayoria de veces el trabajo que va a hacer bubble va a crecer 4 veces y el de quick sort n*log n


#Parte E

#Midan el algoritmo desarrollado, en los dos lenguajes, y hagan la tabla con la columna de factor.
#Escriban el párrafo que interpreta esa tabla. No basta pegarla: hay que decir qué significa. 
# Si el factor da dos, digan que es O de n y que coincide con lo esperado. Si no coincide, digan por qué creen que no.

#Parte F

#Un equipo de desarrollo tiene implementado el mismo algoritmo en Python y C++. 
# Ambos proyectos utilizan GitHub y quieren automatizar un proceso de Integración Continua y Entrega Continua (CI/CD).

#El equipo propone el siguiente flujo:

#git push → ejecutar programa → pruebas → compilar → desplegar

#Uno de los integrantes afirma:

#“En Python no necesitamos Integración Continua porque Python no requiere compilación; CI/CD es principalmente para lenguajes como C++.”

#Pregunta:

#¿Estás de acuerdo con esta afirmación? Explica por qué y propón cómo debería ser un pipeline de CI/CD para el proyecto en Python y otro para C++.

#No estoy de acuerdo con esta afirmacion ya que el CI  no es solo para compilar si no que tambien sirve para hallar problemas de compatibilidad.
#realizar pruebas en busca de erroes, hallar problemas de compilacion entre otros por lo tanto el CI sigue siendo necesario

#Python

# Primero hacer push al repo → ejecutar el programa → realizar pruebas especificas para buscar erres → desplegar el codigo 

#C++

#Primero hacer push al repo → compilar el programa → realizar pruebas especificas para buscar errores→ desplegar el codigo

#Como implementarioa CD/CI para este laboratorio

#yo lo implementaria con el siguiente pipe line