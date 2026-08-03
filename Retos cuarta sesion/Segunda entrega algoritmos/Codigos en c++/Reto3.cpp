/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
#include <random>
#include <cctype> 
#include <algorithm> //estas 2 ultimas funciones son para convertir los strings en minusculas
using namespace std;
int main()
{
    random_device aleatorio; //obtiene una semilla aleatoria del sistema operativo
    mt19937 gen(aleatorio()); //crea un numero speudo aleatorio
    uniform_int_distribution<> distrib(1, 100); //define el limite inferior y el limite superior
    int numeroAleatorio= distrib(gen); //inicia la funcion para conseguir el numero aleatorio final 
    
    string eleccion, maquina, moneda;
    
    cout<<"Cara o Cruz"<<endl;
    cin>> eleccion;
    transform (eleccion.begin(), eleccion.end(), eleccion.begin(), ::tolower); //pasa el string a minusculas
    
    while (eleccion!="cara" and eleccion!="cruz") //evita que el usuario escoja una opcion no valida
    {
        cout<<"eleccion no valida elija una eleccion que si sea valida por favor "<<endl;
        cin>>eleccion;
    }
    
    if (eleccion == "cara") //determina que va a elegir la maquina
    {
        maquina= "cruz";
    }
    else
    {
        maquina= "cara";
    }    
    
    if (numeroAleatorio%2==0)
    {
        moneda="cara";
    }
    else 
    {
        moneda="cruz";
    }
    
    if (eleccion == moneda)
    {
        cout<<"la moneda cayo en "<<moneda<<" felicidades ganaste";
    }
    
    else
    {
        cout<<"la moneda cayo en "<<moneda<<" perdiste mejor suerte la proxima";
    }
}