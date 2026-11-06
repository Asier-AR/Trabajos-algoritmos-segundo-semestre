//quis del 6 de noviembre del 2026

#include <iostream>
#include <vector>
#include <queue>
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


void bfs(int inicio, vector<int>& dist, vector<int>& padre) {
    vector<bool> vis(N, false);
    queue<int> cola;
    vis[inicio] = true; 
    dist[inicio] = 0;
    cola.push(inicio);
    while (!cola.empty()) {
        int u = cola.front(); cola.pop(); //se le asigna el valor de la cola a letra u y se elimina de la cola
        for (int v : lista[u]) { //se recorre la lista de adyacencia de u
            if (!vis[v]) { //si no ha sido visitado
                vis[v] = true;     //se marca como visitado
                dist[v] = dist[u] + 1; //se le asigna la distancia de u + 1 a v
                padre[v] = u; //se le asigna a v el valor de u como padre
                cola.push(v); //se encola v
            }
        }
    }
}

int main() {
    // 1. construir la lista de adyacencia
    for (auto [u, v] : ARISTAS) { lista[u].push_back(v); lista[v].push_back(u); }
    for (auto& v : lista) sort(v.begin(), v.end());

    // 2. BFS desde CENTRO
    vector<int> dist(N, -1), padre(N, -1); //se declaran dos vectores de tipo entero con la misma cantidad de elementos N que estan llenos de -1
    bfs(0, dist, padre); //se llama a la funcion bfs con los parametros 0, dist y padre
    cout<< "Colores de los sitios"<<endl;
    cout<< "Centro-> azul "<<endl<<"Oriente, Sur, Norte -> verde"<<endl<<"Occidente, Chapinero, Usaquen, Bosa -> rojo"<<endl<<"vereda -> blanco"<<endl;

    // 4. Camino mas corto CENTRO -> VEREDA
    int destino = 8;
    cout << "Camino mas corto desde centro hasta vereda (en numero de tramos): "
         << dist[destino] << endl;

    vector<int> camino;
    for (int v = destino; v != -1; v = padre[v]) camino.push_back(v);
    reverse(camino.begin(), camino.end());

    for (size_t i = 0; i < camino.size(); i++) {
        cout << NOMBRES[camino[i]];
        if (i + 1 < camino.size()) cout << " -> ";
    }
    cout << endl;

    return 0;
}