# include <iostream>
#include <vector>
using namespace std;
// entrada : [73, 74, 75, 71, 69, 72, 76, 73]
// salida : [1, 1, 4, 2, 1, 1, 0, 0]
vector<int> temperatura(vector<int> a){
    int n=a.size(); //tamaño del vector
    vector<int> res(n); //crea el vector de resultados que tendra un tamaño n
    for(int i=0;i<n;i++){ //recorre el vector a //contador de temperaturas mayores
        for(int j=i+1;j<n;j++){ //recorre el vector a desde la posición i+1 hasta el final
            if(a[j]>a[i]){ //si la temperatura en la posicion j es mayor que la temperatura en la posición i
                res[i]=j-i; //asigna el valor de j-i al vector de resultados en la posición i
                break; //sale del bucle 
            }
        }
    }  
    return res;
}

int main (){
    vector<int> a={73, 74, 75, 71, 69, 72, 76, 73}; //vector de temperaturas
    vector<int> res=temperatura(a); //llama a la función temperatura y guarda el resultado en res
    for(int i=0;i<res.size();i++){ //recorre el vector de resultados
        cout<<res[i]<<" "; //imprime el valor del vector de resultados en la posición i
    }
    return 0;
}
