
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

int main()
{
    
    double numero1, numero2;
    cout<<"Ingrese los 2 numeros que desea operar"<<endl;
    cin>>numero1;
    cin>>numero2;
    
    cout<<"La suma "<<numero1<<"+"<<numero2<<" es "<<numero1+numero2<<endl;
    
    cout<<"La resta "<<numero1<<"-"<<numero2<<" es "<<numero1-numero2<<endl;
    
    cout<<"La multiplicacion "<<numero1<<"x"<<numero2<<" es "<<numero1*numero2<<endl;
    
    cout<<"La division "<<numero1<<"/"<<numero2<<" es "<<numero1/numero2<<endl;
    
    cout<<"La potencia "<<numero1<<"^"<<numero2<<" es "<<pow(numero1, numero2)<<endl;
//la funcion pow viene de la libreria cmath   el primer numero es la base y el segundo el exponente

    cout<<" la raiz cuadrada de "<<numero1<<" es "<<sqrt(numero1)<<endl;
    
    cout<<" la raiz cuadrada de "<<numero2<<" es "<<sqrt(numero2)<<endl;
}