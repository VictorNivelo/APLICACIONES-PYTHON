import numpy as np
import matplotlib.pyplot as plt


def euler_method(f, t0, y0, t_end, step_size):
    """
    Método de Euler para resolver EDOs.

    :param f: Función que define la EDO, f(t, y)
    :param t0: Tiempo inicial
    :param y0: Valor inicial de y
    :param t_end: Tiempo final
    :param step_size: Tamaño del paso
    :return: Arrays de t y y con las soluciones aproximadas
    """
    t_values = np.arange(t0, t_end, step_size)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0

    for i in range(1, len(t_values)):
        y_values[i] = y_values[i - 1] + step_size * f(t_values[i - 1], y_values[i - 1])

    return t_values, y_values


# Ejemplo de uso
if __name__ == "__main__":
    # Definimos la EDO: dy/dt = -2 * y
    def f(t, y):
        return -2 * y

    t0 = 0  # Tiempo inicial
    y0 = 1  # Valor inicial de y
    t_end = 5  # Tiempo final
    step_size = 0.1  # Tamaño del paso

    t_values, y_values = euler_method(f, t0, y0, t_end, step_size)

    # Graficar la solución
    plt.plot(t_values, y_values, label="Aproximación por Euler")
    plt.xlabel("t")
    plt.ylabel("y")
    plt.title("Método de Euler")
    plt.legend()
    plt.grid(True)
    plt.show()
