edades=[20,25,22,23,19]
promedioNumerador=0
maximo=0
minimo=edades[0]
for i in range (len(edades)):
    promedioNumerador= promedioNumerador+edades[i]

promedioFinal= promedioNumerador / len(edades)

for i in range (len(edades)):
    if maximo<edades[i]:
        maximo=edades[i]
        
for i in range (len(edades)):
    if minimo>edades[i]:
        minimo=edades[i]
        
print ("el promedio de las edades es ", promedioFinal)
print ("el maximo de las edades es ", maximo)
print ("el minimo de las edades es", minimo)
