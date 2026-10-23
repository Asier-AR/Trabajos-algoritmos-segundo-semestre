#include <vector>
# include <iostream> 
# include <algorithm>
using namespace std;


vector<int> fusionar(const vector<int>& a, const vector<int>& b)
{
    vector<int> c;
    int i = 0, j = 0;
    while (i < a.size() && j < b.size())
    {
        if (a[i] < b[j])
        {
            c.push_back(a[i]);
            i++;
        }
        else
        {
            c.push_back(b[j]);
            j++;
        }
    }
    // Agregar los elementos restantes de cualquiera de los vectores
    while (i < a.size())
    {
        c.push_back(a[i]);
        i++;
    }
    while (j < b.size())
    {
        c.push_back(b[j]);
        j++;
    }
    return c;
}

int main()
{
 vector<int> a = {5, 18, 27, 40};
 vector<int> b = {9, 18, 33};
 vector<int> c = fusionar(a, b);
 for (int i = 0; i < c.size(); i++)
 {
     cout << c[i] << " ";
 }
 return 0;
}
