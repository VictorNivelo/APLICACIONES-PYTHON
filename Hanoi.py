# Algoritmo de Hanoi


def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return
    hanoi(n - 1, origen, auxiliar, destino)
    print(f"Mover disco {n} de {origen} a {destino}")
    hanoi(n - 1, auxiliar, destino, origen)


def main_hanoi():
    while True:
        try:
            n = int(input("Ingrese el número de discos: "))
            if n <= 0:
                raise ValueError("El número de discos debe ser un entero positivo.")
            break
        except ValueError as e:
            print(f"Error: {e}. Por favor, intente de nuevo.")

    hanoi(n, "A", "C", "B")


if __name__ == "__main__":
    main_hanoi()
