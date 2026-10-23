// ============================================================
//  Prueba corta · Segundo corte · EJERCICIO 4  (25 puntos)
//  Tema: mapas y conjuntos
//  Sistema: RedAcopio — consolidado de recoleccion por zona
//
//  Este archivo NO tiene main(): el main esta en pruebas_e4.cpp
//  NO MODIFIQUE el archivo pruebas_e4.cpp
//  Compile y ejecute:
//     g++ -std=c++17 -g -o pruebas_e4 zonas.cpp pruebas_e4.cpp
//     ./pruebas_e4
// ============================================================
#include <vector>
#include <string>
#include <map>
#include <set>
using namespace std;

// Debe hacer TRES cosas:
//   1. llenar 'totales' con los kilos acumulados por zona
//   2. llenar 'repetidas' con las zonas que aparecen en MAS DE UN registro
//   3. devolver el nombre de la zona con mayor total acumulado
//
// Si 'reg' esta vacio, devuelva la cadena vacia "" y no agregue nada.
//
// PENDIENTE: implementar el cuerpo de la funcion.

string zonaMayor(const vector<pair<string,int>>& reg,
                 map<string,int>& totales,
                 set<string>& repetidas) {
    
    for (const auto& [zona, kilos] : reg) {
        // Acumular los kilos por zona
        totales[zona] += kilos;
        
        // Verificar si la zona ya estaba en el mapa de totales
        if (totales[zona] > kilos) {
            repetidas.insert(zona);
        }
    }

    // Encontrar la zona con el mayor total acumulado
    string zona_maxima;
    int max_kilos = 0;
    for (const auto& [zona, total] : totales) {
        if (total > max_kilos) {
            max_kilos = total;
            zona_maxima = zona;
        }
    }
    return zona_maxima;
}
