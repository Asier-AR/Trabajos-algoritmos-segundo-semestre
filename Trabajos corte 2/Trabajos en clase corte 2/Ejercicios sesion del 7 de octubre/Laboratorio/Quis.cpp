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
int hashearMala(const string & clave) const {
    unsigned long long h = 0;
    for (size_t i = 0; i < clave.size() && i < 4; i++) h += (unsigned char)clave[i];
    return (int)(h % cap);
}

    double factorCarga() const { return (double)n / cap; }

    void insertar(const string& clave, const string& valor) {
        int i = hashear(clave);
        for (auto& par : cubetas[i]) {
            if (par.first == clave) { par.second = valor; return; }   // ACTUALIZA
        }
        cubetas[i].push_back({clave, valor});
        n++;
        if (factorCarga() > 0.75) redimensionar();
    }
    void insertarMala(const string& clave, const string& valor) {
        int i = hashearMala(clave);
        for (auto& par : cubetas[i]) {
            if (par.first == clave) { par.second = valor; return; }   // ACTUALIZA
        }
        cubetas[i].push_back({clave, valor});
        n++;
        if (factorCarga() > 0.75) redimensionarMala();
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
    void redimensionarMala(){
        vector<list<pair<string, string>>> viejas = cubetas;
        cap *= 2;
        cubetas.assign(cap, list<pair<string, string>>()); n=0;
        
        for (const auto& cubeta : viejas) {
            for (const auto& par : cubeta) {
                insertarMala(par.first, par.second);
            }
        }

    }
    void redimensionar() {
        vector<list<pair<string, string>>> viejas = cubetas;
        cap *= 2;
        cubetas.assign(cap, list<pair<string, string>>()); n=0;
        
        for (const auto& cubeta : viejas) {
            for (const auto& par : cubeta) {
                insertar(par.first, par.second);
            }
        }
    }
    // y al final de insertar():
    //     if (factorCarga() > 0.75) redimensionar();
    int capacidad(){return cap; }
    void mostrarDistribucion() const {
    size_t maxLargo = 0, vacias = 0, total = 0;
    int masLlena = 0;

    for (int i = 0; i < cap; i++) {
        size_t largo = cubetas[i].size();
        total += largo;
        if (largo == 0) vacias++;
        if (largo > maxLargo) {
            maxLargo = largo;
            masLlena = i;
        }
        cout << "cubeta " << i << ": " << largo << " "
             << string(min(largo, (size_t)60), '#') << "\n";
    }

    cout << " |cubeta mas larga: " << masLlena << " con " << maxLargo << " elementos\n"
         << " | cubetas vacias: " << vacias << "/" << cap;
}
};

int main()
{

int capacidad=8;
TablaHash tabla(capacidad);

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


TablaHash tablaMala(capacidad);


tablaMala.insertarMala("EST-2026-0101", "Ana Torres");
tablaMala.insertarMala("EST-2026-0107", "Pedro Ruiz");
tablaMala.insertarMala("EST-2026-0102", "Carlos Rojas");
tablaMala.insertarMala("EST-2026-0108", "Camila Diaz");
tablaMala.insertarMala("EST-2026-0103", "Diego Pardo");
tablaMala.insertarMala("EST-2026-0109", "Luis Herrera");
tablaMala.insertarMala("EST-2026-0104", "Sofia Mejia");
tablaMala.insertarMala("EST-2026-0110", "Valentina Cruz");
tablaMala.insertarMala("EST-2026-0105", "Juan Gomez");
tablaMala.insertarMala("EST-2026-0111", "Andres Vega");
tablaMala.insertarMala("EST-2026-0106", "Maria Lopez");
tablaMala.insertarMala("EST-2026-0112", "Laura Castro");

string valor;
bool busqueda = tabla.buscar("EST-2026-0107", valor);

cout<<"Resultado de la búsqueda Parte A : " << busqueda<< endl;
cout<<"Valor encontrado: " << valor << endl;

cout<<"-----------------------------------------------------------"<<endl;

cout<<"Punto 3"<<endl<<endl;

cout<<"Datos de Hashear Normal"<<endl;
cout<<"Capacidad inicial: "<<capacidad<<endl;
cout<<"Capacidad final: "<<tabla.capacidad()<<endl;
cout<<"Factor de carga: "<<tabla.factorCarga()<<endl;
tabla.mostrarDistribucion();
cout<< endl;

cout<<"-----------------------------------------------------------"<<endl;

cout<<"Datos de Hashear Mala"<<endl;
cout<<"Capacidad inicial: "<<capacidad<<endl;
cout<<"Capacidad final: "<<tablaMala.capacidad()<<endl;
cout<<"Factor de carga: "<<tablaMala.factorCarga()<<endl;
tablaMala.mostrarDistribucion();
cout<< endl;


return 0;

}