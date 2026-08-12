import random


dado1=random.randint(1, 6)
dado2=random.randint(1, 6)

print ("Lanzando dados ")

print ("sacaste", dado1, "con el primer dado y ", dado2, "con el segundo dado ")

if dado1==1 and dado2==1:
        
    print("Felicidades has ganado ")
    

elif dado1+dado2==3:
    
    print("Felicidades has ganado ")
    

elif (dado1+dado2==11):
        
    print ("Felicidades has ganado ")
        

elif (dado1+dado2==2 or dado1+dado2==12):
        
    print ("Felicidades has ganado ")
       

elif (dado1+dado2==7):
        
    print("Felicidades has ganado ")
        

else:
        
    print("has perdido mejor suerte la proxima")
        