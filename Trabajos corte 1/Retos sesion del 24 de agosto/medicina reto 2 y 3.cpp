#include <iostream>
using namespace std;
namespace Salud //creacion del paquete salud
{
    


class Persona{
    protected:

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
    
    void pedirDatos(string rol="Paciente")
    {   cout<<"-------INGRESO DE DATOS del "<<rol<<"-------"<<endl;
        cout<<"Ingrese el nombre del "<<rol<<endl;
        cin>> nombre;

        cout<<"Ingrese el apellido del "<<rol<<endl;
        cin>> apellido;

        cout<<"Ingrese el sexo del "<<rol<<endl;
        cin>> sexo;

        cout<<"Ingrese el tipo de documento del "<<rol<<endl;
        cin>>tipoDoc;

        cout<<"Ingrese el numero de documento del "<<rol<<endl;
        cin>>documento;

        cout<<"Ingrese la edad del "<<rol<<endl;
        cin>>edad;

        cout<<"Ingrese el peso del "<<rol<<" en kg"<<endl;
        cin>>peso;

        cout<<"Ingrese la estatura del "<<rol<<" en metros"<<endl;
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

    // Getters (Lectura de todos los atributos)
    string getTipoDoc() const { return tipoDoc; }
    int getDocumento() const { return documento; }
    string getNombre() const { return nombre; }
    string getApellido() const { return apellido; }
    double getPeso() const { return peso; }
    double getEstatura() const { return estatura; }
    int getEdad() const { return edad; }
    string getSexo() const { return sexo; }

    //setters (entrada de los atributos)
    void setTipoDoc(string td) { tipoDoc = td; }
    void setDocumento(int d) { documento = d; }
    void setNombre(string n) { nombre = n; }
    void setApellido(string a) { apellido = a; }
    void setPeso(double p) { peso = p; }
    void setEstatura(double e) { estatura = e; }
    void setEdad(int ed) { edad = ed; }
    void setSexo(string s) { sexo = s; }



};
class Empleado: public Persona //Indica que todos los metodos publicos de la clase persona seguiran siendo publicos en esta clase empleado
{
    private:
    double valorHora;
    double horasTrabajadas;
    string cargo;
    string departamento;

    public:
    Empleado(): Persona(){}
    void pedirdatos()
    {
        pedirDatos("Empleado"); //le digo que use el metodo pedir datos de la clase padre Persona

        cout<<"Ingrese el cargo"<<endl;
        cin>>cargo;
        
        cout<<"Ingrese el departamente"<<endl;
        cin>>departamento;

        cout<<"Ingrese el valor por hora de su trabajo"<<endl;
        cin>>valorHora;

        cout<<"Ingrese cuantas horas ha trabajado";
        cin>>horasTrabajadas;


    }

    void calcularHonorarios()
    {
       
        Persona:: mostrarDatos();
        double Reteica, valor, valorFinal;
       
       valor= valorHora * horasTrabajadas;
       Reteica= valor* 0.00966;
       valorFinal= valor-Reteica;

        cout<<"Departamento: "<<departamento<<endl;
        cout<<"Cargo: "<<cargo<<endl;
        cout<<"Horas trabajadas: "<<horasTrabajadas<<endl;
        cout<<"Valor de las horas trabajadas: "<<valorHora<<endl; 
        cout<<"Valor final: "<<valorFinal<<endl;
    }
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

        Salud::Empleado empleado1;

        empleado1.pedirDatos();
        empleado1.calcularHonorarios();

    }

    };



}
int main ()
{

Principal:: Inicio::ejecutor(); //se llama la funcion ejecutor perteneciente a la clase Inicio que a su ves pertenece al paquete principal
return 0;
}