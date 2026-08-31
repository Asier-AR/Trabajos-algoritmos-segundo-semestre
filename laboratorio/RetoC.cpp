#include <iostream>
#include <string> // Se agrega la librería string
using namespace std;

class PuntoAcopio
{
protected:
    int codigo, totalRecogido;
    string barrio;

public:
    PuntoAcopio() : codigo(0), totalRecogido(0), barrio("") {} // Constructor

    void ingresarPuntoDeAcopio()
    {
        cout << "Ingrese el codigo del punto de acopio: ";
        cin >> codigo;

        cout << "Ingrese el barrio al que pertenece el punto de acopio: ";
        cin >> barrio;

        cout << "Ingrese el total que ha recogido el punto de acopio: ";
        cin >> totalRecogido;
    }

    // Registra nuevos kilos y devuelve el acumulado total del objeto
    int registrarRecoleccion(int kilosNuevos)
    {
        totalRecogido += kilosNuevos;
        return totalRecogido;
    }

    void mostrarPunto() const
    {
        cout << "Punto [" << codigo << "] Barrio: " << barrio 
             << " | Total Recogido: " << totalRecogido << " kg" << endl;
    }
};

int main()
{
    PuntoAcopio punto;
    punto.ingresarPuntoDeAcopio();
    
    // Sumar recolección adicional
    punto.registrarRecoleccion(50);
    
    punto.mostrarPunto();
    
    return 0;
}