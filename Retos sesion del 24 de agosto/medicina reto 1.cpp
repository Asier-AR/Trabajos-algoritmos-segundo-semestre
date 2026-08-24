#include <iostream>
using namespace std;
namespace Salud //creacion del paquete salud
{
    


class Persona{
    private:

    string tipoDoc;
    int documento;
    string nombre;
    string apellido;
    double peso;
    double estatura;
    int edad;
    string sexo;

    public:
    Persona() {}
    
    void pedirDatos()
    {   cout<<"-------INGRESO DE DATOS-------"<<endl;
        cout<<"Ingrese el nombre del paciente"<<endl;
        cin>> nombre;

        cout<<"Ingrese el apellido del paciente"<<endl;
        cin>> apellido;

        cout<<"Ingrese el sexo del paciente"<<endl;
        cin>> sexo;

        cout<<"Ingrese el tipo de documento del paciente"<<endl;
        cin>>tipoDoc;

        cout<<"Ingrese el numero de documento del paciente"<<endl;
        cin>>documento;

        cout<<"Ingrese la edad del paciente"<<endl;
        cin>>edad;

        cout<<"Ingrese el peso del paciente en kg"<<endl;
        cin>>peso;

        cout<<"Ingrese la estatura del paciente"<<endl;
        cin>>estatura;

        cout<<"------------------------------"<<endl;
    }

    void mostrarDatos()
    {
        cout<<"Nombre y apellido :"<<nombre<<" "<<apellido<<endl;
        cout<<"Sexo: "<<sexo<<endl;
        cout<<"Edad: "<<edad<<endl;
        cout<<"Tipo de documento: "<<tipoDoc<<endl;
        cout<<"Documento: "<<documento<<endl;
        cout<<"Peso: "<<peso<<endl;
        cout<<"Estatura: "<<estatura<<endl;
    }

    string calcularlmc()
    {   string retorno;

        if (peso== 0 or peso<0)
        {
            retorno="Peso invalido para calcular el lmc";
            return retorno;
        }


        double pesoActual= (double) peso / (estatura * estatura);

        if (pesoActual<20)
        {
            retorno="El peso esta debajo de lo ideal";
            return retorno;
        }

        else if (20<=pesoActual and pesoActual<=25)
        {
            retorno="El peso es ideal";
            return retorno;
        }

        else if (25<pesoActual)
        {
            retorno="El paciente tiene sobrepeso";
            return retorno;
        }

        retorno="problemas tecnicos para calcular el lmc";
        return retorno;
    }

    void mayorEdad()
    {
        if (edad<18)
        {
            cout<<"El paciente es menor de edad "<<endl;
        }

        else if (edad>=18)
        {
            cout<<"El paciente es mayor de edad"<<endl;
        }
    }

    //Los metodos no piden datos debido a que viven en el mismo espacio que la clase paciente por lo que se registran desde un primer momento
};
}//fin del paquete salud

namespace Principal
{
    class Inicio
    {   
        private:
       Inicio(){}

       public:
        
       static void ejecutor(){ //el static determina que la funcion pertenece a la clase haciendo que no se tenga que crear un objeto nuevo
       
        Salud::Persona paciente1;

        paciente1.pedirDatos();
        paciente1.mostrarDatos();
        string resultadoLmc=paciente1.calcularlmc();

        if (resultadoLmc=="Peso invalido para calcular el lmc")
        {
            cout<<resultadoLmc<<endl;
        }

        else if (resultadoLmc== "El peso esta debajo de lo ideal")
        {
            cout<<resultadoLmc<<endl;
        }

        else if (resultadoLmc== "El peso es ideal")
        {
            cout<<resultadoLmc<<endl;
        }

        else if(resultadoLmc== "El paciente tiene sobrepeso" )
        {
            cout<<resultadoLmc<<endl;
        }

        else 
        {
            cout<<"Error de calculo"<<endl;
        }

        paciente1.mayorEdad();

    }

    };



}
int main ()
{

Principal:: Inicio::ejecutor(); //se llama la funcion ejecutor perteneciente a la clase Inicio que a su ves pertenece al paquete principal
return 0;
}