import requests
from bs4 import BeautifulSoup
import os
import tkinter as tk
from tkinter import messagebox
import pygame
import subprocess

class Cancion:
    def __init__(self):
        self.vocal_path = None

    def obtener_letra(self, nombre_artista, nombre_cancion):
        artista = nombre_artista.replace(" ", "-").lower()
        cancion = nombre_cancion.replace(" ", "-").lower()
        url = f"https://www.letras.com/{artista}/{cancion}/"
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            sopa = BeautifulSoup(respuesta.text, 'html.parser')
            letras = sopa.find("div", class_="cnt-letra")
            if letras:
                return letras.get_text(separator="\n").strip()
        return "Letra no encontrada o acceso al sitio fallido."

    def separar_audio(self, archivo_entrada):
        if not os.path.exists(archivo_entrada):
            return "Archivo de audio no encontrado."
        comando = f"demucs --two-stems=vocals \"{archivo_entrada}\""
        subprocess.run(comando, shell=True)
        nombre_archivo = os.path.splitext(os.path.basename(archivo_entrada))[0]
        self.vocal_path = os.path.join("separated", "htdemucs", nombre_archivo, "vocals.wav")
        if not os.path.exists(self.vocal_path):
            return "Error al generar archivo de voz."
        return "Separación completada."

class Aplicacion:
    def __init__(self, root, cancion):
        self.cancion = cancion
        self.root = root
        self.root.title("Separador de Canciones y Letras")
        self.root.geometry("400x200")
        tk.Label(root, text="Artista:").pack()
        self.nombre_artista = tk.Entry(root)
        self.nombre_artista.pack()
        tk.Label(root, text="Canción:").pack()
        self.nombre_cancion = tk.Entry(root)
        self.nombre_cancion.pack()
        self.boton_letra = tk.Button(root, text="Mostrar Letra", command=self.mostrar_letra)
        self.boton_letra.pack(pady=5)
        self.boton_sonido = tk.Button(root, text="Reproducir Voz", command=self.reproducir_sonido)
        self.boton_sonido.pack(pady=5)
        pygame.mixer.init()

    def mostrar_letra(self):
        artista = self.nombre_artista.get().strip()
        cancion = self.nombre_cancion.get().strip()
        if not artista or not cancion:
            messagebox.showwarning("Campos vacíos", "Por favor ingresa el nombre del artista y la canción.")
            return
        letra = self.cancion.obtener_letra(artista, cancion)
        messagebox.showinfo("Letra de la Canción", letra)

    def reproducir_sonido(self):
        archivo_entrada = "C:/Users/Victor/Music/Musica\\200 Mph.mp3"
        estado_separacion = self.cancion.separar_audio(archivo_entrada)
        if "completada" in estado_separacion:
            pygame.mixer.music.load(self.cancion.vocal_path)
            pygame.mixer.music.play()
        else:
            messagebox.showerror("Error", estado_separacion)

root = tk.Tk()
cancion = Cancion()
app = Aplicacion(root, cancion)
root.mainloop()
