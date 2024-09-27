# Algoritmo de potenciacion


def potencia(base, exponente):
    resultado = 1
    while exponente > 0:
        if exponente % 2 == 1:
            resultado *= base
        base *= base
        exponente //= 2
    return resultado


def main_potencia():
    while True:
        try:
            base = float(input("Ingrese la base: "))
            exponente = int(input("Ingrese el exponente (entero): "))
            break
        except ValueError as e:
            print(f"Error: {e}. Por favor, intente de nuevo.")

    resultado = potencia(base, exponente)
    print(f"{base} elevado a {exponente} es: {resultado}")


if __name__ == "__main__":
    main_potencia()
