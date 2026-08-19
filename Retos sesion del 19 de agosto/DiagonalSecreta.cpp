#include <iostream>
using namespace std;


int main()
{   
int suma, principal, secundaria, N;
N=3;
suma=0; 
    
int matriz[N][N]= {{1,2,3},
                   {4,5,6},
                   {7,8,9}};

for (int i=0; i<N; i++) //halla la diagonal principal 
    {
        suma=suma + matriz[i][i];
    }
principal=suma;
suma=0;
for (int j=0; j<N; j++)
    {
        suma=suma+ matriz [j][N-1-j];
    }
secundaria=suma;

cout<<"Diagonal principal: "<<principal<<endl;

cout<<"Diagonal secundaria: "<<secundaria<<endl;

return 0;
}