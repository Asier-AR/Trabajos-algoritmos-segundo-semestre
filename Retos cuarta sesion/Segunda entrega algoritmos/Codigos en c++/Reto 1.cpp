

#include <iostream>
#include <string>
using namespace std;

int main()
{

double Centigrados, Fahrenheit;
cout<< "Porfavor ingrese la cantidad de grados Fahrenheit que desea pasar a grados Celcius "<<endl;

cin>> Fahrenheit;

Centigrados= (Fahrenheit-32)/1.8; //operacion que nos permite pasar grados Fahrenheit a grados Centigrados

cout<<Fahrenheit<<" grados Fahrenheit son "<<Centigrados<<" grados Centigrados";
return 0;
}