import tkinter as tk
from PIL import Image, ImageTk


def resize_image(image, width, height):
    return image.resize((width, height))


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz con Imagen y Botón")

# Cargar la imagen y redimensionarla
imagen_original = Image.open("Escenario.png")
imagen_redimensionada = resize_image(imagen_original, 500, 500)
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

# Crear un botón con la imagen
boton_imagen = tk.Button(ventana, image=imagen_tk, width=100, height=100)
boton_imagen.pack()


# Función para cambiar el tamaño del botón
def resize_button():
    boton_imagen.config(width=700, height=700)


# Crear un botón para cambiar el tamaño del botón
boton_cambio_tamano = tk.Button(
    ventana, text="Cambiar Tamaño del Botón", command=resize_button
)
boton_cambio_tamano.pack()

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
