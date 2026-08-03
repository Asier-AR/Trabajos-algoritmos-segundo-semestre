
#include <iostream>
using namespace std;

int main()
{
  double edadBebe, pesoBebe;
  double dosisMedicamento;
  
  cout<<"Ingrese la edad del bebe"<<endl;
  cin>>edadBebe;
  
  while (edadBebe<=0)
  {
    cout<<"Usted ingreso una edad invalida por favor ingrese una edad valida";
    cin>>edadBebe;
  }
  
  cout<<"ingrese el peso del Bebe"<<endl;
  cin>>pesoBebe;
  
  dosisMedicamento= ((pesoBebe+10)/(edadBebe*10))*8;
  
  cout<<"Tiene que dar una dosis de "<<dosisMedicamento<<" ml";
}