# ============================================================
#  Prueba corta · Segundo corte · EJERCICIO 3  (25 puntos)
#  Tema: pilas
#  Sistema: PrestaLab — historial de acciones del operador
#
#  NO MODIFIQUE el archivo pruebas_e3.py
#  Ejecute:   python3 pruebas_e3.py
# ============================================================


def historial_final(acciones):
    pila = []
    for a in acciones:
        if a == "DESHACER":
            if pila:
                pila.pop()
            # si la pila está vacía, se ignora
        else:
            pila.append(a)
    return pila


def profundidad_maxima(acciones):
    """Devuelve el mayor numero de acciones que el historial llego a
       tener en algun momento del recorrido."""
    pila = []
    maximo = 0
    for a in acciones:
        if a == "DESHACER":
            if pila:
                pila.pop()
        else:
            pila.append(a)
            if len(pila) > maximo:
                maximo = len(pila)
    return maximo
        
