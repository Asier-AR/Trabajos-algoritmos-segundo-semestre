# include <iostream>
#include <string>
using namespace std;


void escritor(string matriz [][7], string franjaHoraria[6])//escribe la matriz
{
    cout<<"Dia \t\t ";

    for (int k=0; k<6; k++)
    {
        cout<<franjaHoraria[k]<<"\t\t";
    }

    cout<<endl;

    for (int i=0; i<5; i++)
    {
        for (int j=0; j<7; j++)
        {
            cout<<matriz[i][j]<<"\t\t";
        }
        cout<<endl;
    }
    cout<<endl;
}

void maximo(string matriz[][7], string franjaHoraria[6])//encuentra la franja horaria mas concurrida
{
    // 1. Inicializamos con valores por defecto validos
    int maximo = 0; //sirve para comparar el maximo de estudiantes
    int maximoFinal = 0; //encuentra un numero mayor en la matriz de estudiantes 
    int diaMaximo = 0; //sirve para encontrar la fila del dia maximo y guardarla
    int franjaMaxima = 1; // sirve para encontrar la columna con el numero mas alto

    for (int i = 0; i < 5; i++)
    {
        for (int j = 1; j < 7; j++)
        {   
            maximo = stoi(matriz[i][j]);
            if (maximo > maximoFinal)
            {
                maximoFinal = maximo;
                diaMaximo = i;
                franjaMaxima = j; // Guarda un valor entre 1 y 6
            }
        }
    }

    // 2. Restamos 1 a franjaMaxima para acceder correctamente a franjaHoraria (indices 0 a 5)
    cout << "La franja mas concurrida fue la de " << franjaHoraria[franjaMaxima - 1] //se le resta uno a la franja maxima debido a que la matriz sobre la que opera j tiene una mayor cantidad de elementos que la franja horaria 
         << " el dia " << matriz[diaMaximo][0] 
         << " con un total de " << matriz[diaMaximo][franjaMaxima] 
         << " estudiantes" << endl;

}
    
void diaMaximo(string matriz[][7]) //encuentra el dia maximo 
{
      int maximo, maximoFinal, diaMaximo;
    maximoFinal=0;
    maximo=0;
    for (int i=0; i<5; i++)
    {
        for (int j=1; j<7; j++)
        {   
            maximo=maximo + stoi (matriz[i][j]); //stoi sirve para pasar un string a un entero
           


        }
         if (maximo>maximoFinal)
            {
                maximoFinal=maximo;
                diaMaximo= i;
            }

     maximo=0;
    }

    cout<<"El dia mas concurrido fue el dia "<<matriz[diaMaximo][0]<<" con un total de "<<maximoFinal<<" estudiantes "<<endl;
}   


int main (){

string horario, cantidadEstudiantes;

string matriz[5][7]={{"Lunes    "}, {"Martes   "}, {"Miercoles"}, {"Jueves   "}, {"Viernes  "}};
string franjaHoraria[6];

for (int x=0; x<6; x++)
{
cout<<"Ingrese las seis franjas horarias (sin espacios por ejemplo 12:00-13:00) "<<endl;
cin>>horario;

franjaHoraria[x]=horario;
}

for (int y=0; y<5; y++)
    {   int h=0;
        for(int z=1; z<7; z++)
        {   
            cout<<"Anote la cantidad de estudiantes que hubo el dia "<<matriz[y][0]<<" en la franja horaria de las "<<franjaHoraria[h]<<endl;
            cin>>cantidadEstudiantes;

            matriz[y][z]=cantidadEstudiantes;
            h=h+1;
        }
    }
 escritor (matriz, franjaHoraria); 
 maximo (matriz, franjaHoraria);
diaMaximo(matriz);
return 0;
}