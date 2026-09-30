#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>  //sirve para medir el tiempo
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


void bubbleSort(vector<int>& arr, int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}



int main ()
{

// Parte D

// Un ordenamiento avanzado y la medición Implementen Merge o Quicksort, midan el tiempo contra uno de los básicos para tres tamaños distintos de entrada 
// y produzcan la tabla. En el archivo de respuestas, expliquen en cinco líneas por qué los tiempos crecen distinto.


vector <int> tamano_1 = {
    100004, 200018, 100002, 200012, 100009, 
    200015, 100006, 200019, 100001, 200011, //lista de 20 elementos
    100008, 200020, 100003, 200014, 100010, 
    200017, 100005, 200016, 100007, 200013
};

vector <int> tamano_2 = {
    300028, 100005, 200014, 400039, 100002, 
    200020, 300021, 100009, 400034, 200011, 
    300025, 100008, 400037, 200018, 100001, 
    300029, 200016, 400040, 100004, 300023, 
    200012, 400032, 100007, 300030, 200019,  //lista de 40 elementos
    400036, 100003, 200015, 300022, 400031, 
    100010, 200017, 300026, 400035, 100006, 
    200013, 300027, 400038, 300024, 400033
};

vector <int> tamano_3 = {
    500052, 200014, 100003, 400038, 300021, 
    600060, 200018, 500043, 100009, 300027, 
    400032, 600055, 100001, 500049, 200012, 
    300025, 400036, 600058, 200020, 100007, 
    500041, 300023, 400034, 600051, 100005, 
    200016, 500047, 300029, 400040, 600054, 
    200011, 100002, 500045, 300022, 400031,  //lista de 60 elementos
    600057, 100008, 200019, 500050, 300028, 
    400037, 600053, 200015, 100004, 500044, 
    300026, 400035, 600059, 100010, 200017, 
    500048, 300030, 400033, 600052, 100006, 
    200013, 500042, 500046, 400039, 600056
};

vector <int> copia1=tamano_1;

vector <int> copia2= tamano_2;

vector <int> copia3= tamano_3;

cout<<"========================Tamaño 1========================"<<endl;

auto inicio= chrono::high_resolution_clock::now();
quicksort(copia1, 0, (copia1.size()-1));
auto final= chrono::high_resolution_clock::now();
chrono::duration<double, std::milli> duracion = final - inicio;

auto inicio1= chrono::high_resolution_clock::now();
bubbleSort(tamano_1, tamano_1.size());
auto final1= chrono::high_resolution_clock::now();
chrono::duration<double, std::milli> duracion1 = final1 - inicio1;

cout<<"Tiempo que le tomo al quicksort: "<<duracion<<endl;
cout<<"Tiempo que le tomo al bubble sort: "<<duracion1<<endl;

cout<<"========================Tamaño 2========================"<<endl;



inicio= chrono::high_resolution_clock::now();
quicksort(copia2, 0, (copia2.size()-1));
final= chrono::high_resolution_clock::now();
duracion = final - inicio;

inicio1= chrono::high_resolution_clock::now();
bubbleSort(tamano_2, tamano_2.size());
final1= chrono::high_resolution_clock::now();
duracion1 = final1 - inicio1;

cout<<"Tiempo que le tomo al quicksort: "<<duracion<<endl;
cout<<"Tiempo que le tomo al bubble sort: "<<duracion1<<endl;

cout<<"========================Tamaño 3========================"<<endl;

inicio= chrono::high_resolution_clock::now();
quicksort(copia3, 0, (copia3.size()-1));
final= chrono::high_resolution_clock::now();
duracion = final - inicio;

inicio1= chrono::high_resolution_clock::now();
bubbleSort(tamano_3, tamano_3.size());
final1= chrono::high_resolution_clock::now();
duracion1 = final1 - inicio1;

cout<<"Tiempo que le tomo al quicksort: "<<duracion<<endl;
cout<<"Tiempo que le tomo al bubble sort: "<<duracion1<<endl;

return 0;


//Los tiempos crecen distintos por la complejidad de ambas funciones (aunque tambien depende del tipo de equipo que corra el codigo)
// porque la complejidad de bubble sort es de O(n al cuadrado en todos sus casos 
// y Quick sort tiene una complejidad de O(n log n) en su caso promedio y en su peor de O(n al cuadrado)
// en conclucion la mayoria de veces el trabajo que va a hacer bubble va a crecer 4 veces y el de quick sort n*log n
}