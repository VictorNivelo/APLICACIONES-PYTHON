import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.wave import WAVE
from mutagen.id3 import ID3, APIC
import os
import datetime


def cargar_metadatos(archivo):
    extension = archivo.split(".")[-1].lower()
    if extension == "mp3":
        return MP3(archivo, ID3=EasyID3)
    elif extension == "flac":
        return FLAC(archivo)
    elif extension == "wav":
        return WAVE(archivo)
    else:
        raise ValueError("Formato no compatible. Solo se admiten MP3, FLAC y WAV.")


def cargar_caratula(archivo):
    if archivo.endswith(".mp3"):
        audio = MP3(archivo, ID3=ID3)
        for tag in audio.tags.values():
            if isinstance(tag, APIC):
                return tag.data
    return None


def mostrar_metadatos(metadatos):
    archivo = archivo_var.get()
    titulo_var.set(metadatos.get("title", [""])[0] if "title" in metadatos else "")
    artista_var.set(metadatos.get("artist", [""])[0] if "artist" in metadatos else "")
    album_var.set(metadatos.get("album", [""])[0] if "album" in metadatos else "")
    ano_var.set(metadatos.get("date", [""])[0] if "date" in metadatos else "")
    genero_var.set(metadatos.get("genre", [""])[0] if "genre" in metadatos else "")
    pista_var.set(metadatos.get("tracknumber", [""])[0] if "tracknumber" in metadatos else "")
    descripcion_var.set(metadatos.get("comment", [""])[0] if "comment" in metadatos else "")
    compositor_var.set(metadatos.get("composer", [""])[0] if "composer" in metadatos else "")
    arreglista_var.set(metadatos.get("arranger", [""])[0] if "arranger" in metadatos else "")
    productor_var.set(metadatos.get("producer", [""])[0] if "producer" in metadatos else "")
    interprete_var.set(metadatos.get("performer", [""])[0] if "performer" in metadatos else "")
    bit_rate_var.set(
        metadatos.info.bitrate // 1000 if hasattr(metadatos, "info") and hasattr(metadatos.info, "bitrate") else ""
    )
    codec_var.set(metadatos.mime if hasattr(metadatos, "mime") else "")
    duracion_var.set(str(datetime.timedelta(seconds=int(metadatos.info.length))) if hasattr(metadatos, "info") else "")
    tamano_var.set(os.path.getsize(archivo) // 1024 if archivo else "")
    frecuencia_var.set(
        metadatos.info.sample_rate if hasattr(metadatos, "info") and hasattr(metadatos.info, "sample_rate") else ""
    )
    num_disco_var.set(metadatos.get("discnumber", [""])[0] if "discnumber" in metadatos else "")
    fecha_creacion_var.set(datetime.datetime.fromtimestamp(os.path.getctime(archivo)).strftime("%Y-%m-%d %H:%M:%S"))
    fecha_modificacion_var.set(datetime.datetime.fromtimestamp(os.path.getmtime(archivo)).strftime("%Y-%m-%d %H:%M:%S"))


def mostrar_caratula(archivo):
    caratula_data = cargar_caratula(archivo)
    if caratula_data:
        with open("temp_caratula.jpg", "wb") as f:
            f.write(caratula_data)
        img = Image.open("temp_caratula.jpg")
        img.thumbnail((150, 150))
        img = ImageTk.PhotoImage(img)
        caratula_label.config(image=img)
        caratula_label.image = img
    else:
        caratula_label.config(image="", text="Sin carátula")


def modificar_metadatos():
    archivo = archivo_var.get()
    if not archivo:
        messagebox.showerror("Error", "Selecciona un archivo primero.")
        return
    try:
        metadatos = cargar_metadatos(archivo)
        if titulo_var.get():
            metadatos["title"] = titulo_var.get()
        if artista_var.get():
            metadatos["artist"] = artista_var.get()
        if album_var.get():
            metadatos["album"] = album_var.get()
        if ano_var.get():
            metadatos["date"] = ano_var.get()
        if genero_var.get():
            metadatos["genre"] = genero_var.get()
        if pista_var.get():
            metadatos["tracknumber"] = pista_var.get()
        if descripcion_var.get():
            metadatos["comment"] = descripcion_var.get()
        if compositor_var.get():
            metadatos["composer"] = compositor_var.get()
        if arreglista_var.get():
            metadatos["arranger"] = arreglista_var.get()
        if productor_var.get():
            metadatos["producer"] = productor_var.get()
        if interprete_var.get():
            metadatos["performer"] = interprete_var.get()
        if caratula_var.get():
            with open(caratula_var.get(), "rb") as f:
                caratula = f.read()
            if isinstance(metadatos, MP3):
                metadatos.tags.add(APIC(mime="image/jpeg", type=3, desc="Cover", data=caratula))
        metadatos.save()
        messagebox.showinfo("Éxito", "Metadatos modificados y guardados correctamente.")
        mostrar_caratula(archivo)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo modificar: {e}")


def seleccionar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de audio", "*.mp3 *.flac *.wav")])
    archivo_var.set(archivo)
    if archivo:
        try:
            metadatos = cargar_metadatos(archivo)
            mostrar_metadatos(metadatos)
            mostrar_caratula(archivo)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar metadatos: {e}")


def seleccionar_caratula():
    caratula = filedialog.askopenfilename(filetypes=[("Imágenes", "*.jpg *.jpeg *.png")])
    caratula_var.set(caratula)
    if caratula:
        img = Image.open(caratula)
        img.thumbnail((150, 150))
        img = ImageTk.PhotoImage(img)
        caratula_label.config(image=img)
        caratula_label.image = img


ventana = tk.Tk()
ventana.title("Editor de Metadatos de Audio")
ventana.geometry("600x600")
ventana.config(bg="#f0f0f0")

archivo_var = tk.StringVar()
titulo_var = tk.StringVar()
artista_var = tk.StringVar()
album_var = tk.StringVar()
ano_var = tk.StringVar()
genero_var = tk.StringVar()
pista_var = tk.StringVar()
descripcion_var = tk.StringVar()
caratula_var = tk.StringVar()
compositor_var = tk.StringVar()
arreglista_var = tk.StringVar()
productor_var = tk.StringVar()
interprete_var = tk.StringVar()
bit_rate_var = tk.StringVar()
codec_var = tk.StringVar()
duracion_var = tk.StringVar()
tamano_var = tk.StringVar()
frecuencia_var = tk.StringVar()
num_disco_var = tk.StringVar()
fecha_creacion_var = tk.StringVar()
fecha_modificacion_var = tk.StringVar()

tk.Label(ventana, text="Archivo:", bg="#f0f0f0").grid(row=0, column=0, sticky="e")
tk.Entry(ventana, textvariable=archivo_var, width=50).grid(row=0, column=1)
tk.Button(ventana, text="Seleccionar", command=seleccionar_archivo).grid(row=0, column=2)

tk.Label(ventana, text="Título:", bg="#f0f0f0").grid(row=1, column=0, sticky="e")
tk.Entry(ventana, textvariable=titulo_var, width=50).grid(row=1, column=1, columnspan=2)
tk.Label(ventana, text="Artista:", bg="#f0f0f0").grid(row=2, column=0, sticky="e")
tk.Entry(ventana, textvariable=artista_var, width=50).grid(row=2, column=1, columnspan=2)
tk.Label(ventana, text="Álbum:", bg="#f0f0f0").grid(row=3, column=0, sticky="e")
tk.Entry(ventana, textvariable=album_var, width=50).grid(row=3, column=1, columnspan=2)
tk.Label(ventana, text="Año:", bg="#f0f0f0").grid(row=4, column=0, sticky="e")
tk.Entry(ventana, textvariable=ano_var, width=50).grid(row=4, column=1, columnspan=2)
tk.Label(ventana, text="Género:", bg="#f0f0f0").grid(row=5, column=0, sticky="e")
tk.Entry(ventana, textvariable=genero_var, width=50).grid(row=5, column=1, columnspan=2)
tk.Label(ventana, text="Pista:", bg="#f0f0f0").grid(row=6, column=0, sticky="e")
tk.Entry(ventana, textvariable=pista_var, width=50).grid(row=6, column=1, columnspan=2)
tk.Label(ventana, text="Descripción:", bg="#f0f0f0").grid(row=7, column=0, sticky="e")
tk.Entry(ventana, textvariable=descripcion_var, width=50).grid(row=7, column=1, columnspan=2)
tk.Label(ventana, text="Compositor:", bg="#f0f0f0").grid(row=8, column=0, sticky="e")
tk.Entry(ventana, textvariable=compositor_var, width=50).grid(row=8, column=1, columnspan=2)
tk.Label(ventana, text="Arreglista:", bg="#f0f0f0").grid(row=9, column=0, sticky="e")
tk.Entry(ventana, textvariable=arreglista_var, width=50).grid(row=9, column=1, columnspan=2)
tk.Label(ventana, text="Productor:", bg="#f0f0f0").grid(row=10, column=0, sticky="e")
tk.Entry(ventana, textvariable=productor_var, width=50).grid(row=10, column=1, columnspan=2)
tk.Label(ventana, text="Intérprete:", bg="#f0f0f0").grid(row=11, column=0, sticky="e")
tk.Entry(ventana, textvariable=interprete_var, width=50).grid(row=11, column=1, columnspan=2)
tk.Label(ventana, text="Tasa de Bit:", bg="#f0f0f0").grid(row=12, column=0, sticky="e")
tk.Entry(ventana, textvariable=bit_rate_var, width=50, state="readonly").grid(row=12, column=1, columnspan=2)
tk.Label(ventana, text="Códec:", bg="#f0f0f0").grid(row=13, column=0, sticky="e")
tk.Entry(ventana, textvariable=codec_var, width=50, state="readonly").grid(row=13, column=1, columnspan=2)
tk.Label(ventana, text="Duración:", bg="#f0f0f0").grid(row=14, column=0, sticky="e")
tk.Entry(ventana, textvariable=duracion_var, width=50, state="readonly").grid(row=14, column=1, columnspan=2)
tk.Label(ventana, text="Tamaño (KB):", bg="#f0f0f0").grid(row=15, column=0, sticky="e")
tk.Entry(ventana, textvariable=tamano_var, width=50, state="readonly").grid(row=15, column=1, columnspan=2)
tk.Label(ventana, text="Frecuencia (Hz):", bg="#f0f0f0").grid(row=16, column=0, sticky="e")
tk.Entry(ventana, textvariable=frecuencia_var, width=50, state="readonly").grid(row=16, column=1, columnspan=2)
tk.Label(ventana, text="Número de Disco:", bg="#f0f0f0").grid(row=17, column=0, sticky="e")
tk.Entry(ventana, textvariable=num_disco_var, width=50).grid(row=17, column=1, columnspan=2)
tk.Label(ventana, text="Fecha de Creación:", bg="#f0f0f0").grid(row=18, column=0, sticky="e")
tk.Entry(ventana, textvariable=fecha_creacion_var, width=50, state="readonly").grid(row=18, column=1, columnspan=2)
tk.Label(ventana, text="Fecha de Modificación:", bg="#f0f0f0").grid(row=19, column=0, sticky="e")
tk.Entry(ventana, textvariable=fecha_modificacion_var, width=50, state="readonly").grid(row=19, column=1, columnspan=2)

tk.Label(ventana, text="Carátula:", bg="#f0f0f0").grid(row=20, column=0, sticky="e")
tk.Entry(ventana, textvariable=caratula_var, width=50).grid(row=20, column=1)
tk.Button(ventana, text="Seleccionar", command=seleccionar_caratula).grid(row=20, column=2)

caratula_label = tk.Label(ventana, text="Sin carátula", bg="#f0f0f0")
caratula_label.grid(row=21, column=1)

tk.Button(
    ventana, text="Guardar Metadatos", command=modificar_metadatos, bg="green", fg="white", font=("Arial", 12)
).grid(row=22, column=1, pady=20)

ventana.mainloop()
