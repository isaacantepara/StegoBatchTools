import base64
import os
import random
from PIL import Image
import sys

def imagen_(ruta_archivo_binario, nombre_archivo, carpeta_salida, cantidad_ruido=1024):
    """Convierte un string base64 a una imagen y elimina el ruido."""
    os.makedirs(carpeta_salida, exist_ok=True)
    ruta_archivo = os.path.join(carpeta_salida, nombre_archivo + ".jpeg")  # Agrega extensión
    with open(ruta_archivo_binario, "rb") as archivo_binario:
        datos_con_ruido = archivo_binario.read()
        
        # Elimina el ruido
        imagen_binaria = datos_con_ruido[cantidad_ruido:-cantidad_ruido]
        
        with open(ruta_archivo, "wb") as imagen_archivo:
            imagen_archivo.write(imagen_binaria)

def recuperacion(carpeta_base64, carpeta_salida):
    """Recupera imágenes desde los archivos base64."""
    for nombre_archivo in os.listdir(carpeta_base64):
        # Elimina la extensión de la imagen original
        nombre_archivo_sin_ext = os.path.splitext(nombre_archivo)[0]
        ruta_archivo = os.path.join(carpeta_base64, nombre_archivo)
        imagen_(ruta_archivo, nombre_archivo_sin_ext, carpeta_salida, cantidad_ruido=1024)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 decodificarM_img.py <ruta_carpeta_codificada> <ruta_carpeta_decodificada>")
        sys.exit(1)

    carpeta_base64 = sys.argv[1]  # Ruta de la carpeta para los archivos base64
    carpeta_recuperadas = sys.argv[2]   # Ruta de la carpeta para las imágenes recuperadas

    # Recuperar las imágenes desde los archivos base64
    recuperacion(carpeta_base64, carpeta_recuperadas)