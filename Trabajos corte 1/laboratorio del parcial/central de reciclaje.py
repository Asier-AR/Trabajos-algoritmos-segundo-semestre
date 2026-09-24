
def totalPorPunto(puntos):
    suma=0
    guardador=[]

    for i in range(len(puntos)):
        suma=0
        for n in range(len (puntos[i])):
            suma+=puntos[i][n]
        guardador.append(suma)
                
    return guardador


def totalPorDia(puntos):
    cantidadDias=len(puntos[0])
    cantidadPuntos=len(puntos)
    guardador=[]
    for i in range(cantidadDias):
        sumaDia=0
        for n in range (cantidadPuntos):
            sumaDia+=puntos[n][i]
        guardador.append(sumaDia)
    return guardador

        

def escritorPuntos(puntos):

    for i in range(len(puntos)):
        print("Total del punto de acopio numero ", i+1,": ",puntos[i] )

def escritorPuntosDias(puntos):
     for i in range(len(puntos)):
            print("Total del punto del dia numero ", i+1,": ",puntos[i] )

def Produccion(puntos):
    z=puntos[0]
    x=puntos[0]
    indice=0
    inidiceMayor=0
    for i in range(len(puntos)):
        if x>puntos[i]:
            x=puntos[i]
            indice=i
        if z<puntos[i]:
            z=puntos[i]
            inidiceMayor=i

    print ("El dia menos productivo fue el dia numero ", indice+1, "Con ", x, "kg recolectados")  
    print ("El dia mas productivo fue el dia numero ", inidiceMayor+1, "Con ", z, "kg recolectados")  
               







puntosDeAcopio=[[120, 145, 110, 160, 180, 0], [95, 105, 100, 130, 150, 0],[210, 195,	220, 200, 240, 200], [80, 90, 851, 101, 105, 100]]
totalesPunto=totalPorPunto(puntosDeAcopio)
totalesDia=totalPorDia(puntosDeAcopio)
Produccion(totalesDia)
escritorPuntos(totalesPunto)
escritorPuntosDias(totalesDia)