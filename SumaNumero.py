# Diseño del algoritmo

# Algoritmo BuscarParesQueSuman(lista, k)
#     pares ← lista vacía                                       # -> 1
#     para i desde 0 hasta longitud(lista) - 1 hacer            # -> n
#         para j desde i + 1 hasta longitud(lista) - 1 hacer    # -> n * (n-1)
#             si lista[i] + lista[j] = k entonces               # -> n * (n-1)
#                 agregar (lista[i], lista[j]) a pares          # -> n * (n-1)
#             fin si
#         fin para
#     fin para
#     retornar pares                                            # -> 1
# Fin Algoritmo
#                                                               ---------------------
#                                                               f(n) = 3n2 + 2n + 1


# Codigo en Python


def buscarParesQueSuman(lista, k):
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == k:
                pares.append((lista[i], lista[j]))
    return pares


lista = list(
    map(int, input("Ingrese una lista de números separados por espacios: ").split())
)
k = int(input("Ingrese el número k para buscar pares que sumen a k: "))

pares = buscarParesQueSuman(lista, k)
print("Los pares que suman a", k, "son:", pares)
