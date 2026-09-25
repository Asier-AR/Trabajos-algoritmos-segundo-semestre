#include <iostream>
#include <vector>
#include <algorithm> //sirve para hacer max_element
using namespace std;

vector<int> Bucketsort(vector<int> & arr, int numbuckets)
{   if (arr.size()==0)
    {
        return arr;
    }

    vector<vector<int>> buckets;
    for (int i=0; i< numbuckets; i++)
    {
        buckets.push_back({}); 
    }


    for (int j=0; j<arr.size(); j++)
    {   
        int maximoElemento= *max_element(arr.begin(), arr.end()); //se pone el * antes de max_element ya que lo que realmente devuelve es un puntero que apunta al elemento mas grande del arreglo o vector

        int numero= arr[j];
        int normalized= int (numero/(maximoElemento+1)); //es una ecuacion que encontre por internet que sirve para determinar a que cubeta se van a ir los elementos

        int bucketIndice=int(arr.size()* normalized);

        buckets[bucketIndice].push_back(numero);
    }

    vector<int> ordenado={};

    for (int f=0; f<buckets.size(); f++)
    {    sort (buckets[f].begin(), buckets[f].end());
        for (int c=0; c<buckets[f].size(); c++)
        {   
           
            ordenado.push_back(buckets[f][c]);
        }
    }

    return ordenado;
}

int main()
{
  vector<int> lista={4, 8, 3, 12, 9, 7};

  vector <int> ordenar=Bucketsort(lista, 25);

  for (int i=0; i<ordenar.size(); i++)
  {
    cout<<ordenar[i]<<" ";
  }
}

