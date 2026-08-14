#include <iostream>
using namespace std;

 int main()
 {
    int n, k;
    n=4;
    k=2;
   string matriz[n][k]={{"Secilia", "+57 300 123 4567"},
                        {"Alfonzo", "+57 315 987 6543"},                              
                        {"Matheo",  "+57 320 555 0192"},
                        {"Sofia",    "+57 311 404 0101"}};
 
cout<<"Nombre\t\tTelefono"<<endl;  //\t\t significa que habra un espacio de 2 tabulaciones                      

    for (int i=0; i<n; i++)
    {
        for (int j=0; j<k; j++)
        {
            cout<<matriz[i][j]<<"\t\t";
        }
        cout<<endl;
    }

 }