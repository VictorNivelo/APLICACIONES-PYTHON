# Diseño del algoritmo

# def encontrarMaximoMinimo(lista):
#    maximo = lista[0]              -- > 1
#    minimo = lista[0]              -- > 1
#    for i in range(1, len(lista)): -- > n
#        if lista[i] > maximo:      -- > n - 1
#            maximo = lista[i]      -- > n*n - 1
#        if lista[i] < minimo:      -- > n*n - 1
#            minimo = lista[i]      -- > n - 1
#    return maximo, minimo
#                                   ------------
#                                    f(n) = 6n2 + 2n +2(n - 1)
#                                    f(n) = 2 + n + 4n - 4
#                                    f(n) = 6n2 + 2n + 2
#                                    f(n) = 0(n)


def encontrarMaximoMinimo(lista):
    maximo = lista[0]
    minimo = lista[0]

    for elemento in lista:
        if elemento > maximo:
            maximo = elemento
        if elemento < minimo:
            minimo = elemento

    return maximo, minimo


lista = []
tamanio = int(input("Ingrese el tamaño de la lista: "))

print("Ingrese los elementos de la lista:")
for i in range(tamanio):
    elemento = int(input("Elemento {}: ".format(i + 1)))
    lista.append(elemento)

maximo, minimo = encontrarMaximoMinimo(lista)

print("El valor Máximo de la lista es:", maximo)
print("El valor Mínimo de la lista es:", minimo)
