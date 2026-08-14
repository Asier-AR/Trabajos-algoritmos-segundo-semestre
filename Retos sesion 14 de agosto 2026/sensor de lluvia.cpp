#include <iostream>
#include <string>
using namespace std;

int main ()
{
    int n, contador, mejorRacha;
    contador=0;
    mejorRacha=0;
    n=9;
    int sensor[9]={0,1,1,0,1,1,1,0,1};

    for (int i=0; i<n; i++)
    {
        if (sensor[i]==1)
        {
            contador+=1;        
        }

        else if (sensor[i]==0 and contador>mejorRacha)
        {
            mejorRacha=contador;
            contador=0;
        }

        else 
        {
            contador=0;
        }
    }

    cout<<"La mayor racha de dias consecutivos lloviendo fue de: "<<mejorRacha<<" dias";
    
}