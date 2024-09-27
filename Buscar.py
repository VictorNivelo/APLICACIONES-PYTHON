# Diseño del algoritmo

# Algoritmo buscar(lista, elemento)
# Para i en rango(0, longitud(lista))    -- > n
# Si lista[i] es igual a elemento        -- > n
# Retornar i                             -- > 1
# Retornar -1                            -- > 1
# Fin del algoritmo
#                                       ------------
#                                       f(n) = N + (n-1) + 1 + 1
#                                       f(n) = 2n + 1
# Complejidad del algoritmo              | O(n)     |

# Algoritmo buscar(lista, elemento)


def buscar(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1


# Ejemplo de uso:
mi_lista = [1, 2, 3, 4, 5]
elemento_a_buscar = 3
resultado = buscar(mi_lista, elemento_a_buscar)
print("El elemento", elemento_a_buscar, "se encuentra en el índice:", resultado)
