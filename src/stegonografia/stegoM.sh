#!/bin/bash

# Verificar si se pasaron dos argumentos (la ruta de la carpeta de zips y la ruta de la carpeta de imágenes)
if [ $# -ne 2 ]; then
  echo "Uso: $0 /ruta/a/carpeta/con/zip /ruta/a/carpeta/con/imagenes"
  exit 1
fi

# Verificar si stegohide está instalado
if ! command -v steghide &> /dev/null; then
    echo "steghide no está instalado. Instálalo primero."
    exit 1
fi

# Ruta de la carpeta de archivos zip
carpeta_zips="$1"

# Ruta de la carpeta de imágenes
carpeta_imagenes="$2"

# Crear la carpeta stegoImg si no existe
carpeta_stego="stegoMain"
mkdir -p "$carpeta_stego"

# Iterar sobre cada archivo .zip en la carpeta proporcionada
for archivo_zip in "$carpeta_zips"/*.zip; do
  # Intentar hasta que se complete la operación o no queden imágenes
  while true; do
    # Generar un nombre de imagen base seleccionando aleatoriamente de la carpeta de imágenes
    imagen=$(find "$carpeta_imagenes" -type f -name "*.jpg" | shuf -n 1)

    if [ -f "$imagen" ]; then
      # Generar el nombre de la imagen resultante en la carpeta stegoImg
      nombre_imagen_stego="$carpeta_stego/$(basename "$imagen" .jpg).jpg"

      echo "Incrustando $archivo_zip en $imagen..."
      
      # Usar stegohide para ocultar el archivo zip en la imagen sin contraseña
      if steghide embed -cf "$imagen" -ef "$archivo_zip" -sf "$nombre_imagen_stego" -p ""; then
        echo "Proceso completado para $archivo_zip. Imagen guardada como $nombre_imagen_stego"
        break  # Salir del bucle si la operación fue exitosa
      else
        echo "Falló al incrustar $archivo_zip en $imagen. Intentando con otra imagen..."
      fi
    else
      echo "No se encontraron imágenes disponibles en la ruta proporcionada."
      break  # Salir si no hay imágenes disponibles
    fi
  done
done
