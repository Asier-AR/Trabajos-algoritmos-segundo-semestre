from collections import deque

NOMBRES = [
    "San Ignacio",
    "Santa Fe",
    "El Tunal",
    "Kennedy",
    "Country",
    "Militar Central",
]

ARISTAS = [(3,0), (3,2), (3,4), (0,1), (2,4), (4,5)]

N=6

def construir():
    lista=[[] for _ in range(N)]
    for u, v in ARISTAS:
        lista[u].append(v)
        lista[v].append(u)
    for vecinos in lista:
        vecinos.sort()
    return lista    

def bfs(inicio):
    visitado = [False] * N
    dist  = [-1] * N
    padre = [-1] * N
    lista=construir()
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
    return dist


for origen in range (N):
    distancias=bfs(origen)
    tiempo=max(distancias) 
    print(f"Tiempo para el fallo empezando en: {NOMBRES[origen]}")

    for v in range(N):
        print(f"{NOMBRES[v]}: minuto: {distancias[v]}")

    print(f"La red completa cae en {tiempo} minutos")





