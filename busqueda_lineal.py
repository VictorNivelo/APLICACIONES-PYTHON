import random


def busqueda_lineal(lista, objetivo):
    encontrado = False

    for elemento in lista:
        if elemento == objetivo:
            encontrado = True
            break
    return encontrado


if __name__ == "__main__":
    tamano_de_lista = int(input("De qué  tamaño será la lista?: "))
    objetivo = int(input("Qué número desea encontrar? :"))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    encontrado = busqueda_lineal(lista, objetivo)
    print(f'El elemento {objetivo}{" esá " if encontrado else " no está"} en la lista')
    print(lista)
