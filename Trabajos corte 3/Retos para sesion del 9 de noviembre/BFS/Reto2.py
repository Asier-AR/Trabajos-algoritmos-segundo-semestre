#Reto 2 — Los grados de separación · Obligatorio Calcule, para cada par de vértices de su red, la distancia mínima entre ellos. 
# Reporte el diámetro de la red, que es la mayor de todas esas distancias, e identifique qué par de puntos lo produce.
#
#Pista: Un BFS desde cada vértice. Son V recorridos de O(V+E), es decir O(V·(V+E)) en total. Para redes pequeñas es perfectamente viable.

#Resultado esperado: El diámetro y el par de puntos más alejados. Interprete el resultado: ¿qué significa para la operación de su sistema?

from collections import deque

nombreEjemplo=["Central", "Claustro", "Norte", "Empresarial", "Emprendimiento", "Sureste"]

ARISTAS = [
    (0, 1),  # Central - Claustro
    (0, 2),  # Central - Norte
    (1, 2),  # Claustro - Norte
    (0, 3),  # Central - Empresarial
    (3, 4),  # Empresarial - Emprendimiento
    (3, 5),  # Empresarial - Sureste
]

N=6

def bfs(inicio, lista):
    visitado = [False] * N
    dist  = [-1] * N
    padre = [-1] * N
    cola = deque([inicio])
    visitado[inicio] = True
    dist[inicio] = 0
    orden = []
    while cola:
        u = cola.popleft()
        orden.append(u)
        for v in lista[u]:
            if not visitado[v]:
                visitado[v] = True
                dist[v]  = dist[u] + 1
                padre[v] = u
                cola.append(v)
    return orden, dist, padre

def construir():
    lista=[[] for _ in range(N)]
    for u, v in ARISTAS:
        lista[u].append(v)
        lista[v].append(u)
    for vecinos in lista:
        vecinos.sort()
    return lista    


lista = construir()
diametro = 0
pares = []
print("Distancia mínima por par:")
for i in range(N):
    _, dist, _ = bfs(i, lista)       # dist = distancias desde i a todos
    for j in range(i + 1, N):        # solo j > i: no dirigido, sin repetidos
        d = dist[j]
        print(f"  {nombreEjemplo[i]} - {nombreEjemplo[j]}: {d}")
        if d > diametro:             # nuevo máximo: reinicia la lista de pares
            diametro = d
            pares = [(i, j)]
        elif d == diametro and d > 0: 
            pares.append((i, j))
            
print(f"\nDiámetro de la red: {diametro}")
print("Pares que lo producen:")
for i, j in pares:
    print(f"  {nombreEjemplo[i]} - {nombreEjemplo[j]}")



