# Diseño del algortimo

# Función encontrar_minimo_usuario():
#     Escribir("Ingresa una lista de números separados por espacios: ")
#     entrada_usuario = Leer()
#     lista = ConvertirCadenaAListaDeEnteros(entrada_usuario)
#     Si longitud(lista) == 0:
#         Devolver Nulo
#     minimo = lista[0]
#     Para cada elemento en lista:
#         Si elemento < minimo:
#             minimo = elemento
#     Devolver minimo

# resultado = encontrar_minimo_usuario()
# Escribir("El valor mínimo es:", resultado)


# Complejidad del algoritmo

# def encontrar_minimo_usuario():
#     entrada_usuario = input("Ingresa una lista de numeros separados por espacios: ")      ---> 1
#     lista = [int(numero) for numero in entrada_usuario.split()]                           ---> n
#     if len(lista) == 0:                                                                   ---> 1
#         return None                                                                       ---> 1
#     minimo = lista[0]                                                                     ---> 1
#     for elemento in lista:                                                                ---> n + 1
#         if elemento < minimo:                                                             ---> n
#             minimo = elemento                                                             ---> n
#     return minimo                                                                         ---> 1

# resultado = encontrar_minimo_usuario()                                                    ---> 1
# print("El valor mínimo es:", resultado)                                                   ---> 1
#                                                                                           ---------------------
#                                                                                           f(n) = 4n + 8


# Codigo en Python


def encontrar_minimo_usuario():
    entrada_usuario = input("Ingresa una lista de numeros separados por espacios: ")
    lista = [int(numero) for numero in entrada_usuario.split()]
    if len(lista) == 0:
        return None
    minimo = lista[0]
    for elemento in lista:
        if elemento < minimo:
            minimo = elemento
    return minimo


resultado = encontrar_minimo_usuario()
print("El valor mínimo es:", resultado)
