from matplotlib import pyplot as plt
from matplotlib.patches import FancyBboxPatch, ArrowStyle

# Create a figure and axis
fig, ax = plt.subplots(figsize=(15, 10))


# Helper function to draw arrows
def draw_arrow(ax, start, end, text="", color="black"):
    ax.annotate(
        text,
        xy=start,
        xytext=end,
        arrowprops=dict(facecolor=color, edgecolor=color, arrowstyle="->"),
        ha="center",
        va="center",
        fontsize=10,
    )


# Draw lifelines
x_positions = [1, 3, 5, 7]
labels = ["Usuario", "Interfaz Modificar", "Control Tarea", "Base de Datos"]

for x, label in zip(x_positions, labels):
    ax.text(
        x,
        9.5,
        label,
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgrey"),
    )
    ax.plot([x, x], [0, 9], "k--")

# Define interactions (start point, end point, label, color)
interactions = [
    ((1, 8.5), (3, 8.5), "Selecciona actualizar tarea", "black"),
    ((3, 8), (1, 8), "Muestra formulario\ncon información actual", "black"),
    ((1, 7.5), (3, 7.5), "Modifica información\nde tarea", "black"),
    ((3, 7), (5, 7), "Envía datos modificados\npara validación", "black"),
    ((5, 6.5), (7, 6.5), "Solicita validación", "black"),
    ((7, 6), (5, 6), "Datos validados", "black"),
    ((5, 5.5), (3, 5.5), "Datos validados", "black"),
    ((3, 4.5), (1, 4.5), "Error en validación", "red"),
    ((1, 4), (3, 4), "Corrige datos", "red"),
    ((3, 3.5), (5, 3.5), "Reenvía datos\nmodificados para validación", "red"),
    ((5, 3), (7, 3), "Solicita validación", "red"),
    ((7, 2.5), (5, 2.5), "Datos validados", "red"),
    ((5, 2), (3, 2), "Datos validados", "red"),
    ((3, 1.5), (1, 1.5), "Confirma validación\nexitosa", "black"),
    ((1, 1), (3, 1), "Guarda cambios", "black"),
    ((3, 0.5), (5, 0.5), "Solicita actualización", "black"),
    ((5, 0), (7, 0), "Actualiza datos\nen la base de datos", "black"),
    ((7, -0.5), (5, -0.5), "Confirmación de actualización", "black"),
    ((5, -1), (3, -1), "Confirmación de actualización", "black"),
    ((3, -1.5), (1, -1.5), "Confirmación\nexitosa", "black"),
]

# Draw interactions
for interaction in interactions:
    draw_arrow(ax, interaction[0], interaction[1], interaction[2], interaction[3])

# Set limits and hide axes
ax.set_xlim(0, 8)
ax.set_ylim(-2, 10)
ax.axis("off")

# Show the diagram
plt.show()
