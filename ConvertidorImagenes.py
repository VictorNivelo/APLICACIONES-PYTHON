import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import os


class ConvertidorImagenes:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Convertidor de Imágenes PNG")
        self.ventana.geometry("600x400")
        self.ventana.configure(bg="#f0f0f0")
        self.rutas_imagenes = []
        self.modo = tk.StringVar(value="oscuro_a_claro")
        self.crear_elementos()

    def crear_elementos(self):
        frame_principal = ttk.Frame(self.ventana)
        frame_principal.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        ttk.Label(frame_principal, text="Modo de conversión:").pack(pady=5)
        ttk.Radiobutton(frame_principal, text="Oscuro a Claro", variable=self.modo, value="oscuro_a_claro").pack()
        ttk.Radiobutton(frame_principal, text="Claro a Oscuro", variable=self.modo, value="claro_a_oscuro").pack()
        self.boton_agregar = ttk.Button(frame_principal, text="Agregar Imágenes", command=self.agregar_imagenes)
        self.boton_agregar.pack(pady=10)
        frame_lista = ttk.Frame(frame_principal)
        frame_lista.pack(fill=tk.BOTH, expand=True, pady=10)
        self.lista_imagenes = tk.Listbox(frame_lista, width=60, height=10)
        scrollbar = ttk.Scrollbar(frame_lista, orient=tk.VERTICAL, command=self.lista_imagenes.yview)
        self.lista_imagenes.configure(yscrollcommand=scrollbar.set)
        self.lista_imagenes.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.boton_convertir = ttk.Button(frame_principal, text="Convertir Imágenes", command=self.convertir_imagenes)
        self.boton_convertir.pack(pady=10)

    def agregar_imagenes(self):
        archivos = filedialog.askopenfilenames(title="Seleccionar imágenes", filetypes=[("Archivos PNG", "*.png")])
        for archivo in archivos:
            if archivo not in self.rutas_imagenes:
                self.rutas_imagenes.append(archivo)
                self.lista_imagenes.insert(tk.END, os.path.basename(archivo))

    def ajustar_tamaño(self, imagen):
        if imagen.size != (512, 512):
            return imagen.resize((512, 512), Image.Resampling.LANCZOS)
        return imagen

    def procesar_nombre(self, nombre_base, modo):
        if nombre_base.endswith("_oscuro"):
            nombre_base = nombre_base[:-7]
        elif nombre_base.endswith("_claro"):
            nombre_base = nombre_base[:-6]
        if modo == "claro_a_oscuro":
            nombre_base += "_oscuro"
        return nombre_base

    def convertir_imagenes(self):
        if not self.rutas_imagenes:
            messagebox.showwarning("Advertencia", "No hay imágenes seleccionadas")
            return
        carpeta_salida = filedialog.askdirectory(title="Seleccionar carpeta destino")
        if not carpeta_salida:
            return
        for ruta_imagen in self.rutas_imagenes:
            try:
                img = Image.open(ruta_imagen)
                img = self.ajustar_tamaño(img)
                if img.mode != "RGBA":
                    img = img.convert("RGBA")
                datos = img.getdata()
                nuevos_datos = []
                nombre_base = os.path.splitext(os.path.basename(ruta_imagen))[0]
                if self.modo.get() == "oscuro_a_claro":
                    for pixel in datos:
                        if pixel[0] < 30 and pixel[1] < 30 and pixel[2] < 30:
                            nuevos_datos.append((255, 255, 255, pixel[3]))
                        else:
                            nuevos_datos.append(pixel)
                else:
                    for pixel in datos:
                        if pixel[0] > 225 and pixel[1] > 225 and pixel[2] > 225:
                            nuevos_datos.append((0, 0, 0, pixel[3]))
                        else:
                            nuevos_datos.append(pixel)
                nombre_base = self.procesar_nombre(nombre_base, self.modo.get())
                img.putdata(nuevos_datos)
                ruta_salida = os.path.join(carpeta_salida, f"{nombre_base}.png")
                img.save(ruta_salida, "PNG")
            except Exception as e:
                messagebox.showerror("Error", f"Error al procesar {os.path.basename(ruta_imagen)}: {str(e)}")
                continue
        messagebox.showinfo("Éxito", "Conversión completada")

    def ejecutar(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    app = ConvertidorImagenes()
    app.ejecutar()
