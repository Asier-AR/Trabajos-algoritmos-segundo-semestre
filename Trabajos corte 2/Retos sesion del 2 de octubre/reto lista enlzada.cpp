#include <cassert>
#include <cstddef>
#include <utility>

template <class T>
class LinkedStack {
    struct Node {
        T dato;
        Node* siguiente;
        Node(const T& d, Node* s) : dato(d), siguiente(s) {}
    };

    Node* cima = nullptr;   // la cima de la pila es la cabeza de la lista
    size_t n = 0;

public:
    LinkedStack() = default;

    // Evita copias accidentales que provocarían doble delete
    LinkedStack(const LinkedStack&) = delete;
    LinkedStack& operator=(const LinkedStack&) = delete;

    ~LinkedStack() {
        while (cima != nullptr) pop();
    }

    void push(const T& x) {
        cima = new Node(x, cima);   // el nuevo nodo apunta a la antigua cima
        ++n;
    }

    void pop() {
        assert(n > 0);
        Node* temp = cima;
        cima = cima->siguiente;
        delete temp;
        --n;
    }

    T& top() {
        assert(n > 0);
        return cima->dato;
    }

    bool empty() const { return n == 0; }
    size_t size() const { return n; }
};