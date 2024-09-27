# Diseño del algoritmo

# Funcion Fibonacci(n):
#     fib_sequence = [0, 1]  // Inicializar la secuencia de Fibonacci con los dos primeros números
#     Para i desde 2 hasta n:
#         nuevo_valor = fib_sequence[i-1] + fib_sequence[i-2]  // Calcular el siguiente número de Fibonacci
#         Añadir nuevo_valor a fib_sequence  // Agregar el nuevo valor a la secuencia
#     Retornar fib_sequence
# // Leer el número del usuario
# Escribir "Ingrese un número para calcular la secuencia de Fibonacci: "
# numeroEjemplo = LeerEntero()
# // Calcular la secuencia de Fibonacci
# secuencia = Fibonacci(numeroEjemplo)
# // Imprimir la secuencia de Fibonacci
# Escribir "La secuencia de Fibonacci de ", numeroEjemplo, " es: ", secuencia


# Complejidad del algoritmo

# def Fibonnaci(n):
#     fib_sequence = [0, 1]                                                                     1
#     for i in range(2, n+1):                                                                   2^(n+1)
#         fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])                            n
#     return fib_sequence                                                                       n
# numeroEjemplo = int(input("Ingrese un número para calcular la secuencia de Fibonacci: "))     1
# secuencia = Fibonnaci(numeroEjemplo)                                                          1
# print("La secuencia de Fibonacci de", numeroEjemplo, "es:", secuencia)
#                                                                                               ---------------------
#                                                                                               f(n) =2^(n+1) + 2n + 3

# Codigo en Python


def Fibonnaci(n):
    fib_sequence = [0, 1]

    for i in range(2, n + 1):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

    return fib_sequence


numeroEjemplo = int(
    input("Ingrese un número para calcular la secuencia de Fibonacci: ")
)

secuencia = Fibonnaci(numeroEjemplo)

print("La secuencia de Fibonacci de", numeroEjemplo, "es:", secuencia)
