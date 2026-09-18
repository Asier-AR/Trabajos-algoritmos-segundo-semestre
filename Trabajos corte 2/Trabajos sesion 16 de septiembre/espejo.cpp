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
        return Volteador(texto.substr(1)) + texto[0];
    }
}


int main ()
{

    string texto= "paralelepipedo";


    cout<<(Volteador(texto));
    return 0;
}