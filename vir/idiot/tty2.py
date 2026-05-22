#!/bin/bash

# Twoje logo (w wersji bez znaków specjalnych, żeby bash się nie wywalił na Atomie)
LOGO="YOU ARE AN IDIOT!
⠀⣀⣤⠤⠤⣤⣄⣀⠀
⣠⡞⠉⠀⠀⠀⠀⠀⠉⠳⣄
⢰⡏⠀⠰⣿⡷⠀⢿⣿⠆⠀⢹⣦
⢸⡃⠀⠀⠉⠁⠀⠈⠉⠀⠀⢸⣿
⠸⣇⠺⣦⡀⠀⠀⠀⢀⣴⠇⣸⠿
⠀⠻⣦⡈⠙⠓⠒⠛⠋⣁⣴⠏
⠀⠈⠙⠓⠶⠶⠶⠛⠋⠀"

# Funkcja otwierająca terminal z logo
spawn_terminal() {
    # -e odpala komendę w nowym oknie i trzyma je otwarte (bash --hold)
    lxterminal -t "!!!" -e "bash -c 'echo -e \"\e[35m$LOGO\e[0m\"; exec bash'" &
}

# Główna pętla
while true; do
    spawn_terminal
    echo -en "\007" # Beep!
    sleep 0.5       # Nowe okno co pół sekundy
done

