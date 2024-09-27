# Algoritmo de dijkstra

# funcion dijkstra(Grafo g, int origen):
#     distancias = {nodo: infinito para cada nodo en grafo}
#     distancias[origen] = 0
#     rutas = {nodo: [] para cada nodo en grafo}
#     rutas[origen] = [origen]
#     cola = [(0, origen)]
#     mientras cola no este vacia:
#         distancia_actual, nodo_actual = extraer_minimo(cola)
#         si distancia_actual > distancias[nodo_actual], entonces:
#             continuar
#         fin_si
#         para cada vecino, peso en Grafo[nodo_actual], hacer:
#             distancia = distancia_actual + peso["weight"]
#             si distancia < distancias[vecino], entonces:
#                 distancias[vecino] = distancia
#                 rutas[vecino] = rutas[nodo_actual] + [vecino]
#                 agregar(cola, (distancia, vecino))
#             fin_si
#         fin_para
#     fin_mientras
#     devolver distancias, rutas


# Codigo en python

import heapq
import networkx as nx
import matplotlib.pyplot as plt


# Calculo de la complejidad

# def Dijkstra(Grafo, origen):                                      1
#     distancias = {nodo: float("inf") for nodo in Grafo.nodes()}   n(n - 1)
#     distancias[origen] = 0                                        n
#     rutas = {nodo: [] for nodo in Grafo.nodes()}                  n-1
#     rutas[origen] = [origen]                                      1
#     cola = [(0, origen)]                                          1
#     while cola:                                                   n
#         distancia_actual, nodo_actual = heapq.heappop(cola)       n(n - 1)
#         if distancia_actual > distancias[nodo_actual]:            n(n - 1)
#             continue                                              n(n - 1)
#         for vecino, peso in Grafo[nodo_actual].items():           n(n(n - 1) - 1)
#             distancia = distancia_actual + peso["weight"]         n(n(n - 1) - 1)
#             if distancia < distancias[vecino]:                    n(n(n - 1) - 1 )
#                 distancias[vecino] = distancia                    n(n(n - 1) - 1)
#                 rutas[vecino] = rutas[nodo_actual] + [vecino]     n(n(n - 1) - 1)
#                 heapq.heappush(cola, (distancia, vecino))         n(n(n - 1) - 1)
#     return distancias, rutas                                      1
#                                                                   ---------------------
#                                                                   6n3 + 4n2 + 3n + 4

# Grafo = nx.Graph()
# Grafo = Grafo.to_directed()
# Grafo.add_nodes_from([1, 2, 3, 4, 5])
# pos = {1: (0, 0), 2: (1.5, 1.5), 3: (2.5, 0), 4: (3.5, 1), 5: (4.5, 0)}
# nx.set_node_attributes(Grafo, pos, "pos")
# Grafo.add_weighted_edges_from(
#     [
#         (1, 2, 100),
#         (1, 3, 30),
#         (2, 3, 20),
#         (3, 4, 10),
#         (3, 5, 60),
#         (4, 2, 15),
#         (4, 5, 50),
#     ]
# )

# pos = nx.get_node_attributes(Grafo, "pos")
# nx.draw(
#     Grafo,
#     pos,
#     with_labels=True,
#     node_size=700,
#     node_color="lightblue",
#     font_weight="bold",
#     font_color="black",
#     font_size=10,
#     width=2,
#     edge_color="gray",
# )
# aristas = nx.get_edge_attributes(Grafo, "weight")
# nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=aristas)


# Codigo con representacion grafica


def Dijkstra(Grafo, origen):
    distancias = {nodo: float("inf") for nodo in Grafo.nodes()}
    distancias[origen] = 0
    rutas = {nodo: [] for nodo in Grafo.nodes()}
    rutas[origen] = [origen]
    cola = [(0, origen)]

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)
        if distancia_actual > distancias[nodo_actual]:
            continue
        for vecino, peso in Grafo[nodo_actual].items():
            distancia = distancia_actual + peso["weight"]
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                rutas[vecino] = rutas[nodo_actual] + [vecino]
                heapq.heappush(cola, (distancia, vecino))
    return distancias, rutas


Grafo = nx.DiGraph()
Grafo.add_nodes_from([1, 2, 3, 4, 5])
pos = {1: (0, 0), 2: (1.5, 1.5), 3: (2.5, 0), 4: (3.5, 1), 5: (4.5, 0)}
nx.set_node_attributes(Grafo, pos, "pos")
Grafo.add_weighted_edges_from(
    [
        (1, 2, 100),
        (1, 3, 30),
        (2, 3, 20),
        (3, 4, 10),
        (3, 5, 60),
        (4, 2, 15),
        (4, 5, 50),
    ]
)

origen = int(input("Ingrese el nodo de origen (1-5): "))

distancias, rutas = Dijkstra(Grafo, origen)

for destino in distancias:
    if destino != origen:
        print(
            f"Ruta más corta de {origen} a {destino}: {' -> '.join(map(str, rutas[destino]))} con una distancia de {distancias[destino]}"
        )

plt.figure(figsize=(10, 6))
pos = nx.get_node_attributes(Grafo, "pos")
nx.draw(
    Grafo,
    pos,
    with_labels=True,
    node_size=700,
    node_color="lightblue",
    font_weight="bold",
    font_color="black",
    font_size=10,
    width=2,
    edge_color="gray",
)
aristas = nx.get_edge_attributes(Grafo, "weight")
nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=aristas)

for destino in rutas:
    if destino != origen:
        path_edges = list(zip(rutas[destino], rutas[destino][1:]))
        nx.draw_networkx_edges(
            Grafo, pos, edgelist=path_edges, edge_color="red", width=2
        )

plt.title(f"Rutas más cortas desde la ciudad {origen}")
plt.show()
