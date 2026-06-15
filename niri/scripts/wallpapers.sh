#!/bin/bash

# Usamos $HOME en lugar de ~ dentro de las comillas dobles
DIR="$HOME/Pictures/Wallpapers/blueink"
INTERVALO=600 # Tiempo en segundos

# Arrancar el demonio si no está corriendo
awww query || awww-daemon --format xrgb &

# Una pausa minúscula para asegurar que el demonio cree el socket antes de mandar imágenes
sleep 1 

while true; do
    # Iterar numéricamente del 1 al 20
    for i in {1..20}; do
        IMG="$DIR/$i.jpg"
        if [ -f "$IMG" ]; then
            # Cambia la imagen con transición
            awww img "$IMG" --resize no --fill-color e6ded5 --transition-type wave --transition-duration 3
            sleep $INTERVALO
        fi
    done
done
