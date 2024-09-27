from matplotlib import pyplot as plt
import matplotlib.patches as patches

# Configurar el tamaño de la figura
fig, ax = plt.subplots(figsize=(12, 18))

# Configurar los ejes
ax.set_xlim(0, 10)
ax.set_ylim(0, 100)
ax.axis("off")

# Dibujar las líneas de vida
lineas_vida = [
    ("Actor", 1),
    ("UI CAJERO", 3),
    ("Control CAJERO", 5),
    ("SISTEMA BANCO", 7),
    ("CUENTA", 9),
]
for name, x in lineas_vida:
    ax.plot([x, x], [10, 90], color="black")
    ax.text(
        x,
        95,
        name,
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white"),
    )

# Dibujar las acciones
acciones = [
    ("Insertar tarjeta", 1, 3, 90),
    ("Leer código de banda", 3, 5, 85),
    ("Verificar código de banda", 5, 7, 80),
    ("Solicitar código", 5, 3, 75),
    ("Ingresar código", 3, 1, 70),
    ("Verificar código", 3, 5, 65),
    ("Seleccionar transacción", 3, 1, 60),
    ("Solicitar cantidad", 5, 3, 55),
    ("Ingresar cantidad", 3, 1, 50),
    ("Enviar petición", 5, 7, 45),
    ("Verificar fondos", 7, 9, 40),
    ("Respuesta", 9, 7, 35),
    ("Expulsar tarjeta", 5, 3, 30),
    ("Imprimir recibo", 5, 3, 25),
    ("Entregar dinero", 5, 3, 20),
]

for accion, x1, x2, y in acciones:
    ax.annotate(
        accion,
        xy=(x1, y),
        xytext=(x2, y),
        arrowprops=dict(facecolor="black", shrink=0.05),
        ha="center",
        va="center",
        fontsize=10,
    )

# Dibujar los bucles y alternativas
bucles = [
    (1, 75, 3, 70, "Intentos <= 3"),
    (5, 55, 7, 50, "Código correcto"),
    (5, 45, 7, 40, "Transacción autorizada"),
]

for x1, y1, x2, y2, text in bucles:
    ax.plot([x1, x1, x2, x2], [y1, y2, y2, y1], color="red", linestyle="dashed")
    ax.text(
        (x1 + x2) / 2,
        y2 - 2,
        text,
        ha="center",
        va="center",
        fontsize=10,
        bbox=dict(boxstyle="round,pad=0.3", edgecolor="red", facecolor="white"),
    )

# Excepciones y cancelaciones
excepciones = [
    ("Tarjeta no aceptada", 5, 3, 85, "Emitir sonido y expulsar tarjeta"),
    ("Código incorrecto (1,2)", 3, 1, 65, "Reintentar"),
    ("Código incorrecto (3)", 3, 1, 65, "Retener tarjeta"),
    ("No autorizado", 7, 5, 40, "Expulsar tarjeta"),
]

for exc, x1, x2, y, action in excepciones:
    ax.annotate(
        exc,
        xy=(x1, y),
        xytext=(x2, y - 5),
        arrowprops=dict(facecolor="blue", shrink=0.05),
        ha="center",
        va="center",
        fontsize=10,
        color="blue",
    )
    ax.text(
        x2,
        y - 7,
        action,
        ha="center",
        va="center",
        fontsize=10,
        bbox=dict(boxstyle="round,pad=0.3", edgecolor="blue", facecolor="white"),
    )

# Mostrar el diagrama
plt.gca().invert_yaxis()
plt.show()
