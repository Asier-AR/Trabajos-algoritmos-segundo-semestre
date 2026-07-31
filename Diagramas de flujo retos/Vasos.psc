Algoritmo Vasos
	Vaso_A <- 'Jugo'
	Vaso_B <- 'Agua'
	Vaso_C <- 'Vacio'
	Si Vaso_A=='Agua' Y Vaso_B=='Jugo' Entonces
		Escribir 'hola'
	SiNo
		Vaso_C <- Vaso_A
		Escribir 'Agarro el vaso A y vierto su liquido en el Vaso C"
		Vaso_A <- 'Vacio'
		Vaso_A <- Vaso_B
		Escribir 'Despues de dejar en la mesa el vaso A agarramos el vaso B y lo vertimos en el Vaso A'
		Vaso_B <- 'Vacio'
		Vaso_B <- Vaso_C
		Vaso_C <- 'Vacio'
		Escribir 'Repito el paso anterior pero esta ves con el vaso B y el Vaso C'
		Escribir "Y asi el vaso C quedo " Vaso_C
		Escribir "El vaso A quedo con " Vaso_A
		Escribir "El vaso B quedo con " Vaso_B
	FinSi
FinAlgoritmo
