def bubble_sort_optimized(arr):
    n = len(arr)
    comparaciones = 0
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparaciones += 1  # Contador para medir las comparaciones
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Bandera: si no hubo intercambios en la pasada completa, corta
        if not swapped:
            break
            
    print(f"Bubble Sort realizó {comparaciones} comparaciones.")
    return arr


def selection_sort(arr):
    n = len(arr)
    comparaciones = 0
    
    # Busca el más pequeño y lo pone al principio
    for i in range(n):
        swapped=False
        min_idx = i
        for j in range(i + 1, n):
            comparaciones += 1  # Contador para medir las comparaciones
            if arr[j] < arr[min_idx]:
                min_idx = j
                swapped=True

        if not swapped:
            break
        # Intercambia el elemento mínimo encontrado con el primero no ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    print(f"Selection Sort realizó {comparaciones} comparaciones.")
    return arr


# --- Demostración con datos ya ordenados (8 elementos) ---
datos_ordenados = [1, 2, 3, 4, 5, 6, 7, 8]

print("=== Prueba con datos ordenados ===")
bubble_sort_optimized(datos_ordenados.copy())
selection_sort(datos_ordenados.copy())