class PuntoAcopio:

    def __init__(self):
        # Atributos privados mediante doble guion bajo '__'
        self.__codigo = 0
        self.__barrio = ""
        self.__total_recogido = 0.0

    # --- GETTERS TRADICIONALES ---
    def get_codigo(self) -> int:
        return self.__codigo

    def get_barrio(self) -> str:
        return self.__barrio

    def get_total_recogido(self) -> float:
        return self.__total_recogido

    # --- SETTERS TRADICIONALES CON VALIDACIÓN ---
    def set_codigo(self, cod: int):
        self.__codigo = cod

    def set_barrio(self, b: str):
        self.__barrio = b

    def set_total_recogido(self, kilos: float):
        if kilos >= 0:
            self.__total_recogido = kilos
        else:
            print(
                f"[ERROR]: El peso ingresado no puede ser negativo ({kilos} kg)."
            )

    # --- MÉTODO DE ENTRADA DE DATOS ---
    def ingresar_punto_de_acopio(self, numero_punto: int):
        print(f"\n--- Ingrese datos del Punto de Acopio #{numero_punto} ---")

        cod = int(input("Codigo: "))
        self.set_codigo(cod)

        b = input("Barrio: ")
        self.set_barrio(b)

        kilos = float(input("Total recogido (kg): "))
        self.set_total_recogido(kilos)



cantidad = int(input("¿Cuantos puntos de acopio nuevos desea registrar?: "))

if cantidad <= 0:
    print("[ERROR]: La cantidad debe ser mayor a 0.")

# Lista dinámica para almacenar los objetos
puntos = []

# Crear y registrar cada objeto
for i in range(cantidad):
        nuevo_punto = PuntoAcopio()
        nuevo_punto.ingresar_punto_de_acopio(i + 1)
        puntos.append(nuevo_punto)

# Sumar el total accediendo mediante el método getter explicito get_total_recogido()
suma_total = sum(p.get_total_recogido() for p in puntos)

print("\n==============================================")
print(" Resumen del Registro (Sin @property)")
print("==============================================")
print(f" Total de puntos creados : {cantidad}")
print(f" Total acumulado global  : {suma_total:.1f} kg")
print("==============================================")

