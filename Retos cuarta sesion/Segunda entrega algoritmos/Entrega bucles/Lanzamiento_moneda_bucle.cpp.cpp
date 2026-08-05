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
    
    
    string eleccion, maquina, moneda;
    bool seguirJugando=true;
    int continuar, num_rondas, victorias, victoriasMaquina, x;

    victorias=0;
    victoriasMaquina=0;
    while (seguirJugando==true){
    cout<<"Cuantas rondas quieres jugar "<<endl;
    cin>>num_rondas;
    
    for (int i=0; i<num_rondas; i++){
    cout<<"Cara o Cruz"<<endl;
    cin>> eleccion;

    transform (eleccion.begin(), eleccion.end(), eleccion.begin(), ::tolower); //pasa el string a minusculas
     
    int numeroAleatorio= distrib(gen); //inicia la funcion para conseguir el numero aleatorio final
    
    

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
    
    if (numeroAleatorio%2==0) //determina en que lado va a caer la moneda
    {
        moneda="cara";
    }
    else 
    {
        moneda="cruz";
    }
    
    if (eleccion == moneda)
    {
        cout<<"la moneda cayo en "<<moneda<<" felicidades ganaste "<<endl;
        victorias+=1;

    }
    
    else
    {
        cout<<"la moneda cayo en "<<moneda<<" perdiste mejor suerte la proxima "<<endl;
        victoriasMaquina+=1;
    }

   
}


    cout<<"La maquina ha ganado un total de "<<victoriasMaquina<<" veces y tu has ganado un total de"<<victorias<<" veces"<<endl;

    cout<<"Quieres seguir jugando? (escribe 1 si quieres continuar, 2 si quieres salir)"<<endl; 
    cin>>continuar;
    
    if (continuar==1)
    {
        seguirJugando=true;
    }
    else if (continuar==2)
    {
        seguirJugando=false;}
        
    
    else 
    {
        cout<<"Esta opcion no esta determinada asi que se saldra del juego";
        seguirJugando=false;
    }
    
    
}
}