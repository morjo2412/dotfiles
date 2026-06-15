#!/bin/bash

# 1. Obtener la lista de particiones desmontadas y mostrarla en fzf
SELECCION=$(lsblk -rpo NAME,LABEL,SIZE,TYPE,MOUNTPOINT | \
    awk '$4=="part" && $5=="" {printf "%-15s %-15s %s\n", $1, $2, $3}' | \
    fzf --prompt="Montar USB > " --height=40% --layout=reverse)

# 2. Extraer solo la ruta del dispositivo (ej. /dev/sda1)
DISPOSITIVO=$(echo "$SELECCION" | awk '{print $1}')

# 3. Si elegiste algo, montarlo
if [ -n "$DISPOSITIVO" ]; then
    udiskie-mount "$DISPOSITIVO"
fi
