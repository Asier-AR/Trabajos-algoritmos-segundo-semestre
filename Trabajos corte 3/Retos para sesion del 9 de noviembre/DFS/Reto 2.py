ASIGNATURAS = ["Calculo", "Programacion", "Fisica", "Algoritmos", "Precalculo", "Logica"]
# u -> v significa "u es prerrequisito de v"
ARISTAS = [[0, 1], [1, 2], [2, 3], [3, 4],
           [4, 5],[5,0]]          # el ultimo cierra el ciclo a proposito
N = 6

lista = [[] for _ in range(N)]
for u, v in ARISTAS:
    lista[u].append(v)              # dirigido: solo un sentido
for v in lista:
    v.sort()

SIN_VISITAR, EN_PROCESO, TERMINADO = 0, 1, 2

def hay_ciclo():
    estado = [SIN_VISITAR] * N
    camino = []                      # vertices en proceso, en orden

    def explorar(u):
        estado[u] = EN_PROCESO
        camino.append(u)
        for v in lista[u]:
            if estado[v] == EN_PROCESO:
                # v esta en el camino actual: el ciclo va de v hasta u y vuelve a v
                return camino[camino.index(v):] + [v]
            if estado[v] == SIN_VISITAR:
                ciclo = explorar(v)
                if ciclo:
                    return ciclo
        camino.pop()
        estado[u] = TERMINADO
        return None

    for s in range(N):
        if estado[s] == SIN_VISITAR:
            ciclo = explorar(s)
            if ciclo:
                return ciclo
    return None


ciclo = hay_ciclo()
if ciclo:
    print("Ciclo encontrado:", " -> ".join(ASIGNATURAS[i] for i in ciclo))
else:
    print("El plan de estudios es valido (sin ciclos)")