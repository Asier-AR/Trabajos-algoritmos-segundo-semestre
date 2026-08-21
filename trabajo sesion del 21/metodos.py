edades=[19, 13, 16, 30, 20, 11, 20] #tenemos nuestra lista

print ((edades), "lista edades antes del.sort()")
print (" ")
edades.sort()

print ((edades),(" lista de edades despues del sort")) #como puede observar el metodo .sort() lo que hace es modificar directamente la lista ordenandola de menor a mayor o en orden alfabetico no confundir con sorted() que crea una lista nueva ordenada
print (" ")
letras= ["c","b","a","d"]

print ((letras), "lista letras antes del sort")
print (" ")
letras.sort()

print ((letras), ("lista letras despues del sort"))
print (" ")
edades.sort(reverse=True) #ordenara la lista de mayor a menor

letras.sort(reverse=True) #ordenara la lista de la z a la a

print (edades)
print (" ")
print (letras)