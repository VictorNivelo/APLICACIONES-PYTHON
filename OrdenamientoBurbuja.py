
#Algoritmo

#funcion OrdenamientoBurbuja(Lista)
#    n=longitud(lista)
#    para i de 0 a n-1 hacer
#        para j de 0 a n-i-1 hacer
#            si lista[j] > lista[j+1] entonces
#                intercambiar(lista[j], lista[j+1])
#            Fin si
#        Fin para
#    Fin para
#Fin funcion

def OrdenamientoBurbuja(Lista):
    n = len(Lista)
    for i in range(n-1):
        for j in range(n-i-1):
            if Lista[j] > Lista[j+1]:
                Lista[j], Lista[j+1] = Lista[j+1], Lista[j]
    
    print("La lista ordenada mediante el algoritmo de burbuja es:\n",Lista)
    

#Solicitar la lista de numeros al usuario
print("----- ORDENAMIENTO EN BURBUJA -----")
Entrada = input("Ingresar cada numero separado por un '-': ").split('-')
Datos = Entrada

Lista = [int(Valor) for Valor in Datos]
print("La lista ingresada por el usuario es: \n", Lista)
OrdenamientoBurbuja(Lista)


#Complejidad algoritmica

#def OrdenamientoBurbuja(Lista):                  
#    n = len(Lista)                                              1
#    for i in range(n-1):                                        n
#        for j in range(n-i-1):                                  n*(n-1)/2
#            if Lista[j] > Lista[j+1]:                           n*(n-1)/2
#                Lista[j], Lista[j+1] = Lista[j+1], Lista[j]     n*(n-1)/2
#                                                                ---------
#                                                                T(n) = 1+n+3(n(n-1)/2)
#                                                                T(n) = 1+n+0.5*3(n(n-1))
#                                                                T(n) = 1+n+0.5*3(n^2-n)
#                                                                T(n) = 1+n+1+n+1.5n^2-1.5n
#                                                                T(n) = 1.5n^2+0.5+1
