import time
import os
import pygame # Dźwięk powinien działać, jeśli jest karta dźwiękowa

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

def play_audio():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("idiot.mp3")
        pygame.mixer.music.play(-1)
    except:
        pass

def flood_terminal():
    while True:
        print(ASCII_LOGO)
        print("\a") # Ten znak wysyła systemowy "beep" - mega irytujące!
        time.sleep(0.1)

if __name__ == "__main__":
    play_audio()
    flood_terminal()

