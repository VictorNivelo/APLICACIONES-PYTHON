import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime
from win32file import CreateFile, SetFileTime, CloseHandle
from win32file import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
import pywintypes
import os


class CambiadorFechas:
    def __init__(self, root):
        self.root = root
        self.root.title("Modificador de Fechas")
        self.root.geometry("600x400")
        self.archivo_seleccionado = tk.StringVar()
        self.fecha_var = tk.StringVar()
        self.hora_var = tk.StringVar()
        self.setup_styles()
        self.crear_interfaz()

    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Main.TFrame", background="#f0f0f0")
        self.style.configure("Modern.TButton", padding=10, font=("Segoe UI", 10))
        self.style.configure("Modern.TLabel", font=("Segoe UI", 10))
        self.style.configure("Modern.TLabelframe", font=("Segoe UI", 10))
        self.style.configure("Modern.TEntry", padding=5)

    def crear_interfaz(self):
        main_frame = ttk.Frame(self.root, style="Main.TFrame", padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        file_frame = ttk.Frame(main_frame)
        file_frame.pack(fill=tk.X, pady=(0, 20))
        ttk.Label(file_frame, text="Archivo:", style="Modern.TLabel").pack(side=tk.LEFT)
        ttk.Entry(file_frame, textvariable=self.archivo_seleccionado, width=50).pack(side=tk.LEFT, padx=5)
        ttk.Button(file_frame, text="Buscar", command=self.buscar_archivo, style="Modern.TButton").pack(side=tk.LEFT)
        fecha_frame = ttk.LabelFrame(main_frame, text="Nueva fecha y hora", padding=15, style="Modern.TLabelframe")
        fecha_frame.pack(fill=tk.X, pady=20)
        self.fecha_var.set(datetime.now().strftime("%d/%m/%Y"))
        self.hora_var.set(datetime.now().strftime("%H:%M"))
        ttk.Label(fecha_frame, text="Fecha (DD/MM/AAAA):", style="Modern.TLabel").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(fecha_frame, textvariable=self.fecha_var, width=15).grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(fecha_frame, text="Hora (HH:MM):", style="Modern.TLabel").grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(fecha_frame, textvariable=self.hora_var, width=15).grid(row=1, column=1, padx=5, pady=5)
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(fill=tk.X, pady=20)
        ttk.Button(
            buttons_frame,
            text="Modificar Fecha de Creación",
            command=lambda: self.modificar_fecha("creacion"),
            style="Modern.TButton",
        ).pack(fill=tk.X, pady=5)
        ttk.Button(
            buttons_frame,
            text="Modificar Fecha de Modificación",
            command=lambda: self.modificar_fecha("modificacion"),
            style="Modern.TButton",
        ).pack(fill=tk.X, pady=5)
        ttk.Button(
            buttons_frame,
            text="Modificar Fecha de Acceso",
            command=lambda: self.modificar_fecha("acceso"),
            style="Modern.TButton",
        ).pack(fill=tk.X, pady=5)

    def buscar_archivo(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.archivo_seleccionado.set(filename)

    def obtener_fecha_hora(self):
        try:
            fecha_str = self.fecha_var.get()
            hora_str = self.hora_var.get()
            fecha_completa = f"{fecha_str} {hora_str}"
            return datetime.strptime(fecha_completa, "%d/%m/%Y %H:%M")
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha u hora inválido")
            return None

    def modificar_fecha_creacion(self, ruta, nueva_fecha):
        try:
            wintime = pywintypes.Time(nueva_fecha)
            handle = CreateFile(ruta, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0, 0)
            SetFileTime(handle, wintime, None, None)
            CloseHandle(handle)
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Error al modificar fecha de creación: {str(e)}")
            return False

    def modificar_fecha_modificacion(self, ruta, nueva_fecha):
        try:
            timestamp = nueva_fecha.timestamp()
            os.utime(ruta, (timestamp, timestamp))
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Error al modificar fecha de modificación: {str(e)}")
            return False

    def modificar_fecha_acceso(self, ruta, nueva_fecha):
        try:
            timestamp = nueva_fecha.timestamp()
            os.utime(ruta, (timestamp, os.path.getmtime(ruta)))
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Error al modificar fecha de acceso: {str(e)}")
            return False

    def modificar_fecha(self, tipo):
        archivo = self.archivo_seleccionado.get()
        if not archivo:
            messagebox.showerror("Error", "Por favor seleccione un archivo")
            return
        nueva_fecha = self.obtener_fecha_hora()
        if not nueva_fecha:
            return
        if tipo == "creacion":
            if self.modificar_fecha_creacion(archivo, nueva_fecha):
                messagebox.showinfo("Éxito", "Fecha de creación modificada correctamente")
        elif tipo == "modificacion":
            if self.modificar_fecha_modificacion(archivo, nueva_fecha):
                messagebox.showinfo("Éxito", "Fecha de modificación modificada correctamente")
        elif tipo == "acceso":
            if self.modificar_fecha_acceso(archivo, nueva_fecha):
                messagebox.showinfo("Éxito", "Fecha de acceso modificada correctamente")


if __name__ == "__main__":
    root = tk.Tk()
    app = CambiadorFechas(root)
    root.mainloop()
