import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

from tkinter import filedialog
import tkinter as tk
import threading
import pygame
import time


class ReproductorMP3:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Reproductor MP3")
        self.root.geometry("400x200")
        pygame.mixer.init()
        self.reproduciendo = False
        self.tiempo_reproduccion_actual = 0
        self.tiempo_total_acumulado = 0
        self.tiempo_pausa = 0
        self.ultima_pausa = 0
        self.ruta_archivo = None
        self.crear_interfaz()

    def crear_interfaz(self):
        tk.Button(self.root, text="Seleccionar MP3", command=self.seleccionar_cancion).pack(pady=10)
        self.lbl_nombre = tk.Label(self.root, text="No hay archivo seleccionado")
        self.lbl_nombre.pack(pady=5)
        self.lbl_tiempo = tk.Label(self.root, text="Tiempo: 00:00")
        self.lbl_tiempo.pack(pady=5)
        frame_controles = tk.Frame(self.root)
        frame_controles.pack(pady=10)
        tk.Button(frame_controles, text="▶", command=self.reproducir).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_controles, text="⏸", command=self.pausa).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_controles, text="⏹", command=self.detener).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_controles, text="↺", command=self.reiniciar).pack(side=tk.LEFT, padx=5)

    def seleccionar_cancion(self):
        self.ruta_archivo = filedialog.askopenfilename(
            title="Selecciona un archivo MP3", filetypes=[("Archivos MP3", "*.mp3")]
        )
        if self.ruta_archivo:
            nombre_archivo = os.path.basename(self.ruta_archivo)
            self.lbl_nombre.config(text=f"Archivo: {nombre_archivo}")
            self.detener()

    def actualizar_tiempo(self):
        while self.reproduciendo:
            if pygame.mixer.music.get_busy():
                tiempo_actual = pygame.mixer.music.get_pos() / 1000
                self.tiempo_reproduccion_actual = tiempo_actual + self.tiempo_pausa
                minutos = int(self.tiempo_reproduccion_actual // 60)
                segundos = int(self.tiempo_reproduccion_actual % 60)
                milisegundos = int((self.tiempo_reproduccion_actual % 1) * 1000)
                self.lbl_tiempo.config(
                    text=f"Tiempo: {minutos:02d}:{segundos:02d}.{milisegundos:03d}"
                )
            time.sleep(0.01)

    def reproducir(self):
        if self.ruta_archivo:
            if not self.reproduciendo:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.load(self.ruta_archivo)
                    pygame.mixer.music.play(start=self.tiempo_pausa)
                self.reproduciendo = True
                threading.Thread(target=self.actualizar_tiempo, daemon=True).start()

    def pausa(self):
        if self.reproduciendo:
            pygame.mixer.music.pause()
            self.reproduciendo = False
            tiempo_actual = self.tiempo_reproduccion_actual
            minutos = int(tiempo_actual // 60)
            segundos = int(tiempo_actual % 60)
            milisegundos = int((tiempo_actual % 1) * 1000)
            print(f"\nCanción pausada en: {minutos:02d}:{segundos:02d}.{milisegundos:03d}")
            if tiempo_actual > self.ultima_pausa:
                self.tiempo_total_acumulado += tiempo_actual - self.ultima_pausa
            self.ultima_pausa = tiempo_actual
            self.tiempo_pausa = tiempo_actual
            minutos_total = int(self.tiempo_total_acumulado // 60)
            segundos_total = int(self.tiempo_total_acumulado % 60)
            milisegundos_total = int((self.tiempo_total_acumulado % 1) * 1000)
            print(
                f"Tiempo total acumulado: {minutos_total:02d}:{segundos_total:02d}.{milisegundos_total:03d}"
            )
            self.lbl_tiempo.config(text=f"Tiempo: {minutos:02d}:{segundos:02d}.{milisegundos:03d}")

    def detener(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        self.reproduciendo = False
        tiempo_actual = self.tiempo_reproduccion_actual
        minutos = int(tiempo_actual // 60)
        segundos = int(tiempo_actual % 60)
        milisegundos = int((tiempo_actual % 1) * 1000)
        print(f"\nCanción detenida en: {minutos:02d}:{segundos:02d}.{milisegundos:03d}")
        if tiempo_actual > self.ultima_pausa:
            self.tiempo_total_acumulado += tiempo_actual - self.ultima_pausa
        minutos_total = int(self.tiempo_total_acumulado // 60)
        segundos_total = int(self.tiempo_total_acumulado % 60)
        milisegundos_total = int((self.tiempo_total_acumulado % 1) * 1000)
        print(
            f"Tiempo total acumulado: {minutos_total:02d}:{segundos_total:02d}.{milisegundos_total:03d}"
        )
        self.tiempo_reproduccion_actual = 0
        self.tiempo_pausa = 0
        self.ultima_pausa = 0
        self.lbl_tiempo.config(text="Tiempo: 00:00.000")

    def reiniciar(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        self.reproduciendo = False
        print("\nReproductor reiniciado")
        print("Tiempo total acumulado: 00:00")
        self.tiempo_reproduccion_actual = 0
        self.tiempo_total_acumulado = 0
        self.tiempo_pausa = 0
        self.ultima_pausa = 0
        self.lbl_tiempo.config(text="Tiempo: 00:00")

    def iniciar(self):
        self.root.mainloop()


if __name__ == "__main__":
    reproductor = ReproductorMP3()
    reproductor.iniciar()
