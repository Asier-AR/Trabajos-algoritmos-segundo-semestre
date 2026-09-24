# include <iostream>
#include <string>
using namespace std;

string Volteador(string texto)
{   
    string invertido="";
    if (texto=="")
    {
       return "";
    }

    else
    {
        return Volteador(texto.substr(1)) + texto[0]; //el comando .substr(1) hace que se tome el string pero esta ves empezando desde el segundo elemento
    }
}


int main ()
{

    string texto= "paralelepipedo";


    cout<<(Volteador(texto));
    return 0;
}