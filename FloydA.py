import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def floyd(graph):
    n = graph.number_of_nodes()
    distancia = np.full((n, n), float("inf"))
    recorrido = np.zeros((n, n), dtype=int)

    for origen, destino, datos in graph.edges(data=True):
        peso = datos.get("weight", 1)
        distancia[origen - 1][destino - 1] = peso
        recorrido[origen - 1][destino - 1] = destino

    for i in range(n):
        for j in range(n):
            if i != j:
                recorrido[i][j] = j + 1
            else:
                recorrido[i][j] = 0

    for origen in range(n):
        distancia[origen][origen] = 0
        recorrido[origen][origen] = 0

    print("\nMatriz de distancias inicial:")
    print(
        pd.DataFrame(
            np.where(np.isfinite(distancia), distancia, "inf"),
            index=range(1, n + 1),
            columns=range(1, n + 1),
        )
    )
    print("\nMatriz de recorrido inicial:")
    print(pd.DataFrame(recorrido, index=range(1, n + 1), columns=range(1, n + 1)))

    matrices_distancias = []
    matrices_recorrido = []

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distancia[i][j] > distancia[i][k] + distancia[k][j]:
                    distancia[i][j] = distancia[i][k] + distancia[k][j]
                    recorrido[i][j] = k + 1

        matrices_distancias.append(np.copy(distancia))
        matrices_recorrido.append(np.copy(recorrido))

        print(f"\nIteración {k + 1}:")
        print("Matriz de distancias actualizada:")
        print(
            pd.DataFrame(
                np.where(np.isfinite(distancia), distancia, "inf"),
                index=range(1, n + 1),
                columns=range(1, n + 1),
            )
        )
        print("Matriz de recorrido actualizada:")
        print(pd.DataFrame(recorrido, index=range(1, n + 1), columns=range(1, n + 1)))

    return matrices_distancias, matrices_recorrido


grafo = nx.DiGraph()

numero_nodos = int(input("Ingrese el numero de nodos: "))
nodos = list(range(1, numero_nodos + 1))
grafo.add_nodes_from(nodos)

numero_aristas = int(input("Ingrese el numero de aristas: "))
for _ in range(numero_aristas):
    datos = input("Ingrese los datos de la arista (origen-destino-peso): ").split("-")
    if len(datos) != 3:
        print("Entrada inválida. Por favor, ingrese los datos en el formato correcto.")
        continue
    origen, destino, peso = int(datos[0]), int(datos[1]), int(datos[2])
    direccion = int(
        input(
            "Si la arista es bidireccional ingrese 1, si no es bidireccional ingrese 2: "
        )
    )
    if direccion == 1:
        grafo.add_edge(origen, destino, weight=peso)
        grafo.add_edge(destino, origen, weight=peso)
    elif direccion == 2:
        grafo.add_edge(origen, destino, weight=peso)
    else:
        print("Entrada inválida. Por favor, ingrese 1 o 2.")

matrices_distancias, matrices_recorrido = floyd(grafo)

nodos = list(grafo.nodes())
matriz_distancias_final = matrices_distancias[-1]
matriz_distancias = pd.DataFrame(
    np.where(np.isfinite(matriz_distancias_final), matriz_distancias_final, "inf"),
    index=range(1, len(matriz_distancias_final) + 1),
    columns=range(1, len(matriz_distancias_final) + 1),
)
print("\nLa matriz de distancias final es: ")
print(matriz_distancias)

pos = nx.spring_layout(grafo)
nx.draw(grafo, pos, with_labels=True, font_weight="bold")
aristas = nx.get_edge_attributes(grafo, "weight")
nx.draw_networkx_edge_labels(grafo, pos, edge_labels=aristas)
plt.show()
