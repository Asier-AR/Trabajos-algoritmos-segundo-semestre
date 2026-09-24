
#include <iostream>
#include <random> //permite generar un numero random
using namespace std;
int main()
{
    random_device aleatorio; //obtiene una semilla aleatoria del sistema operativo
    mt19937 gen(aleatorio()); //crea un numero speudo aleatorio
    uniform_int_distribution<> distrib(1, 3); //define el limite inferior y el limite superior
    int numeroAleatorio= distrib(gen); //inicia la funcion para conseguir el numero aleatorio final 
    
    int eleccion;
    string escoges, maquina;
    
    cout<<"Escoge 1 si quieres elegir piedra, 2 si quieres elegir papel, 3 si quieres elegir tijeras"<<endl;
    cin>> eleccion;
    
    while (eleccion!= 1 and eleccion!= 2 and eleccion!= 3) //se asegura que el usuario no escriba una opcion inexistente
    {
        cout<<"Escogiste una opcion invalida"<<endl;
        cin>> eleccion;
    }
    
    if (eleccion== 1) //piedra
    {
        escoges="piedra";
    }
    else if (eleccion== 2) //papel
    {
        escoges="papel";
    }
    
    else if (eleccion== 3) //tijeras
    {
        escoges="tijeras";
    }
    
    if (numeroAleatorio== 1) //piedra IA
    {
        maquina="piedra";
    }
    else if (numeroAleatorio== 2) //papel IA
    {
        maquina="papel";
    }
    else if (numeroAleatorio== 3) //tijeras IA
    {
        maquina="tijeras";
    }
    
    if (escoges == maquina) //determina si empatar
    {
        cout<<"la ia saco "<<maquina<<" y tu sacaste "<<escoges<<" es un empate";
    }
    
    else if ((escoges=="piedra" and maquina=="tijeras") or (escoges=="tijeras" and maquina=="papel") or (escoges=="papel" and maquina=="piedra"))
    {
        cout<<"la ia saco "<<maquina<<" y tu sacaste "<<escoges<<" tu ganas";
    } //determina si tu ganas
    
    else 
    {
        cout<<"la ia saco "<<maquina<<" y tu sacaste "<<escoges<<" has perdido";
    } //pierdes
}