#include <iostream>
#include <vector>
#include <list>
#include <string>
using namespace std;
class TablaHash{
private:
    int cap;
    int n;
    vector<list<pair<string, string>>> cubetas;
public:
    TablaHash(int capacidad=8):cap(capacidad),n(0),cubetas(capacidad){}

int hashear(const string & clave) const {
        unsigned long long h = 0;
        for (unsigned char c : clave) h = (h * 31 + c) % cap;
        return (int)h;
    }
    void insertar(const string& clave, const string& valor) {
        int i = hashear(clave);
        for (auto& par : cubetas[i]) {
            if (par.first == clave) { par.second = valor; return; }   // ACTUALIZA
        }
        cubetas[i].push_back({clave, valor});
        n++;
    }
    bool buscar(const string& clave, string& salida) const {
        int i = hashear(clave);
        for (const auto& par : cubetas[i]) {
            if (par.first == clave) { salida = par.second; return true; }
        }
        return false;
    }
    bool eliminar(const string& clave) {
        int i = hashear(clave);
        for (auto it = cubetas[i].begin(); it != cubetas[i].end(); ++it) {
            if (it->first == clave) { cubetas[i].erase(it); n--; return true; }
        }
        return false;
    }
};

int main()
{
    TablaHash tabla(8);

tabla.insertar("EST-2026-0101", "Ana Torres");
tabla.insertar("EST-2026-0107", "Pedro Ruiz");
tabla.insertar("EST-2026-0102", "Carlos Rojas");
tabla.insertar("EST-2026-0108", "Camila Diaz");
tabla.insertar("EST-2026-0103", "Diego Pardo");
tabla.insertar("EST-2026-0109", "Luis Herrera");
tabla.insertar("EST-2026-0104", "Sofia Mejia");
tabla.insertar("EST-2026-0110", "Valentina Cruz");
tabla.insertar("EST-2026-0105", "Juan Gomez");
tabla.insertar("EST-2026-0111", "Andres Vega");
tabla.insertar("EST-2026-0106", "Maria Lopez");
tabla.insertar("EST-2026-0112", "Laura Castro");

string valor;
bool busqueda = tabla.buscar("EST-2026-0107", valor);

cout<<"Resultado de la búsqueda: " << busqueda<< endl;
cout<<"Valor encontrado: " << valor << endl;
return 0;
}