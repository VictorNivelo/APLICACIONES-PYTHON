import yt_dlp as youtube_dl
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import messagebox
import os


class DescargadorYoutube:
    def __init__(self, root):
        self.root = root
        self.root.title("Descargador de YouTube")
        self.root.geometry("600x400")
        self.crear_interfaz()

    def crear_interfaz(self):
        marco = ttk.Frame(self.root, padding="10")
        marco.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        ttk.Label(marco, text="URL del video:").grid(row=0, column=0, sticky=tk.W)
        self.url_entrada = ttk.Entry(marco, width=50)
        self.url_entrada.grid(row=0, column=1, columnspan=2, pady=5)
        ttk.Label(marco, text="Carpeta destino:").grid(row=1, column=0, sticky=tk.W)
        self.ruta_entrada = ttk.Entry(marco, width=40)
        self.ruta_entrada.grid(row=1, column=1, pady=5)
        ttk.Button(marco, text="Buscar", command=self.seleccionar_carpeta).grid(row=1, column=2)
        ttk.Label(marco, text="Calidad:").grid(row=2, column=0, sticky=tk.W)
        self.calidad = ttk.Combobox(marco, values=["Mejor calidad", "720p", "480p", "360p"], state="readonly")
        self.calidad.set("Mejor calidad")
        self.calidad.grid(row=2, column=1, pady=5)
        ttk.Label(marco, text="Formato:").grid(row=3, column=0, sticky=tk.W)
        self.formato = ttk.Combobox(marco, values=["mp4", "webm"], state="readonly")
        self.formato.set("mp4")
        self.formato.grid(row=3, column=1, pady=5)
        self.progreso = ttk.Progressbar(marco, length=400, mode="determinate")
        self.progreso.grid(row=4, column=0, columnspan=3, pady=10)
        ttk.Button(marco, text="Descargar", command=self.iniciar_descarga).grid(row=5, column=0, columnspan=3, pady=10)

    def seleccionar_carpeta(self):
        carpeta = filedialog.askdirectory()
        if carpeta:
            self.ruta_entrada.delete(0, tk.END)
            self.ruta_entrada.insert(0, carpeta)

    def iniciar_descarga(self):
        url = self.url_entrada.get().strip()
        carpeta = self.ruta_entrada.get().strip()
        if not url or not carpeta:
            messagebox.showerror("Error", "Por favor ingrese la URL y seleccione una carpeta")
            return
        calidad_seleccionada = self.calidad.get()
        formato_seleccionado = self.formato.get()
        formato_calidad = {
            "Mejor calidad": "best",
            "720p": "best[height<=720]",
            "480p": "best[height<=480]",
            "360p": "best[height<=360]",
        }
        ydl_opts = {
            "format": f"{formato_calidad[calidad_seleccionada]}[ext={formato_seleccionado}]",
            "outtmpl": os.path.join(carpeta, "%(title)s.%(ext)s"),
            "progress_hooks": [self.actualizar_progreso],
        }
        try:
            self.progreso["value"] = 0
            self.root.update_idletasks()
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            messagebox.showinfo("Éxito", "Descarga completada exitosamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error al descargar: {str(e)}")

    def actualizar_progreso(self, d):
        if d["status"] == "downloading":
            p = d.get("_percent_str", "0%")
            try:
                self.progreso["value"] = float(p.replace("%", ""))
                self.root.update_idletasks()
            except:
                pass


if __name__ == "__main__":
    root = tk.Tk()
    app = DescargadorYoutube(root)
    root.mainloop()
