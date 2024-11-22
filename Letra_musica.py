import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pygame import mixer
import os
from mutagen.id3 import ID3, USLT
from mutagen.mp3 import MP3
import shutil
from pathlib import Path
import time
import threading


class ReproductorConLetra:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Reproductor de Música con Letras")
        self.root.geometry("1000x700")
        self.root.configure(bg="#f0f0f0")
        self.root.iconbitmap("music.ico") if os.path.exists("music.ico") else None
        mixer.init()
        self.reproduciendo = False
        self.cancion_actual = ""
        self.duracion = 0
        self.tiempo_actual = 0
        self.actualizando_tiempo = False
        self.crear_interfaz()
        self.configurar_estilos()

    def configurar_estilos(self):
        style = ttk.Style()
        style.configure("Custom.TFrame", background="#f0f0f0")
        style.configure("Custom.TButton", padding=6, font=("Arial", 10))
        style.configure("Title.TLabel", font=("Arial", 12, "bold"), background="#f0f0f0")
        style.configure("Info.TLabel", font=("Arial", 10), background="#f0f0f0")
        style.configure("Progreso.Horizontal.TProgressbar", thickness=8)

    def crear_interfaz(self):
        frame_principal = ttk.Frame(self.root, style="Custom.TFrame")
        frame_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        ttk.Label(frame_principal, text="Reproductor de Música con Letras", style="Title.TLabel").pack(pady=10)
        frame_botones = ttk.Frame(frame_principal, style="Custom.TFrame")
        frame_botones.pack(fill=tk.X, pady=10)
        ttk.Button(frame_botones, text="🎵 Seleccionar", command=self.seleccionar_musica, width=15).pack(
            side=tk.LEFT, padx=5
        )
        ttk.Button(frame_botones, text="💾 Guardar Letra", command=self.guardar_letra, width=15).pack(
            side=tk.LEFT, padx=5
        )
        ttk.Button(frame_botones, text="🗑️ Borrar Letra", command=self.eliminar_letra, width=15).pack(
            side=tk.LEFT, padx=5
        )
        frame_controles = ttk.Frame(frame_principal, style="Custom.TFrame")
        frame_controles.pack(fill=tk.X, pady=10)
        ttk.Button(frame_controles, text="⏮", command=self.reiniciar, width=3).pack(side=tk.LEFT, padx=2)
        self.btn_reproducir = ttk.Button(frame_controles, text="⏵", command=self.reproducir_pausar, width=3)
        self.btn_reproducir.pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_controles, text="⏹", command=self.detener, width=3).pack(side=tk.LEFT, padx=2)
        frame_progreso = ttk.Frame(frame_principal, style="Custom.TFrame")
        frame_progreso.pack(fill=tk.X, pady=5)
        self.tiempo_label = ttk.Label(frame_progreso, text="00:00 / 00:00", style="Info.TLabel")
        self.tiempo_label.pack(side=tk.RIGHT, padx=5)
        self.barra_progreso = ttk.Progressbar(
            frame_progreso, style="Progreso.Horizontal.TProgressbar", length=100, mode="determinate"
        )
        self.barra_progreso.pack(fill=tk.X, padx=5)
        frame_letra = ttk.LabelFrame(frame_principal, text="Letra de la canción", style="Custom.TFrame")
        frame_letra.pack(fill=tk.BOTH, expand=True, pady=10)
        self.texto_letra = tk.Text(frame_letra, wrap=tk.WORD, font=("Arial", 12), bg="white")
        scrollbar = ttk.Scrollbar(frame_letra, orient="vertical", command=self.texto_letra.yview)
        self.texto_letra.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.texto_letra.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.lbl_cancion = ttk.Label(frame_principal, text="No hay canción seleccionada", style="Info.TLabel")
        self.lbl_cancion.pack(pady=5)

    def actualizar_tiempo(self):
        while self.actualizando_tiempo:
            if self.reproduciendo:
                self.tiempo_actual = mixer.music.get_pos() // 1000
                self.barra_progreso["value"] = (self.tiempo_actual / self.duracion) * 100 if self.duracion else 0
                mins, secs = divmod(self.tiempo_actual, 60)
                mins_total, secs_total = divmod(self.duracion, 60)
                self.tiempo_label.config(text=f"{mins:02d}:{secs:02d} / {mins_total:02d}:{secs_total:02d}")
            time.sleep(0.1)

    def seleccionar_musica(self):
        if self.reproduciendo:
            self.detener()
        archivo = filedialog.askopenfilename(filetypes=[("Archivos MP3", "*.mp3")])
        if archivo:
            try:
                self.cancion_actual = archivo
                nombre_cancion = Path(archivo).name
                self.lbl_cancion.config(text=f"Canción: {nombre_cancion}")
                audio = MP3(archivo)
                self.duracion = int(audio.info.length)
                mixer.music.load(archivo)
                self.cargar_letra_mp3()
                if not self.actualizando_tiempo:
                    self.actualizando_tiempo = True
                    threading.Thread(target=self.actualizar_tiempo, daemon=True).start()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar la música: {str(e)}")

    def reproducir_pausar(self):
        if self.cancion_actual:
            if not self.reproduciendo:
                mixer.music.play(start=self.tiempo_actual)
                self.btn_reproducir.config(text="⏸")
            else:
                mixer.music.pause()
                self.btn_reproducir.config(text="⏵")
            self.reproduciendo = not self.reproduciendo

    def detener(self):
        if self.reproduciendo:
            mixer.music.stop()
            self.reproduciendo = False
            self.btn_reproducir.config(text="⏵")
            self.tiempo_actual = 0
            self.barra_progreso["value"] = 0
            self.tiempo_label.config(text=f"00:00 / {self.duracion//60:02d}:{self.duracion%60:02d}")

    def reiniciar(self):
        if self.cancion_actual:
            self.tiempo_actual = 0
            mixer.music.play()
            self.reproduciendo = True
            self.btn_reproducir.config(text="⏸")

    def guardar_letra(self):
        if not self.cancion_actual:
            messagebox.showerror("Error", "Seleccione una canción primero")
            return
        if self.reproduciendo:
            self.detener()
        letra = self.texto_letra.get("1.0", tk.END).strip()
        try:
            mixer.music.unload()
            temp_path = Path(os.path.expanduser("~")) / "temp_lyrics.mp3"
            shutil.copy2(self.cancion_actual, temp_path)
            audio = MP3(temp_path, ID3=ID3)
            if not audio.tags:
                audio.add_tags()
            audio.tags.add(USLT(encoding=3, lang="spa", desc="", text=letra))
            audio.save()
            shutil.copy2(temp_path, self.cancion_actual)
            messagebox.showinfo("Éxito", "Letra guardada correctamente")
            mixer.music.load(self.cancion_actual)
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar: {str(e)}")
        finally:
            if Path(temp_path).exists():
                try:
                    os.remove(temp_path)
                except:
                    pass

    def eliminar_letra(self):
        if not self.cancion_actual:
            messagebox.showerror("Error", "Seleccione una canción primero")
            return
        if messagebox.askyesno("Confirmar", "¿Desea eliminar la letra de esta canción?"):
            try:
                if self.reproduciendo:
                    self.detener()
                mixer.music.unload()
                audio = MP3(self.cancion_actual, ID3=ID3)
                if "USLT::spa" in audio.tags:
                    audio.tags.delall("USLT")
                    audio.save()
                    self.texto_letra.delete("1.0", tk.END)
                    messagebox.showinfo("Éxito", "Letra eliminada correctamente")
                mixer.music.load(self.cancion_actual)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar la letra: {str(e)}")

    def cargar_letra_mp3(self):
        self.texto_letra.delete("1.0", tk.END)
        try:
            audio = ID3(self.cancion_actual)
            if "USLT::spa" in audio:
                letra = audio["USLT::spa"].text
                self.texto_letra.insert("1.0", letra)
        except:
            pass

    def iniciar(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = ReproductorConLetra()
    app.iniciar()
