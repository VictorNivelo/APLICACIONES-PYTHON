# Algorirmo de Floyd

# funcion Floyd(Grafo):
#     n = numero de vertices de Grafo
#     distania = matriz de n x n con infinito en todas las celdas
#     Para cada arista(origen, destino) en Grafo Hacer:
#         distancia[origen][destino] = perso de la arista[origen][destino]
#     Fin para
#     Para nodo origen de 0 a n Hacer:
#         distancia[origen][origen] = 0
#     Fin para
#     Para k desde 0 a n Hacer:
#         Para i desde 0 a n Hacer:
#             Para j de 0 a n Hacer:
#                 Si distancia[i][j] > min(distancia[i][j], distancia[i][k] + distancia[k][j])
#             Fin para
#         Fin para
#     Fin para
#     Retornar distancia
# Fin funcion


# Calculo de complejidad

# funcion Floyd(Grafo):
#     n = numero de vertices de Grafo                                                               -> 1
#     distania = matriz de n x n con infinito en todas las celdas                                   -> n(n-1)
#     Para cada arista(origen, destino) en Grafo Hacer:                                             -> n
#         distancia[origen][destino] = perso de la arista[origen][destino]                          -> n-1
#     Fin para                                                                                      -> n-1
#     Para nodo origen de 0 a n Hacer:                                                              -> n
#         distancia[origen][origen] = 0                                                             -> n-1
#     Fin para                                                                                      -> n
#     Para k desde 0 a n Hacer:                                                                     -> n (n-1)
#         Para i desde 0 a n Hacer:                                                                 -> n (n(n-1)-1)
#             Para j de 0 a n Hacer:                                                                -> n (n(n(n-1)-1)-1)
#                 Si distancia[i][j] > min(distancia[i][j], distancia[i][k] + distancia[k][j])      -> n (n(n(n-1)-1)-1)
#             Fin para
#         Fin para
#     Fin para
#     Retornar distancia
# Fin funcion
#                                                                                                   ---------------------------
#                                                                                                   = 3n^3 - n^2 - 2n - 4


# Codigo

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def floyd_warshall_with_steps(graph):
    n = graph.number_of_nodes()
    distancia = np.full((n, n), float("inf"))

    for origen, destino, datos in graph.edges(data=True):
        peso = datos.get("weight", 1)
        distancia[origen - 1][destino - 1] = peso

    for origen in range(n):
        distancia[origen][origen] = 0

    print("Matriz de distancias inicial:")
    print(pd.DataFrame(distancia))

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distancia[i][j] > distancia[i][k] + distancia[k][j]:
                    distancia[i][j] = distancia[i][k] + distancia[k][j]
        print(f"\nIteración {k + 1}:")
        print("Matriz de distancias actualizada:")
        print(pd.DataFrame(distancia))

    return distancia


# Inicialización del grafo
grafo = nx.DiGraph()

numero_nodos = int(input("Ingrese el numero de nodos: "))
nodos = list(range(1, numero_nodos + 1))
grafo.add_nodes_from(nodos)

numero_aristas = int(input("Ingrese el numero de aristas: "))
for _ in range(numero_aristas):
    datos = input("Ingrese los datos de la arista (origen destino peso): ").split()
    if len(datos) != 3:
        print("Entrada inválida. Por favor, ingrese los datos en el formato correcto.")
        continue
    origen, destino, peso = int(datos[0]), int(datos[1]), int(datos[2])
    direccion = int(input("Si la arista es bidireccional ingrese 1, si no ingrese 2: "))
    if direccion == 1:
        grafo.add_edge(origen, destino, weight=peso)
        grafo.add_edge(destino, origen, weight=peso)
    else:
        grafo.add_edge(origen, destino, weight=peso)

# Dibujar el grafo
pos = nx.spring_layout(grafo)
nx.draw(grafo, pos, with_labels=True, font_weight="bold")
aristas = nx.get_edge_attributes(grafo, "weight")
nx.draw_networkx_edge_labels(grafo, pos, edge_labels=aristas)
plt.show()

# Calcular las distancias usando Floyd-Warshall con pasos intermedios
distancias = floyd_warshall_with_steps(grafo)
nodos = list(grafo.nodes())
matriz = pd.DataFrame(distancias, index=nodos, columns=nodos)
print("\nLa matriz de distancias final es: ")
print(matriz)


# Codigo en C

# #include <stdio.h>
# #include <stdlib.h>
# #include <limits.h>

# #define INF INT_MAX

# void floydWarshall(int **dist, int n) {
#     for (int k = 0; k < n; k++) {
#         for (int i = 0; i < n; i++) {
#             for (int j = 0; j < n; j++) {
#                 if (dist[i][k] != INF && dist[k][j] != INF && dist[i][j] > dist[i][k] + dist[k][j]) {
#                     dist[i][j] = dist[i][k] + dist[k][j];
#                 }
#             }
#         }
#     }
# }

# int main() {
#     int numero_nodos, numero_aristas;

#     printf("Ingrese el numero de nodos: ");
#     scanf("%d", &numero_nodos);

#     // Inicializar la matriz de distancias
#     int **dist = (int **)malloc(numero_nodos * sizeof(int *));
#     for (int i = 0; i < numero_nodos; i++) {
#         dist[i] = (int *)malloc(numero_nodos * sizeof(int));
#         for (int j = 0; j < numero_nodos; j++) {
#             if (i == j)
#                 dist[i][j] = 0;
#             else
#                 dist[i][j] = INF;
#         }
#     }

#     printf("Ingrese el numero de aristas: ");
#     scanf("%d", &numero_aristas);

#     for (int i = 0; i < numero_aristas; i++) {
#         int origen, destino, peso, direccion;
#         printf("Ingrese los datos de la arista (origen destino peso): ");
#         scanf("%d %d %d", &origen, &destino, &peso);
#         printf("Si la arista es bidireccional ingrese 1, si no ingrese 2: ");
#         scanf("%d", &direccion);

#         dist[origen - 1][destino - 1] = peso;
#         if (direccion == 1) {
#             dist[destino - 1][origen - 1] = peso;
#         }
#     }

#     floydWarshall(dist, numero_nodos);

#     printf("\nLa matriz de distancias es:\n");
#     for (int i = 0; i < numero_nodos; i++) {
#         for (int j = 0; j < numero_nodos; j++) {
#             if (dist[i][j] == INF)
#                 printf("INF ");
#             else
#                 printf("%d ", dist[i][j]);
#         }
#         printf("\n");
#     }

#     for (int i = 0; i < numero_nodos; i++) {
#         free(dist[i]);
#     }
#     free(dist);

#     return 0;
# }
