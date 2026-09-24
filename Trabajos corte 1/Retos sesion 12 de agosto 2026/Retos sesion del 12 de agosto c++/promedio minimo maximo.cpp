#include <iostream>
using namespace std;

int main() {
   int edades[5] = {20, 25, 22, 23, 19};
    
    int promedioNumerador = 0;
    int maximo = 0;
    int minimo = edades[0];

    // Suma de todas las edades
    for (int i = 0; i < (sizeof(edades) / sizeof(edades[0])); i++) {
        promedioNumerador += edades[i];
    }

    double promedioFinal = promedioNumerador / (sizeof(edades) / sizeof(edades[0]));

    // Búsqueda del valor máximo
    for (size_t i = 0; i < (sizeof(edades) / sizeof(edades[0])); i++) {
        if (maximo < edades[i]) {
            maximo = edades[i];
        }
    }

    // Búsqueda del valor mínimo
    for (size_t i = 0; i < (sizeof(edades) / sizeof(edades[0])); i++) {
        if (minimo > edades[i]) {
            minimo = edades[i];
        }
    }

    cout << "el promedio de las edades es " << promedioFinal << endl;
    cout << "el maximo de las edades es " << maximo << endl;
    cout << "el minimo de las edades es " << minimo << endl;

    return 0;
}