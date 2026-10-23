registros = [("vidrio", 12), ("papel", 8),  ("vidrio", 5),  ("plastico", 20), 
("papel", 14),  ("metal", 3), ("plastico", 7), ("vidrio", 9)] 


def acumular(registros):
    diccionario = {} # en este caso es mejor usar un diccionario ya que nos permite revisar directamente si la clave existe o no, en lugar de recorrer toda la lista como en el caso de un mapa
    for x in registros:
        if x[0] in diccionario:
            diccionario[x[0]] += x[1]
        else:
            diccionario[x[0]] = x[1]
    return diccionario

def mayortotal(diccionario): #para el mayor total es mejor emplear un diccionario gracias a su estructura clave dato que nos permite saber a ciencia cierta cual es el material con la mayor clave
    mayor = 0
    clave_mayor = ""
    for clave, valor in diccionario.items():
        if valor > mayor:
            mayor = valor
            clave_mayor = clave
    return clave_mayor, mayor

def listarMateriales(registros): #para listar los materiales es mejor emplear un mapa ya que nos permite almacenar los materiales sin repeticiones y luego convertirlo en una lista para poder mostrarlo
    mapa=set()
    for x in registros:
        mapa.add(x[0])
    return mapa

print(listarMateriales(registros))