# include <iostream>
using namespace std;

class objetos
{    
    private:

    static int contador;
  
    public:

    objetos(){contador+=1;}

    int obtenerContador ()
    {
        return contador;
    }
};

int objetos::contador=0;

int main ()
{   

    objetos objeto1;
    objetos objeto2;

    cout<<"el total de objetos es "<<objeto1.obtenerContador()<<endl;
}