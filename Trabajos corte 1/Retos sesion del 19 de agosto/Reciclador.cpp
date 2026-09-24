#include <iostream>
using namespace std;

int main()
{
     int f = 2;
     int c = 3;

    int matriz1[f][c] = 
    {
        {1, 2, 3},
        {4, 5, 6}
    };

    // segun lo que entendi las filas y las columnas se intercambian
    int matrizNueva[c][f]; 

    // 2. Aplicar la fórmula de rotación a 90°
    for (int i = 0; i < f; i++)
    {
        for (int j = 0; j < c; j++)
        {
            matrizNueva[j][f - 1 - i] = matriz1[i][j];
        }
    }

    // 3. Imprimir usando las dimensiones de la nueva matriz (c x f)
    for (int i = 0; i < c; i++)
    {   cout<<"{";
        for (int j = 0; j < f; j++)
        {
            cout << matrizNueva[i][j]<<", ";
        }
        cout <<"}"<< endl;
    }

    return 0;
}