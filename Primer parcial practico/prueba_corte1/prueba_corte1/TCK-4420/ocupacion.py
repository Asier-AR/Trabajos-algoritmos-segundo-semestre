# ============================================================
#  Cívica Software  ·  TCK-4420  ·  Severidad P3
#  Sistema: RedAcopio  —  Reporte de ocupación
#  NO MODIFIQUE la seccion de datos ni el archivo de pruebas.
# ============================================================

# filas = puntos de acopio, columnas = dias de la semana
ocupacion = [
    [4, 2, 6, 1, 3, 0],
    [0, 5, 5, 2, 7, 1],
    [8, 1, 0, 4, 2, 6],
    [3, 3, 3, 0, 0, 5],
]

def total_por_punto(m):
    """Devuelve una lista con el total recogido por cada punto (fila)."""
    totales = []
    for fila in m:
        s = 0
        for v in fila:
            s += v
        totales.append(s)
    return totales


def total_por_dia(m):
    """Devuelve una lista con el total recogido cada dia (columna).
       BUG REPORTADO: entrega totales incorrectos."""
    totales = []
    cantidad_dias = len(m[0])  # cantidad de columnas
    cantidad_puntos = len(m)  # cantidad de filas
    for i in range(cantidad_dias):              #
        total = 0
        for j in range(cantidad_puntos):  # BUG: el indice de fila y columna estaba invertido
            total+= m[j][i]                 
        totales.append(total)
    return totales


def dia_mas_flojo(m):
    """Devuelve el indice del dia con MENOR recoleccion total."""
    flojos=total_por_dia(m)
    return flojos.index(min(flojos)) #index sirve para encontrar el indice del valor minimo de la lista


def puntos_inactivos(m):
    """Devuelve cuantos registros estan en 0 (el punto no opero ese dia).
    PENDIENTE: implementar."""
    inactivos=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]==0:
                inactivos+=1
    return inactivos