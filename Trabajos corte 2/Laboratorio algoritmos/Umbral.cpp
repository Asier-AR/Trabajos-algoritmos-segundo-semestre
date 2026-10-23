#include <iostream> 
#include <vector> 
using namespace std; 
int contar(const vector<int>& v, int n, int umbral) { 
if (n < 0){ return 0;}                            
if (v[n] >= umbral) { return 1 + contar(v, n - 1, umbral);}  //el principal error se encontraba en el hecho de trataba de acceder a n y no a n-1 es decir una posicion que no existe

return contar(v, n - 1, umbral); 
}

int main ()
{
 vector<int> v={12, 45, 7, 38, 60, 19, 23};
 int n=v.size()-1;
 int umbral=10;
 
 cout<<contar(v, n, umbral);

 

}