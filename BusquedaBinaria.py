# Diseño del algoritmo

# Algoritmo OrdenamientoBurbuja(lista)
#     n ← longitud(lista)                               # -> 1
#     para i desde 0 hasta n - 1 hacer                  # -> n
#         para j desde 0 hasta n - i - 1 hacer          # -> n * (n-1)
#             si lista[j] > lista[j + 1] entonces       # -> n * (n-1)
#                 intercambiar lista[j] y lista[j + 1]  # -> n * (n-1)
#             fin si
#         fin para
#     fin para
#     retornar lista                                    # -> 1
# Fin Algoritmo
#                                                      ---------------------
#                                                      f(n) = 3n2 + 2n + 1


# Codigo en Python


def ordenamientoBurbuja(lista):
    n = len(lista)  #
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


lista = list(
    map(int, input("Ingrese una lista de números separados por espacios: ").split())
)

lista_ordenada = ordenamientoBurbuja(lista)
print("La lista ordenada es:", lista_ordenada)
