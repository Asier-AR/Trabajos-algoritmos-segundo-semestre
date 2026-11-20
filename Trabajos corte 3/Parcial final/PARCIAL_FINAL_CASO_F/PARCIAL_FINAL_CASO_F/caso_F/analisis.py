# ============================================================
#  analisis.py · CASO F · PARTE F del parcial  (10 puntos)
#  AguaViva — Monitoreo de pozos rurales
#
#  VERIFICACION CRUZADA
#  Esta es la MISMA logica de Sistema::mejorSeleccion, escrita en el otro
#  lenguaje. El verificador compara los dos resultados: si no coinciden,
#  uno de los dos esta mal y el parcial no cierra.
#
#  MODIFIQUE SOLO ESTE ARCHIVO.  NO TOQUE pruebas.py
# ============================================================


def mejor_seleccion(codigos, pesos, valores, capacidad):
    """Devuelve la lista ORDENADA de codigos de la seleccion de mayor
       valor total que no pasa de 'capacidad'.

       codigos[i], pesos[i] y valores[i] describen el mismo punto.
       Cada punto se lleva o no se lleva. Si hay empate en valor, la
       seleccion con MENOS puntos.

       Debe dar exactamente el mismo resultado que la version en C++.

       PENDIENTE: implementar con recursion de tomar / no tomar y poda."""
    lista= []

    for i in range(len(codigos)):
         if pesos[i] <= capacidad:
               lista.append((codigos[i], valores[i], pesos[i]))
    lista.sort(key=lambda x: (-x[1], x[2]))
    return [codigo for codigo, _, _ in lista]