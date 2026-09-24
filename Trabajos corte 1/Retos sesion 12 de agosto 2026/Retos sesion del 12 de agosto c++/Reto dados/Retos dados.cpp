#include <iostream>
#include <string>
#include <cctype> 
#include <algorithm> //estas 2 ultimas funciones son para convertir los strings en minusculas
#include <random>
using namespace std;
int main ()
{
   random_device aleatorio; //obtiene una semilla aleatoria del sistema operativo
    mt19937 gen(aleatorio()); //crea un numero speudo aleatorio
    uniform_int_distribution<> distrib(1, 6); //define el limite inferior y el limite superior
   
    int eleccion2=1;
    int dado1, dado2;
    string eleccion;
    cout<<"------------------------------"<<endl;
    while (eleccion2==1)
    {
        cout<<"lanzando dados"<<endl;
         int numeroAleatorio1= distrib(gen); //inicia la funcion para conseguir el numero aleatorio final
         int numeroAleatorio2= distrib(gen); //inicia la funcion para conseguir el numero aleatorio final
        dado1=numeroAleatorio1;
        dado2=numeroAleatorio2;

        cout<<"El dado numero 1 ha sacado "<<dado1<<endl;
        cout<<"El dado numero 2 ha sacado "<<dado2<<endl;


        if (dado1==1 and dado2==1)
        {
            cout<<"Felicidades has ganado "<<endl;
        }

        else if (dado1+dado2==3)
        {
            cout<<"Felicidades has ganado "<<endl;
        }

        else if (dado1+dado2==11)
        {
            cout<<"Felicidades has ganado "<<endl;
        }

        else if (dado1+dado2==2 or dado1+dado2==12)
        {
            cout<<"Felicidades has ganado "<<endl;
        }

        else if (dado1+dado2==7)
        {
            cout<<"Felicidades has ganado "<<endl;
        }

        else
        {
            cout<<"has perdido mejor suerte la proxima"<<endl;
        }
        
        cout<<"¿Deseas seguir jugando? (S/N)"<<endl;
        cin>>eleccion;

        transform (eleccion.begin(), eleccion.end(), eleccion.begin(), ::tolower); //pasa el string a minusculas

        if (eleccion=="si" or eleccion=="s")
        {
            cout<<"Iniciando otro intento "<<endl;
        }
        else if (eleccion2="no" or eleccion=="n")
        {
            cout<<"saliendo del juego"<<endl;
            eleccion2=2;
        }
        else { cout<<"Haz escogido una opcion no valida cerrando programa"<<endl;
        eleccion2=2;}

        cout<<"------------------------------"<<endl;
    }

    return 0;
}