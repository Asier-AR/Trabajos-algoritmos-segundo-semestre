Algoritmo Gestion_medica
	Edad = 0
	Tiempo_De_Espera = 0
	Enfermedad = ""
	Prioridad = 0
	Escribir "Por favor ingrese su edad"
	Leer Edad
	Si Edad< 18 | Edad>59 Entonces
		Prioridad = Prioridad+1
	SiNo
		Prioridad = Prioridad
	FinSi
	Escribir "Porfavor ingrese cuantos minutos lleva esperando solo el numero"
	Leer Tiempo_De_Espera
	Si Tiempo_De_Espera>= 30 Entonces
		Prioridad = Prioridad+1
	SiNo
		Prioridad = Prioridad
	FinSi
	Escribir "¿Usted sufre de alguna enfermedad que ponga en riesgo su vida de manera inmediata responda Si o No?"
	Leer Enfermedad
	Si Enfermedad=="S" Entonces
		Prioridad = 4
	SiNo
		Si Enfermedad=="Si" Entonces
			Prioridad = 4
		SiNo
			Si Enfermedad=="si" Entonces
				Prioridad = 4
			SiNo
				Si Enfermedad=="sI" Entonces
					Prioridad = 4
				SiNo
					Si Enfermedad== "s" Entonces
						Prioridad = 4
					SiNo
						Prioridad = Prioridad
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
	Si Prioridad==4 Entonces
		Escribir "Prioridad muy Alta"
	SiNo
		Si Prioridad==2 Entonces
			Escribir "Prioridad media"
		SiNo
			Si Prioridad <2 Entonces
				Escribir "Prioridad baja porfavor sea paciente"
			FinSi
		FinSi
	FinSi
FinAlgoritmo
