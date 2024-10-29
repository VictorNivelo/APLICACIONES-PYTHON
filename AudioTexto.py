import tkinter as tk
from tkinter import filedialog, messagebox
import speech_recognition as sr
from pydub import AudioSegment
import os
from pydub.utils import which

os.environ["PATH"] += os.pathsep + r"C:\Users\Victor\Documents\Proyectos\ffmpeg\ffmpeg-master-latest-win64-gpl\bin"

if which("ffmpeg") is None:
    raise Exception("FFmpeg no encontrado")

FFMPEG_PATH = r"C:\Users\Victor\Documents\Proyectos\ffmpeg\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"
FFPROBE_PATH = r"C:\Users\Victor\Documents\Proyectos\ffmpeg\ffmpeg-master-latest-win64-gpl\bin\ffprobe.exe"

if not os.path.exists(FFMPEG_PATH) or not os.path.exists(FFPROBE_PATH):
    raise Exception("No se encontraron los archivos de FFmpeg")

AudioSegment.converter = FFMPEG_PATH
AudioSegment.ffmpeg = FFMPEG_PATH
AudioSegment.ffprobe = FFPROBE_PATH

class AudioTranscriber:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Transcriptor de Audio")
        self.window.geometry("600x400")
        self.create_widgets()

    def create_widgets(self):
        self.select_button = tk.Button(self.window, text="Seleccionar Audio", command=self.select_file)
        self.select_button.pack(pady=20)
        self.text_area = tk.Text(self.window, height=15, width=50)
        self.text_area.pack(pady=20)
        self.save_button = tk.Button(self.window, text="Guardar Transcripción", command=self.save_transcription)
        self.save_button.pack(pady=20)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos de audio", "*.wav *.mp3 *.m4a *.ogg")])
        if file_path:
            self.transcribe_audio(file_path)

    def transcribe_audio(self, file_path):
        try:
            if not file_path.endswith(".wav"):
                audio = AudioSegment.from_file(file_path)
                wav_path = "temp.wav"
                audio.export(wav_path, format="wav")
            else:
                wav_path = file_path
            recognizer = sr.Recognizer()
            with sr.AudioFile(wav_path) as source:
                audio_data = recognizer.record(source)
                text = recognizer.recognize_sphinx(audio_data)
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, text)
            if not file_path.endswith(".wav"):
                os.remove(wav_path)
        except Exception as e:
            messagebox.showerror("Error", f"Error al transcribir el audio: {str(e)}")

    def save_transcription(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivo de texto", "*.txt")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.text_area.get(1.0, tk.END))
            messagebox.showinfo("Éxito", "Transcripción guardada exitosamente")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = AudioTranscriber()
    app.run()