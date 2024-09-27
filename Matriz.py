#Autor: Victor David Nivelo Yaguana

def obtener_matriz(filas, columnas):                                                                              #1
    matriz = []                                                                                                   #1
    for i in range(filas):                                                                                        #n
        fila = []                                                                                                 #n
        for j in range(columnas):                                                                                 #n*m
            while True:                                                                                           #n*m
                try:                                                                                              #n*m
                    valor = int(input(f"Ingrese el valor en la posición: ({i + 1}, {j + 1}): "))                  #n*m
                    fila.append(valor)                                                                            #n*m
                    break                                                                                         #n*m
                except ValueError:                                                                                #n*m
                    print("Ingrese un valor numérico válido.")                                                    #n*m
        matriz.append(fila)                                                                                       #n
    return matriz                                                                                                 #1

def suma_matrices(matriz1, matriz2):                                                                              #
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):                                        #
        raise ValueError("Las matrices deben tener las mismas dimensiones.")                                      #
    resultado = [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]    #
    return resultado                                                                                              #

try:                                                                                                              #
    filas = int(input("Ingrese el número de filas de las matrices: "))                                            #
    columnas = int(input("Ingrese el número de columnas de las matrices: "))                                      #

    print("Ingrese los valores para la matriz A:")                                                                #
    matriz_a = obtener_matriz(filas, columnas)                                                                    #

    print("Ingrese los valores para la matriz B:")                                                                #
    matriz_b = obtener_matriz(filas, columnas)                                                                    #

    resultado_suma = suma_matrices(matriz_a, matriz_b)                                                            #

    print("Matriz Resultado:")                                                                                    #
    for fila in resultado_suma:                                                                                   #
        print(fila)                                                                                               #

except ValueError as e:                                                                                           #
    print(f"Error: {e}")                                                                                          #
