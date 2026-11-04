// quis 28/10/2026

#include <iostream>
#include <vector> //debido a que se necesitan estructuras de datos tipo listas
#include <string> //para permitir usar el sufijo string
#include <algorithm> //para usar funciones como maximo minimo etc
using namespace std;

// BST 50,30,70,20,40,60,80 y 35
// medir cuantos hijos tiene cada nodo antes de eliminar.

struct Nodo {
    int dato;
    string nombre;
    Nodo* izq;
    Nodo* der;
    Nodo(int d, string nom = "") : dato(d), nombre(nom), izq(nullptr), der(nullptr) {}
};

Nodo* insertar(Nodo* n, int clave, string nombre = "")
{
    if (n == nullptr) return new Nodo(clave, nombre);
    if (clave < n->dato) n->izq = insertar(n->izq, clave, nombre);
    else if (clave > n->dato) n->der = insertar(n->der, clave, nombre);
    return n;
}

Nodo* buscar(Nodo* n, int clave, vector<string>* pasos = nullptr)
{
    if (pasos != nullptr) pasos->push_back(n == nullptr ? "vacio" : to_string(n->dato));
    if (n == nullptr || n->dato == clave) return n;
    if (clave < n->dato) return buscar(n->izq, clave, pasos);
    return buscar(n->der, clave, pasos);
}

Nodo* minimo(Nodo* n)
{
    while (n->izq != nullptr) n = n->izq;
    return n;
}

Nodo* maximo(Nodo* n)
{
    while (n->der != nullptr) n = n->der;
    return n;
}

Nodo* eliminar(Nodo* n, int clave)
{
    if (n == nullptr) return nullptr;
    if (clave < n->dato) n->izq = eliminar(n->izq, clave);
    else if (clave > n->dato) n->der = eliminar(n->der, clave);
    else // encontramos el nodo a eliminar
    {
        if (n->izq == nullptr) { Nodo* t = n->der; delete n; return t; }
        if (n->der == nullptr) { Nodo* t = n->izq; delete n; return t; }
        Nodo* suc = minimo(n->der);
        n->dato = suc->dato;
        n->nombre = suc->nombre;
        n->der = eliminar(n->der, suc->dato);
    }
    return n;   // fuera del else
}

void inorden(Nodo* n, vector<int>& s)
{
    if (n == nullptr) return;
    inorden(n->izq, s);
    s.push_back(n->dato);
    inorden(n->der, s);
}

int altura(Nodo* n)
{
    if (n == nullptr) return -1;
    return 1 + max(altura(n->izq), altura(n->der));
}

int hijos(Nodo* n, int clave)
{
    n = buscar(n, clave);
    if (n == nullptr) return -1;
    return (n->izq ? 1 : 0) + (n->der ? 1 : 0);
}

void imprimir(const vector<int>& s)
{
    cout << "[";
    for (size_t i = 0; i < s.size(); i++)
        cout << s[i] << (i + 1 < s.size() ? ", " : "");
    cout << "]" << endl;
}

void liberar(Nodo* n)
{
    if (n == nullptr) return;
    liberar(n->izq);
    liberar(n->der);
    delete n;
}

int main()
{
    Nodo* raiz = nullptr;
    int datos[] = {50, 30, 70, 20, 40, 60, 80, 35};
    for (int c : datos) raiz = insertar(raiz, c);

    vector<int> s;
    inorden(raiz, s);
    cout << "Inorden (queda ordenado): ";
    imprimir(s);
    cout << "minimo = " << minimo(raiz)->dato
         << "  maximo = " << maximo(raiz)->dato
         << "  altura = " << altura(raiz) << endl;

    for (int objetivo : {40, 65})
    {
        vector<string> p;
        Nodo* r = buscar(raiz, objetivo, &p);
        string camino;
        for (size_t i = 0; i < p.size(); i++)
            camino += (i ? " ->" : "") + p[i];
        cout << "buscar(" << objetivo << "): camino " << camino << "  => "
             << (r ? "ENCONTRADO" : "NO ESTA")
             << " (" << p.size() << " comparaciones)" << endl;
    }

    string NOMBRE[] = {"caso 1: hoja, 0 hijos", "caso 2: un hijo", "caso 3: dos hijos"};
    for (int clave : {20, 30, 50})
    {
        int k = hijos(raiz, clave);          // se mide ANTES de eliminar
        raiz = eliminar(raiz, clave);
        vector<int> t;
        inorden(raiz, t);
        cout << "eliminar(" << clave << ") [" << NOMBRE[k] << "] -> ";
        imprimir(t);
    }

    Nodo* deg = nullptr;
    for (int c : {10, 20, 30, 40, 50, 60, 70, 80}) deg = insertar(deg, c);

    cout << "\nBST con datos ordenados: altura = " << altura(deg)
         << " con 8 nodos (una lista enlazada)" << endl;
    cout << "BST con datos mezclados: altura = " << altura(raiz)
         << " con 5 nodos (tras las 3 eliminaciones)" << endl;

    liberar(raiz);
    liberar(deg);
    return 0;
}