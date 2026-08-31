#include <iostream>
using namespace std;

int main()
{

int cantidad;

cout<<"Ingrese la cantidad de puntos de acopio que desea registrar "<<endl;
cin>> cantidad;

if (cantidad<= 0)
{
cout<<"La cantidad de puntos de acopio debe ser mayor a 0"<<endl;
return 1;
}
//reservar memoria para la cantidad de puntos de acopio dinamicamente
double* pesos= new double[cantidad]; //esto es instanciar un objeto y crear un arreglo dinamico

//llenar el arreglo usando aritmetica de punteros

cout<<"Ingrese los pesos de la jornada especial"<<endl;

for (double*p=pesos; p<pesos+cantidad; ++p)
{
    cout<<"Pesos: ";
    cin>>*p;
}

double suma=0;

for (double*p=pesos; p<pesos+cantidad; p++)
{
    suma+=*p;
}

double promedio=suma / cantidad;
cout<<"El promedio de los pesos es: "<<promedio<<endl;

delete[] pesos; //elimina el array pesos

pesos= nullptr; //deja al puntero apuntando a nada
}