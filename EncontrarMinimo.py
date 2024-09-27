#Autor: Victor David Nivelo Yaguana                                                                                                           
    
#Ejecucion para el t(n)              
 
def BuscarMinimo(arreglo):                                                                                                   #1
    if len(arreglo) == 0:                                                                                                    #1
        raise ValueError("La lista está vacía")                                                                              #1
    
    minimo = arreglo[0]                                                                                                      #1
    for i in range(1, len(arreglo)):                                                                                         #n
        if arreglo[i] < minimo:                                                                                              #n
            minimo = arreglo[i]                                                                                              #n
    return minimo                                                                                                            #1

if __name__ == "__main__":                                                                                                   #1
    try:                                                                                                                     #1
        # Solicita al usuario ingresar los elementos dentro de la lista                                                      
        arreglo = [int(x) for x in input("Ingrese los números de la lista separados por un '-': ").split('-')]               #n
        minimo = BuscarMinimo(arreglo)                                                                                       #1
        print(f"El valor mínimo dentro de esta lista es: {minimo}")                                                          #1
    except ValueError as e:                                                                                                  #1
        print(e)                                                                                                             #1
                                                                                                                             #11 + 4n //

# #Ejucucion en complejidad algoritmica

# def BuscarMinimo(arreglo):                                                                                                   
#     if len(arreglo) == 0:                                                                                                    #tc
#         raise ValueError("La lista está vacía")                                                                              #ta + to
    
#     minimo = arreglo[0]                                                                                                      #ta
#     for i in range(1, len(arreglo)):                                                                                         #to + to + ta + ta
#         if arreglo[i] < minimo:                                                                                              #tc + to + to
#             minimo = arreglo[i]                                                                                              #ta
#     return minimo                                                                                                            

# if __name__ == "__main__":                                                                                                   
#     try:                                                                                                                     
#         # Solicita al usuario ingresar los elementos dentro de la lista                                                      
#         arreglo = [int(x) for x in input("Ingrese los números de la lista separados por un '-': ").split('-')]               #to + ta + to + to + to + to + to + to + ta + ta
#         minimo = BuscarMinimo(arreglo)                                                                                       #ta + to + ta
#         print(f"El valor mínimo dentro de esta lista es: {minimo}")                                                          #to + ta + ta
#     except ValueError as e:                                                                                                  #Tiempo = 4ta + 7to + 3tc
#         print(e)  