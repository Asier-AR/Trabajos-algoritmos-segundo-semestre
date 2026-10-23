# ============================================================
#  Prueba corta · Segundo corte · EJERCICIO 1  (25 puntos)
#  Tema: recursion y exploracion de caminos
#  Sistema: TurnoJusto — calculo de rutas de atencion
#
#  NO MODIFIQUE el archivo pruebas_e1.py
#  Ejecute:   python3 pruebas_e1.py
# ============================================================


from glob import glob


def suma_impares(n):
    """Devuelve la suma de todos los numeros impares desde 1 hasta n (incluido).
       Ejemplos:  suma_impares(5) -> 9     (1 + 3 + 5)
                  suma_impares(0) -> 0     (no hay impares)

       DEFECTO REPORTADO: con ciertas entradas el programa se cae.
       Revise el caso base."""
    
    if n==0:
        return 0
    
    if n == 1:
        return 1
    if n % 2 == 0:
        return suma_impares(n - 1)
    return n + suma_impares(n - 1)


def contar_caminos(f, c):   
    if f<1 or c<1:
        return 0
    if f==1 or c==1:
        return 1

    return contar_caminos(f-1, c) + contar_caminos(f, c-1)
    

    """Devuelve cuantos caminos distintos hay desde la casilla superior
       izquierda hasta la inferior derecha de una cuadricula de f filas
       por c columnas, avanzando solo a la DERECHA o hacia ABAJO.

       Ejemplo: contar_caminos(3, 3) -> 6

       PENDIENTE: implementar. Debe ser recursiva: no use ciclos ni listas."""


#def resolver(f, c):
#    # 1. ¿me sali del tablero?
#    if f < 0 or f >= FILAS or c < 0 or c >= COLS:
#        return False
#    # 2. ¿es muro o ya pase por aqui?
#    if laberinto[f][c] == 1 or camino[f][c] == 1:
#        return False
#    # 3. marco esta casilla como parte del camino
#    camino[f][c] = 1
#    # 4. CASO BASE: llegue a la salida
#    if f == FILAS - 1 and c == COLS - 1:
#        return True
#    # 5. CASO RECURSIVO: pruebo las cuatro direcciones
#    if resolver(f + 1, c): return True
#    if resolver(f, c + 1): return True
#    if resolver(f - 1, c): return True
#    if resolver(f, c - 1): return True
#    # 6. BACKTRACKING: ninguna sirvio, desmarco y me devuelvo
#    camino[f][c] = 0
#    return False

    
