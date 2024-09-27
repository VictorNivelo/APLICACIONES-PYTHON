# Autor: Victor David Nivelo Yaguana

class Nodo:                                                                                  #1
    def __init__(self, valor):                                                               #1
        self.valor = valor                                                                   #1
        self.izquierda = None                                                                #1
        self.derecha = None                                                                  #1

def insertar(raiz, valor):                                                                   #n
    if raiz is None:                                                                         #1
        return Nodo(valor)                                                                   #1
    else:                                                                                    #1
        if valor < raiz.valor:                                                               #1
            raiz.izquierda = insertar(raiz.izquierda, valor)                                 #n
        else:                                                                                #1
            raiz.derecha = insertar(raiz.derecha, valor)                                     #n
        return raiz                                                                          #1

def imprimir_arbol(raiz, espacio="    "):                                                    #n
    if raiz is None:                                                                         #1
        return                                                                               #1
    nivel = 0                                                                                #1
    imprimir_subarbol(raiz, espacio, nivel)                                                  #n

def imprimir_subarbol(raiz, espacio, nivel):                                                 #n
    if raiz is not None:                                                                     #1
        imprimir_subarbol(raiz.derecha, espacio, nivel + 1)                                  #n
        print(espacio * nivel + str(raiz.valor))                                             #1
        imprimir_subarbol(raiz.izquierda, espacio, nivel + 1)                                #n

def recorrido_arbol(raiz):                                                                   #n
    if raiz is not None:                                                                     #1
        print(f"Recorrido del árbol a partir del nodo {raiz.valor}:")                        #1
        print("Recorrido en preorden:")                                                      #1
        recorrido_preorden(raiz)                                                             #n
        print("\nRecorrido en inorden:")                                                     #1
        recorrido_inorden(raiz)                                                              #n
        print("\nRecorrido en postorden:")                                                   #1
        recorrido_postorden(raiz)                                                            #n
        print()                                                                              #1

def recorrido_preorden(nodo):                                                                #n
    if nodo is not None:                                                                     #1
        print(nodo.valor, end=" ")                                                           #1
        recorrido_preorden(nodo.izquierda)                                                   #n
        recorrido_preorden(nodo.derecha)                                                     #n

def recorrido_inorden(nodo):                                                                 #n
    if nodo is not None:                                                                     #1
        recorrido_inorden(nodo.izquierda)                                                    #n
        print(nodo.valor, end=" ")                                                           #1
        recorrido_inorden(nodo.derecha)                                                      #n

def recorrido_postorden(nodo):                                                               #n
    if nodo is not None:                                                                     #1
        recorrido_postorden(nodo.izquierda)                                                  #n
        recorrido_postorden(nodo.derecha)                                                    #n
        print(nodo.valor, end=" ")                                                           #1

# Solicitar al usuario ingresar los valores del árbol
tamano_arbol = int(input("Ingrese el tamaño del árbol: "))                                   #1
valores = []                                                                                 #1
print("Ingrese los valores del árbol binario uno por uno.")                                  #1
for i in range(tamano_arbol):                                                                #n
    while True:                                                                              #1
        try:                                                                                 #1
            valor = int(input(f"Ingrese el valor para el nodo {i + 1}: "))                   #1
            valores.append(valor)                                                            #1
            break                                                                            #1
        except ValueError:                                                                   #1
            print("Por favor, ingrese un valor entero válido.")                              #1

# Crear el árbol con los valores ingresados por el usuario
raiz = None                                                                                  #1
for valor in valores:                                                                        #n
    raiz = insertar(raiz, valor)                                                             #n

# Imprimir el árbol de manera visual con niveles
print("\nÁrbol Binario:")                                                                    #1
imprimir_arbol(raiz)                                                                         #n

# Realizar el recorrido del árbol e imprimirlo visualmente
recorrido_arbol(raiz)                                                                        #n
                                                                                             #40 + 26n



# #Complejidad algoritmica

# # Autor: Victor David Nivelo Yaguana

# class Nodo:                                                                                   #tc

#     def __init__(self, valor):                                                                #tc
#         self.valor = valor                                                                    #tc
#         self.izquierda = None                                                                 #tc
#         self.derecha = None                                                                   #tc

# def insertar(raiz, valor):                                                                    #tc

#     if raiz is None:                                                                          #tc
#         return Nodo(valor)                                                                    #ta

#     else:                                                                                     #tc
#         if valor < raiz.valor:                                                                #tc
#             raiz.izquierda = insertar(raiz.izquierda, valor)                                  #to + to + to + ta
#         else:                                                                                 #tc
#             raiz.derecha = insertar(raiz.derecha, valor)                                      #to + to + to + ta
#         return raiz                                                                           #tc

# def imprimir_arbol(raiz, espacio="    "):                                                     #tc
#     if raiz is None:                                                                          #tc
#         return                                                                                #tc

#     nivel = 0                                                                                 #tc
#     imprimir_subarbol(raiz, espacio, nivel)                                                   #tc

# def imprimir_subarbol(raiz, espacio, nivel):                                                  #tc

#     if raiz is not None:                                                                      #tc
#         imprimir_subarbol(raiz.derecha, espacio, nivel + 1)                                   #to + to + to + ta
#         print(espacio * nivel + str(raiz.valor))                                              #tc
#         imprimir_subarbol(raiz.izquierda, espacio, nivel + 1)                                 #to + to + to + ta



# def recorrido_arbol(raiz):                                                                    #tc
#     if raiz is not None:                                                                      #tc
#         print(f"Recorrido del árbol a partir del nodo {raiz.valor}:")                         #tc
#         print("Recorrido en preorden:")                                                       #tc
#         recorrido_preorden(raiz)                                                              #tc
#         print("\nRecorrido en inorden:")                                                      #tc
#         recorrido_inorden(raiz)                                                               #tc
#         print("\nRecorrido en postorden:")                                                    #tc
#         recorrido_postorden(raiz)                                                             #tc
#         print()                                                                               #tc

# def recorrido_preorden(nodo):                                                                 #tc
#     if nodo is not None:                                                                      #tc
#         print(nodo.valor, end=" ")                                                            #tc
#         recorrido_preorden(nodo.izquierda)                                                    #to + to + to + ta
#         recorrido_preorden(nodo.derecha)                                                      #to + to + to + ta

# def recorrido_inorden(nodo):                                                                  #tc
#     if nodo is not None:                                                                      #tc
#         recorrido_inorden(nodo.izquierda)                                                     #to + to + to + ta
#         print(nodo.valor, end=" ")                                                            #tc
#         recorrido_inorden(nodo.derecha)                                                       #to + to + to + ta


# def recorrido_postorden(nodo):                                                                #tc
#     if nodo is not None:                                                                      #tc
#         recorrido_postorden(nodo.izquierda)                                                   #to + to + to + ta
#         recorrido_postorden(nodo.derecha)                                                     #to + to + to + ta
#         print(nodo.valor, end=" ")                                                            #tc

# # Solicitar al usuario ingresar los valores del árbol
# tamano_arbol = int(input("Ingrese el tamaño del árbol: "))                                    #to + ta + ta + to
# valores = []                                                                                  #tc
# print("Ingrese los valores del árbol binario uno por uno.")                                   #tc
# for i in range(tamano_arbol):                                                                 #to + to + to + to + to
#     while True:                                                                               #to
#         try:                                                                                  #to
#             valor = int(input(f"Ingrese el valor para el nodo {i + 1}: "))                    #to + to + to + to + to
#             valores.append(valor)                                                             #tc + to + to + ta
#             break                                                                             #to
        
#         except ValueError:                                                                    #to
#             print("Por favor, ingrese un valor entero válido.")                               #tc

# # Crear el árbol con los valores ingresados por el usuario
# raiz = None                                                                                   #tc

# for valor in valores:                                                                         #to + to + to + to + to + to
#     raiz = insertar(raiz, valor)                                                              #tc + to + to + ta

# # Imprimir el árbol de manera visual con niveles

# print("\nÁrbol Binario:")                                                                     #tc

# imprimir_arbol(raiz)                                                                          #tc

# # Realizar el recorrido del árbol e imprimirlo visualmente

# recorrido_arbol(raiz)                                                                         #tc + to + to + ta
#                                                                                               #52tc + 41 n to + 101ta