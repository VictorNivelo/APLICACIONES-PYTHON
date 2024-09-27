import heapq
import networkx as nx
import matplotlib.pyplot as plt


def imprimir_estado(nodos, distancias, rutas, temporales):
    print(f"{'Nodo':<6} {'Etiqueta':<25} {'Estado':<10}")
    for nodo in nodos:
        if distancias[nodo] < float("inf"):
            estado = "Permanente"
            etiqueta = f"[{distancias[nodo]}," + "->".join(map(str, rutas[nodo])) + "]"
        else:
            estado = "Temporal"
            etiqueta = (
                f"[{distancias[nodo]}," + "->".join(map(str, temporales[nodo])) + "]"
            )
        print(f"{nodo:<6} {etiqueta:<25} {estado:<10}")
    print("\n" + "-" * 45 + "\n")


def Dijkstra(Grafo, origen):
    distancias = {nodo: float("inf") for nodo in Grafo.nodes()}
    distancias[origen] = 0
    rutas = {nodo: [] for nodo in Grafo.nodes()}
    rutas[origen] = [origen]
    cola = [(0, origen)]
    caminos_temporales = {nodo: [] for nodo in Grafo.nodes()}

    imprimir_estado(Grafo.nodes, distancias, rutas, caminos_temporales)

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
                caminos_temporales[vecino] = rutas[nodo_actual] + [vecino]
            else:
                caminos_temporales[vecino] = rutas[nodo_actual] + [vecino]

            print(
                f"Ruta: {' -> '.join(map(str, rutas[vecino]))} con una distancia de {distancias[vecino]}"
            )
            print(
                f"Ruta temporal: {' -> '.join(map(str, caminos_temporales[vecino]))} con una distancia de {distancia}"
            )

        imprimir_estado(Grafo.nodes, distancias, rutas, caminos_temporales)

    return distancias, rutas, caminos_temporales


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

while True:
    try:
        origen = int(input("Ingrese el nodo de origen (1-5): "))
        if origen in Grafo.nodes:
            break
        else:
            print("Por favor, ingrese un número válido entre 1 y 5.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")

distancias, rutas, caminos_temporales = Dijkstra(Grafo, origen)

for destino in distancias:
    if destino != origen:
        print(
            f"Ruta más corta de {origen} a {destino}: {' -> '.join(map(str, rutas[destino]))} con una distancia de {distancias[destino]}"
        )
        if caminos_temporales[destino]:
            print(
                f"Ruta temporal de {origen} a {destino}: {' -> '.join(map(str, caminos_temporales[destino]))}"
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
