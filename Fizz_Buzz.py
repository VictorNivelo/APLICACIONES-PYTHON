# Programa que imprime fiz su es multiplo de 3, buzz si es multiplo de 5 y si es multiplo de 3 y 5 imprime FizzBuzz del 1 al 100


def FizzBuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


FizzBuzz()
