#Diseño del algoritmo

# Funcion MultiplicarMatriz(matriz_A, matriz_B):
#     filas_A, columnas_A = longitud(matriz_A), longitud(matriz_A[0])
#     filas_B, columnas_B = longitud(matriz_B), longitud(matriz_B[0])
#     Si columnas_A != filas_B:
#         Lanzar Error("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz")
#     resultado = Matriz(filas_A, columnas_B)
#     Para i desde 0 hasta filas_A - 1:
#         Para j desde 0 hasta columnas_B - 1:
#             suma = 0
#             Para k desde 0 hasta columnas_A - 1:
#                 suma = suma + matriz_A[i][k] * matriz_B[k][j]
#             resultado[i][j] = suma
#     Retornar resultado
# Funcion IngresarMatriz(filas, columnas, mensaje):
#     Escribir mensaje
#     matriz = Matriz(filas, columnas)
#     Para i desde 0 hasta filas - 1:
#         Para j desde 0 hasta columnas - 1:
#             Escribir "Ingrese el elemento en la posición (", i+1, ", ", j+1, "): "
#             matriz[i][j] = LeerEntero()
#     Retornar matriz
# Escribir "Ingrese el número de filas de la primera matriz: "
# filas_A = LeerEntero()
# Escribir "Ingrese el número de columnas de la primera matriz: "
# columnas_A = LeerEntero()
# matriz_A = IngresarMatriz(filas_A, columnas_A, "Ingrese los elementos de la primera matriz:")
# Escribir "Ingrese el número de filas de la segunda matriz: "
# filas_B = LeerEntero()
# Escribir "Ingrese el número de columnas de la segunda matriz: "
# columnas_B = LeerEntero()
# matriz_B = IngresarMatriz(filas_B, columnas_B, "Ingrese los elementos de la segunda matriz:")
# Intentar:
#     resultado = MultiplicarMatriz(matriz_A, matriz_B)
#     Escribir "El resultado de la multiplicación de matrices es:"
#     Para cada fila en resultado:
#         Escribir fila
# Capturar Error como e:
#     Escribir "Error: ", e


#Complejidad del algoritmo

# def MultiplicarMatriz(matriz_A, matriz_B):
#     filas_A, columnas_A = len(matriz_A), len(matriz_A[0])                                                         1
#     filas_B, columnas_B = len(matriz_B), len(matriz_B[0])                                                         1
#     if columnas_A != filas_B:                                                                                     1
#         raise ValueError(
#             "El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz"
#         )

#     resultado = [
#         [
#             sum(matriz_A[i][k] * matriz_B[k][j] for k in range(columnas_A))                                       1*(n+1)*(n+1)*(n+1)
#             for j in range(columnas_B)
#         ]
#         for i in range(filas_A)
#     ]
#     return resultado                                                                                              1


# def IngresarMatriz(filas, columnas, mensaje):
#     print(mensaje)
#     matriz = [
#         [
#             int(input(f"Ingrese el elemento en la posición ({i+1}, {j+1}): "))                                    (n+1)*(n+1)
#             for j in range(columnas)
#         ]
#         for i in range(filas)                                                                                      1
#     ]
#     return matriz                                                                                                  1


# filas_A = int(input("Ingrese el número de filas de la primera matriz: "))                                          1
# columnas_A = int(input("Ingrese el número de columnas de la primera matriz: "))                                    1 
# matriz_A = IngresarMatriz(
#     filas_A, columnas_A, "Ingrese los elementos de la primera matriz:"                                             1
# )

# filas_B = int(input("Ingrese el número de filas de la segunda matriz: "))                                          1
# columnas_B = int(input("Ingrese el número de columnas de la segunda matriz: "))                                    1
# matriz_B = IngresarMatriz(
#     filas_B, columnas_B, "Ingrese los elementos de la segunda matriz:"                                             1
# )

# try:
#     resultado = MultiplicarMatriz(matriz_A, matriz_B)                                                              n 
#     print("El resultado de la multiplicación de matrices es:")
#     for fila in resultado:
#         print(fila)
# except ValueError as e:
#     print(f"Error: {e}")
#                                                                                                                   ---------------------
#                                                                                                                   f(n) = 3n3 + n2 + n + 15 


#Codigo en Python

def MultiplicarMatriz(matriz_A, matriz_B):
    filas_A, columnas_A = len(matriz_A), len(matriz_A[0])
    filas_B, columnas_B = len(matriz_B), len(matriz_B[0])
    if columnas_A != filas_B:
        raise ValueError(
            "El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz"
        )

    resultado = [
        [
            sum(matriz_A[i][k] * matriz_B[k][j] for k in range(columnas_A))
            for j in range(columnas_B)
        ]
        for i in range(filas_A)
    ]
    return resultado


def IngresarMatriz(filas, columnas, mensaje):
    print(mensaje)
    matriz = [
        [
            int(input(f"Ingrese el elemento en la posición ({i+1}, {j+1}): "))
            for j in range(columnas)
        ]
        for i in range(filas)
    ]
    return matriz


filas_A = int(input("Ingrese el número de filas de la primera matriz: "))
columnas_A = int(input("Ingrese el número de columnas de la primera matriz: "))
matriz_A = IngresarMatriz(
    filas_A, columnas_A, "Ingrese los elementos de la primera matriz:"
)

filas_B = int(input("Ingrese el número de filas de la segunda matriz: "))
columnas_B = int(input("Ingrese el número de columnas de la segunda matriz: "))
matriz_B = IngresarMatriz(
    filas_B, columnas_B, "Ingrese los elementos de la segunda matriz:"
)

try:
    resultado = MultiplicarMatriz(matriz_A, matriz_B)
    print("El resultado de la multiplicación de matrices es:")
    for fila in resultado:
        print(fila)
except ValueError as e:
    print(f"Error: {e}")
