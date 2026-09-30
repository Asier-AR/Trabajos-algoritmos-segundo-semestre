def bubble_sort_optimized(arr):
    n = len(arr)
    comparaciones = 0
    intercambios = 0
    pasadas = 0

    for i in range(n):
        pasadas += 1
        swapped = False
        for j in range(0, n - i - 1):
            comparaciones += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambios += 1
                swapped = True

        if not swapped:
            break

    print(
        f"Bubble Sort realizó {pasadas} pasadas, {comparaciones} comparaciones"
        f" y {intercambios} intercambios."
    )
    return arr


def selection_sort(arr):
    n = len(arr)
    comparaciones = 0
    intercambios = 0
    pasadas = 0

    for i in range(n):
        pasadas += 1
        min_idx = i
        for j in range(i + 1, n):
            comparaciones += 1
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            intercambios += 1

    print(
        f"Selection Sort realizó {pasadas} pasadas, {comparaciones}"
        f" comparaciones y {intercambios} intercambios."
    )
    return arr


def insertion_sort(arr):
    pasadas = 0
    comparaciones = 0
    desplazamientos = 0

    for i in range(1, len(arr)):
        pasadas += 1
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparaciones += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                desplazamientos += 1
                j -= 1
            else:
                break

        arr[j + 1] = key

    print(
        f"Insertion Sort realizó {pasadas} pasadas, {comparaciones}"
        f" comparaciones y {desplazamientos} desplazamientos."
    )
    return arr


# Prueba con datos ordenados
datos_ordenados = [1, 2, 3, 4, 5, 6, 7 ,8 ]

print("=== Prueba con datos ordenados ===")
print (bubble_sort_optimized(datos_ordenados.copy()))
print (selection_sort(datos_ordenados.copy()))
print (insertion_sort(datos_ordenados.copy()))