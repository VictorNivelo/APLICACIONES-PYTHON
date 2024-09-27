# Diseño del algoritmo

# Función resta_matriz(matriz):
#     resultado = copiar(lista(matriz[0]))
#     Para cada fila en matriz[1:]:
#         Para cada i en rango(longitud(fila)):
#             resultado[i] -= fila[i]
#     Devolver resultado
# escribir("Ingrese el número de filas: ")
# filas = convertir_a_entero(leer())
# escribir("Ingrese el número de columnas: ")
# columnas = convertir_a_entero(leer())
# matriz = lista()
# Para i en rango(filas):
#     fila = lista()
#     Para j en rango(columnas):
#         elemento = convertir_a_entero(escribir("Ingrese el elemento en la posición (",i+1,", ",j+1,"): "))
#         añadir(elemento,fila)
#     añadir(fila,matriz)
# resultado = resta_matriz(matriz)
# escribir("La resta de los elementos de la matriz es: ", resultado)


# Complejidad del algoritmo

# def resta_matriz(matriz):
#     resultado = list(matriz[0])                                                       ---> 1
#     for fila in matriz[1:]:                                                           ---> n + 1
#         for i in range(len(fila)):                                                    ---> n * n + 1
#             resultado[i] -= fila[i]                                                   ---> n * n
#     return resultado
# filas = int(input("Ingrese el número de filas: "))
# columnas = int(input("Ingrese el número de columnas: "))
# matriz = []
# for i in range(filas):
#     fila = []                                                                         ---> n + 1
#     for j in range(columnas):                                                         ---> n
#         elemento = int(input(f"Ingrese el elemento en la posición ({i+1}, {j+1}): ")) ---> n * n + 1
#         fila.append(elemento)                                                         ---> n * n
#     matriz.append(fila)                                                               ---> n
# resultado = resta_matriz(matriz)                                                      ---> n
# print("La resta de los elementos de la matriz es:", resultado)                        ---> 1
#                                                                                       ---------------------
#                                                                                       f(n) = 5n2 + 4n + 9

# Codigo en Python


def resta_matriz(matriz):
    resultado = list(matriz[0])
    for fila in matriz[1:]:
        for i in range(len(fila)):
            resultado[i] -= fila[i]
    return resultado


filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        elemento = int(input(f"Ingrese el elemento en la posición ({i+1}, {j+1}): "))
        fila.append(elemento)
    matriz.append(fila)

resultado = resta_matriz(matriz)

print("La resta de los elementos de la matriz es:", resultado)
