#include <iostream>
#include <vector>
#include <list>
using namespace std;

class TablaHash {
private:
    int cap;
    int n;
    vector<list<int>> cubetas;
public:
    TablaHash(int capacidad = 7) : cap(capacidad), n(0), cubetas(capacidad) {}

    int hashear(int x) const {
        return ((x % 7) + 7) % 7;   // evita índices negativos
    }

    void insertar(int x) {
        int i = hashear(x);
        for (int v : cubetas[i]) {
            if (v == x) return;      // ya existe, no se duplica
        }
        cubetas[i].push_back(x);
        n++;
    }

    bool buscar(int x) const {
        int i = hashear(x);
        for (int v : cubetas[i]) {
            if (v == x) return true;
        }
        return false;
    }

    bool eliminar(int x) {
        int i = hashear(x);
        for (auto it = cubetas[i].begin(); it != cubetas[i].end(); ++it) {
            if (*it == x) { cubetas[i].erase(it); n--; return true; }
        }
        return false;
    }
    void imprimir() const {
    for (int i = 0; i < cap; i++) {
        cout << "Bucket " << i << ": ";
        if (cubetas[i].empty()) {
            cout << "vacio";
        } else {
            bool primero = true;
            for (int v : cubetas[i]) {
                if (!primero) cout << " -> ";
                cout << v;
                primero = false;
            }
            cout<<"-> Numero de colisiones: "<<cubetas[i].size();
        }
        cout << endl;
    }
}
};

int main() {
    TablaHash tabla(7);
    tabla.insertar(23);
    tabla.insertar(15);
    tabla.insertar(42);
    tabla.insertar(9);
    tabla.insertar(36);
    tabla.insertar(51);
    tabla.insertar(28);
    tabla.insertar(17);
    tabla.imprimir();
}
