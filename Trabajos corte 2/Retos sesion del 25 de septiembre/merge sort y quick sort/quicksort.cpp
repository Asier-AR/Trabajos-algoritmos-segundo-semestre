#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Declaración previa de la función de partición
int particion(vector<int>& arr, int primero, int ultimo);

void quicksort(vector<int>& arr, int primero, int ultimo) {
    if (primero < ultimo) 
    {
        int pivote = particion(arr, primero, ultimo);

        quicksort(arr, primero, pivote);
        quicksort(arr, pivote+1, ultimo);
    }
}


int particion (vector<int>& arr, int primero, int ultimo)
{

    int pivote=arr[primero];
    int izquierdo= primero-1;
    int derecho= ultimo+1;
    while (true)
    {
        izquierdo+=1;
        while (arr[izquierdo]<pivote)
        {
            izquierdo+=1;
        }



        derecho-=1;
        while (arr[derecho]>pivote)
        {
            derecho-=1;
        }



        if (izquierdo>=derecho)

        {
            return derecho;
        }

        swap (arr[izquierdo], arr[derecho]);
    }



}

int main() 
{
    vector<int> lista = {4, 9, 3, 6, 8, 2};
    int primero=0;
    int ultimo=lista.size()-1;
    quicksort(lista, primero, ultimo);

    for (int i = 0; i < lista.size(); i++) {
        cout << lista[i] << " ";
    }
    cout << endl;

    return 0;
}  