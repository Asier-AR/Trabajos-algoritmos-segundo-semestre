# ============================================================
#  Cívica Software  ·  TCK-5510  ·  Severidad P3
#  Sistema: RedAcopio  —  Mapa de cobertura de rutas
#  NO MODIFIQUE la matriz de datos ni el archivo de pruebas.
# ============================================================

# filas = rutas del camion, columnas = zonas del barrio
# cada celda = kilos recogidos por esa ruta en esa zona
cobertura = [
    [5, 0, 3, 0, 2, 4, 0],
    [0, 0, 7, 0, 1, 0, 6],
    [2, 0, 0, 0, 4, 3, 1],
    [0, 0, 5, 0, 0, 8, 2],
]

def total_por_ruta(m):
    """Devuelve una lista con el total recogido por cada ruta (fila)."""
    totales = []
    for fila in m:
        s = 0
        for v in fila:
            s += v
        totales.append(s)
    return totales


def cobertura_por_zona(m):
    """Devuelve una lista con el total recogido en cada zona (columna).
       BUG REPORTADO: la ultima zona nunca aparece en el informe."""
    totales = []
    for j in range(len(m[0])): #habia un -1 que hacia que la lista no guardara el ultimo dato         # <-- revise este limite
        s = 0
        for i in range(len(m)):
            s += m[i][j]
        totales.append(s)
    return totales


def ruta_mas_productiva(m):
    """Devuelve el INDICE de la ruta que mas kilos recogio en total.
    PENDIENTE: implementar."""
    totales = total_por_ruta(m) #usamos la funcion total que ya esta definida para sacar la lista de valores totales
    max_kilos = max(totales) #usamos el max para encontrar el valor maximo de totales
    x=totales.index(max_kilos) #devuelve el indice vinculado a max
    return x


def zonas_sin_cubrir(m):
    """Devuelve cuantas zonas (columnas) quedaron COMPLETAMENTE en cero,
    es decir, ninguna ruta recogio nada alli.
    PENDIENTE: implementar."""
    totales = cobertura_por_zona(m) #usamos la funcion cobertura_por_zona para sacar la lista de valores totales por zona
    contador=0
    for j in range(len(totales)):
        if totales[j]==0:
            contador+=1
    return contador