import time




# ---------- 9 vertices: grilla tablero 3x3 ----------


CASILLAS9=[ "A1","B1","C1",
            "A2","B2","C2",
            "A3","B3","C3"]
N9 = 9
ARISTAS9 = [(0,1),(1,2),(3,4),(4,5),(6,7),(7,8),
            (0,3),(3,6),(1,4),(4,7),(2,5),(5,8)]

# ---------- 15 vertices: tablero 3x5 (22 aristas) ----------
N15 = 15

CASILLAS15=[ "A1","B1","C1","D1", "E1", 
            "A2","B2","C2","D2", "E2", 
            "A3","B3","C3", "D3", "E3"]

ARISTAS15 = [(0,1),(1,2),(2,3),(3,4),
             (5,6),(6,7),(7,8),(8,9),
             (10,11),(11,12),(12,13),(13,14),
             (0,5),(5,10),(1,6),(6,11),(2,7),(7,12),
             (3,8),(8,13),(4,9),(9,14)]

# ---------- 20 vertices: tablero 4x5 (31 aristas) ----------
CASILLAS20=[ "A1","B1","C1","D1","E1",
            "A2","B2","C2","D2","E2", 
            "A3","B3","C3","D3","E3",
            "A4","B4","C4","D4","E4"]
N20 = 20
ARISTAS20 = [(0,1),(1,2),(2,3),(3,4),
             (5,6),(6,7),(7,8),(8,9),
             (10,11),(11,12),(12,13),(13,14),
             (15,16),(16,17),(17,18),(18,19),
             (0,5),(5,10),(10,15),
             (1,6),(6,11),(11,16),
             (2,7),(7,12),(12,17),
             (3,8),(8,13),(13,18),
             (4,9),(9,14),(14,19)]

def constructorLista(Aristas, N):
    lista=[[]for _ in range(N)]

    for u, v in Aristas:
        lista[u].append(v)
        lista[v].append(u)
    return lista

def camino_mas_largo(lista, origen, destino):
    mejor = []                       
    visitado = [False] * len(lista)
    camino = []

    def dfs(u):
        visitado[u] = True
        camino.append(u)
        if u == destino:
            if len(camino) > len(mejor):
                mejor[:] = camino    # reemplaza el contenido de toda la lista gracias a los [:]
        else:
            for v in lista[u]:
                if not visitado[v]:
                    dfs(v)
        camino.pop()
        visitado[u] = False          # backtracking: libera el vertice

    dfs(origen)
    return mejor

def escritor(camino, Casillas):
    contador=len(camino)
    print("Camino mas largo: ", end="")
    for numero in camino:
        contador-=1
        if contador> 0:
            print(f"{Casillas[numero]} -> ", end="")
            
        else:
            print(f"{Casillas[numero]}")
        


listaVertice= constructorLista(ARISTAS20, N20)

inicio = time.perf_counter()
camino = camino_mas_largo(listaVertice, 0, 19)
fin = time.perf_counter()

print(f"Tiempo: {fin - inicio:.4f} segundos")

escritor(camino, CASILLAS20)

# Con aristas 9 me dio un total de 0.00001 segundos
# con aristas 15 el tiempo fue de  0.0009  segundos
# con asistas 20 el tiempo de fue de  0.0015 segundos

#la razon por la que el camino mas corto es un problema mas sencillo que el del camino largo es porque, al moverte alrededor de grafo, no hace falta recorrer el camino completo
# para determinar si el nuevo camino es mas corto debido a que simplemente dejas de moverte una ves recorres una mayor cantidad de nodos en cambio en el camino mas largo si es
# necesario recorrer todos los caminos posibles para concluir que X camino es el mas largo