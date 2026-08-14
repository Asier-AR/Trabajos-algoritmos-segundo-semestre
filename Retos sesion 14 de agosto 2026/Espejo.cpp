#include <iostream>
using namespace std;

int main () {

int n, j;

n=7;
j=n-1;
int palindromo[n]={4, 3, 2, 5, 2, 3, 4};
bool palindromo1= true;

for (int i=0; i<n; i++)
{  
    if (palindromo[i]!=palindromo[j])
    {
    palindromo1=false;
    break;
    }

    j-=1;
}

if (palindromo1== true)
{
    cout<<"El arreglo es un palindromo"<<endl;
}

else 
{
    cout<<"El arreglo no es un palindromo"<<endl;
}

return 0;
}