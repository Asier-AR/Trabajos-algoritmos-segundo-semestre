#include <iostream>
using namespace std;

int main (){

int n, k, contadorFallos, contadorValido, numerador;
double promedio;
int sensor[n]={};
cout<<"cuantas entradas desea realizar "<<endl;
cin>>n; //n es el numero de elementos que tendra nuestro array estatico
numerador=0;
for (int i=0; i<n; i++)
{   
    cout<<"Ingrese el numero de la lectura o ingrese -999 si la lectura es fallida"<<endl;
    cin>>k; //numero de entrada realizada K

    sensor[i]=k;
}


contadorFallos=0;
contadorValido=0;

for (int i=0; i<n; i++)
{
    if (sensor[i]==-999)
    {
        contadorFallos+=1;
        continue;
    }
    
    else 
    {
        numerador=numerador+sensor[i];
        contadorValido+=1;
    }
}

promedio= (double) numerador/contadorValido;

cout<<"El promedio de los datos obtenidos es "<< promedio<<endl;
cout<<"Se eliminaron "<<contadorFallos<<" lecturas dañadas"<<endl;
cout<<"Numero de entradas validas: "<<contadorValido;

return 0;

}
