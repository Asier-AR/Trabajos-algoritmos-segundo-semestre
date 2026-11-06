//quis sesion del 6 de noviembre 2026

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

const int N = 9;
const vector<string> NOMBRES = {"CENTRO","NORTE","SUR","ORIENTE","OCCIDENTE",
                                "CHAPINERO","USAQUEN","BOSA","VEREDA"};
const vector<pair<int,int>> ARISTAS = {{0,1},{1,4},{0,2},{0,3},{1,5},
                                       {2,7},{3,6},{5,6},{4,7},{7,8},
                                       {7,5},{5,8},{2,6},{6,8},
                                       {1,8},{5,2}};  

vector<vector<int>> lista(N);

string unir(const vector<int>& v) {
    string s;
    for (size_t i = 0; i < v.size(); i++) {
        if (i) s += " -> ";
        s += NOMBRES[v[i]];
    }
    return s;
}

// ---------- DFS recursivo ----------
void dfsRec(int u, vector<bool>& vis, vector<int>& orden,
            int prof = 0, vector<string>* traza = nullptr) {
    vis[u] = true;
    orden.push_back(u);
    if (traza) traza->push_back(string(2 * prof, ' ') + "entra " + NOMBRES[u]);
    for (int v : lista[u]) {
        if (!vis[v]) dfsRec(v, vis, orden, prof + 1, traza);
        else if (traza)
            traza->push_back(string(2 * (prof + 1), ' ') + NOMBRES[v] + " ya visitado, no entra");
    }
    if (traza) traza->push_back(string(2 * prof, ' ') + "sale  " + NOMBRES[u]);
}

// ---------- DFS iterativo con pila ----------
vector<int> dfsIter(int inicio) {
    vector<bool> vis(N, false);
    vector<int> pila{inicio}, orden;
    while (!pila.empty()) {
        int u = pila.back(); pila.pop_back();          // LIFO
        if (vis[u]) continue;
        vis[u] = true;
        orden.push_back(u);
        for (auto it = lista[u].rbegin(); it != lista[u].rend(); ++it)   // al reves
            if (!vis[*it]) pila.push_back(*it);
    }
    return orden;
}

// ---------- Aplicacion 1: componentes conexas ----------
vector<vector<string>> componentes() {
    vector<bool> vis(N, false);
    vector<vector<string>> comps;
    for (int s = 0; s < N; s++) {
        if (!vis[s]) {
            vector<int> o;
            dfsRec(s, vis, o);
            vector<string> nombres;
            for (int i : o) nombres.push_back(NOMBRES[i]);
            comps.push_back(nombres);
        }
    }
    return comps;
}

void imprimirComps(const vector<vector<string>>& comps) {
    cout << "[";
    for (size_t i = 0; i < comps.size(); i++) {
        cout << "[";
        for (size_t j = 0; j < comps[i].size(); j++)
            cout << comps[i][j] << (j + 1 < comps[i].size() ? ", " : "");
        cout << "]" << (i + 1 < comps.size() ? ", " : "");
    }
    cout << "]" << endl;
}

// ---------- Aplicacion 2: deteccion de ciclo ----------
bool explorar(int u, int padre, vector<bool>& vis) {
    vis[u] = true;
    bool padreSaltado = false;
    for (int v : lista[u]) {
        if (v == padre && !padreSaltado) {  
            padreSaltado = true;
            continue;
        }
        if (!vis[v]) {
            if (explorar(v, u, vis)) return true;
        } else {
            return true;                     
        }
    }
    return false;
}

bool hayCiclo() {
    vector<bool> vis(N, false);
    for (int s = 0; s < N; s++)
        if (!vis[s] && explorar(s, -1, vis)) return true;
    return false;
}

int main() {
    // construir la lista de adyacencia
    for (auto [u, v] : ARISTAS) { lista[u].push_back(v); lista[v].push_back(u); }
    for (auto& v : lista) sort(v.begin(), v.end());

    // DFS recursivo con traza
    vector<bool> vis(N, false);
    vector<int> orden;
    vector<string> traza;
    dfsRec(0, vis, orden, 0, &traza);
    cout << "DFS RECURSIVO desde CENTRO" << endl;
    for (auto& t : traza) cout << "  " << t << endl;
    cout << "  orden de visita: " << unir(orden) << endl;

    // DFS iterativo
    cout << "\nDFS ITERATIVO (con pila explicita) desde CENTRO" << endl;
    cout << "  orden de visita: " << unir(dfsIter(0)) << endl;

    // componentes de la red completa
    cout << "\nCOMPONENTES CONEXAS de la red completa: ";
    imprimirComps(componentes());

    // red con tramos cortados
    vector<vector<int>> listaRota(N);
    for (auto [u, v] : vector<pair<int,int>>{{0,1},{0,2},{3,6}}) {
        listaRota[u].push_back(v);
        listaRota[v].push_back(u);
    }
    auto listaOrig = lista;
    lista = listaRota;
    cout << "COMPONENTES de una red con tramos cortados: ";
    imprimirComps(componentes());
    lista = listaOrig;

    // ciclo
    cout << "¿La red tiene algun circuito? " << (hayCiclo() ? "true" : "false") << endl;
    return 0;
}