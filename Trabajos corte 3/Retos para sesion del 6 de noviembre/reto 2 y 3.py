def matrizALista(m):
    n = len(m)
    lista = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if m[i][j] == 1:
                lista[i].append(j)   # la simetría de m hace el resto
    return lista

def listaAmatriz(l):
    n=len(l)
    m=[[0]*n for _ in range(N)] #creamos la matriz
    for i in range (n):
        for j in l[i]:
            m=[i][j]=1
    return m


#Reto 2 — El converso · Obligatorio Escriba matrizALista(m) y listaAMatriz(l) que conviertan una representación en la otra. 
#Verifique que convertir ida y vuelta devuelve el original. 
#Pista: La verificación de ida y vuelta es la prueba más barata y más efectiva que existe para este tipo de funciones. 
#Escríbala antes que las conversiones. Resultado esperado: listaAMatriz(matrizALista(m)) debe ser igual a m para cualquier m válida.


from grafo_base import NOMBRES, ARISTAS, N

# ---------- Representacion 1: matriz de adyacencia ----------
matriz = [[0]*N for _ in range(N)] #crea una matriz llena de 0 con N cantida de filas y N cantida de columnas
for u, v in ARISTAS: #coada U y V presente en aristas marca las matrizes con un 1
    matriz[u][v] = 1
    matriz[v][u] = 1              # grafo NO dirigido: la matriz es simetrica

print("MATRIZ DE ADYACENCIA")
print("            " + " ".join(f"{n[:3]:>4}" for n in NOMBRES))
for i in range(N): 
    print(f"{NOMBRES[i]:>11} " + " ".join(f"{matriz[i][j]:>4}" for j in range(N)))

# ---------- Representacion 2: lista de adyacencia ----------
lista = [[] for _ in range(N)]
for u, v in ARISTAS:
    lista[u].append(v)
    lista[v].append(u)
for v in lista: v.sort()

print("\nLISTA DE ADYACENCIA")
for i in range(N):
    print(f"  {NOMBRES[i]:>10} -> {', '.join(NOMBRES[j] for j in lista[i])}")



