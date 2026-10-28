#include <iostream>
using namespace std;

struct Nodo {
    string dato;
    Nodo*  izq;      // puntero: puede valer nullptr
    Nodo*  der;
    Nodo(string d) : dato(d), izq(nullptr), der(nullptr) {}
};

void Escritor(Nodo* x)
{   
    if (x->dato!="" and x!=nullptr)
    {
        cout<<x->dato<<"\t";
    }

    if (x->der== nullptr and x->izq==nullptr)
    {
        return;
    } 

    if(x->izq!=nullptr)
    {
       Escritor(x->izq); 
    }

    if (x->der!=nullptr)
    {
        Escritor(x->der);
    }
   
}

Nodo* Espejo(Nodo* x)
{
    if (x == nullptr) return nullptr;

    Nodo* nuevo = new Nodo(x->dato);
    nuevo->izq = Espejo(x->der);
    nuevo->der = Espejo(x->izq);

    return nuevo;
}

bool comparar(Nodo* x, Nodo* y)
{   
    if (x==nullptr and y==nullptr) return true;

    if (x==nullptr or y==nullptr) return false;

   return comparar(x->der, y->der) and comparar(x->izq, y->izq);
}

void liberar(Nodo* x)
{
    if (x==nullptr) return;

    liberar(x->der);
    liberar(x->izq);
    delete x;
}

int main()
{
Nodo* raiz = new Nodo("CATALOGO");
raiz->izq=new Nodo("Herramienta");
raiz->izq->izq= new Nodo("Taladro");
raiz->izq->der= new Nodo("Sierra");
raiz->der= new Nodo("Libro");
raiz->der->izq= new Nodo("Arte");
raiz->der->der= new Nodo("Tecnico");
raiz->der->der->der= new Nodo("Redes");

Nodo* raizInvertida= Espejo(raiz);

Escritor(raiz);
cout<<endl;
Escritor(raizInvertida);
bool comparacion=comparar(raiz, raizInvertida);
cout<<endl;
cout<<"¿Son iguales? : "<< comparacion;

liberar(raiz);
liberar(raizInvertida);
return 0;
}
// ... y alguien tendra que hacer delete mas adelante.

