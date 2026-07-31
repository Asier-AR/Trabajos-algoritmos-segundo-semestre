Algoritmo Numero_del_1_al_100
	Numero_a_Adivinar <- 0
	Numero_elegido <- 0
	Intentos <- 0
	Escribir 'Ingrese el numero a adivinar'
	Leer Numero_a_Adivinar
	Escribir 'Elija un numero entre el 1 y el 100'
	Leer Numero_elegido
	Mientras Numero_elegido<>Numero_a_Adivinar Y Intentos<7 Hacer
		Si Numero_elegido<Numero_a_Adivinar Entonces
			Escribir 'El numero es mayor'
		SiNo
			Escribir 'El numero es menor'
		FinSi
		Intentos <- Intentos+1
		Escribir "Te quedan " Intentos " intentos"
		Escribir 'Ingrese un numero'
		Leer Numero_elegido
	FinMientras
	Si Intentos==7 Entonces
		Escribir 'Perdiste mejor suerte la proxima'
	SiNo
		Escribir 'Bien hecho acertaste'
	FinSi
FinAlgoritmo
