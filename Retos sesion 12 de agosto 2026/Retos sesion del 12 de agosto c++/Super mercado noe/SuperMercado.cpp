#include <iostream>
#include <string>
#include <random>
using namespace std;
 random_device aleatorio; //obtiene una semilla aleatoria del sistema operativo
    mt19937 gen(aleatorio()); //crea un numero speudo aleatorio
    uniform_int_distribution<> distrib(1, 4); //define el limite inferior y el limite superior
    
int main ()
{   
    int valor, valorFinal;
    cout<<"Ingrese el valor de su compra "<<endl;
    cin>>valor;
    while (valor<0)
    {
        cout<<"No se puede tener un valor negativo ingrese un valor valido"<<endl; //evita que el usuario ingrese valores negativos
        cin>>valor;
    }
    if (valor>50000) // determina si alcanzo el precio minimo ademas de realizar la accion de sacar la bolita
    {   
        cout<<"precio minimo alcanzado realizando giro de ruleta"<<endl;
        int numeroAleatorio1= distrib(gen); //inicia la funcion para conseguir el numero aleatorio final

        if (numeroAleatorio1==1)
        {
            cout<<"Has sacado la bolita roja descuento de 10%"<<endl;
            valorFinal= valor-(valor*0.1);
        }

        else if (numeroAleatorio1==2)
        {
            cout<<"Has sacado la bolita azul descuento de 30%"<<endl;
            valorFinal= valor-(valor*0.3);
        }

         else if (numeroAleatorio1==3)
        {
            cout<<"Has sacado la bolita amarilla descuento de 50%"<<endl;
            valorFinal= valor-(valor*0.5);
        }

        else if (numeroAleatorio1==4)
        {
            valorFinal= 0;
        }

        cout<<"El precio inicial era de "<<valor<<" pero despues del descuento tendra que pagar "<<valorFinal<<endl;
    }

   else {cout<<"No se ha alcanzado el umbral minimo su compra es de 5 "<<valor<<endl;}

   return 0;
}