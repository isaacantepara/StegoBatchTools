import base64
import os
from PIL import Image

def imagen_a_base64(ruta_imagen):
    """Convierte una imagen a base64."""
    with open(ruta_imagen, "rb") as imagen_archivo:
        imagen_binaria = imagen_archivo.read()
        return imagen_binaria  # No decodificamos a utf-8

def guardar_base64(imagen_binaria, nombre_archivo, carpeta_salida):
    """Guarda el string base64 en un archivo txt."""
    os.makedirs(carpeta_salida, exist_ok=True)  # Crea la carpeta si no existe
    ruta_archivo = os.path.join(carpeta_salida, nombre_archivo + ".bin")  # Extensión ".bin"
    with open(ruta_archivo, "wb") as archivo_binario:
        archivo_binario.write(imagen_binaria)

def base64_a_imagen(ruta_archivo_binario, nombre_archivo, carpeta_salida):
    """Convierte un string base64 a una imagen."""
    os.makedirs(carpeta_salida, exist_ok=True)
    ruta_archivo = os.path.join(carpeta_salida, nombre_archivo + ".png")
    with open(ruta_archivo_binario, "rb") as archivo_binario:
        imagen_binaria = archivo_binario.read()
        with open(ruta_archivo, "wb") as imagen_archivo:
            imagen_archivo.write(imagen_binaria)

def procesar_imagenes(carpeta_imagenes, carpeta_salida):
    """Procesa todas las imágenes de una carpeta."""
    for nombre_archivo in os.listdir(carpeta_imagenes):
        if nombre_archivo.endswith((".jpg", ".jpeg", ".png")):
            ruta_imagen = os.path.join(carpeta_imagenes, nombre_archivo)
            imagen_binaria = imagen_a_base64(ruta_imagen)
            guardar_base64(imagen_binaria, nombre_archivo, carpeta_salida)

def recuperar_imagenes(carpeta_base64, carpeta_salida):
    """Recupera imágenes desde los archivos base64."""
    for nombre_archivo in os.listdir(carpeta_base64):
        if nombre_archivo.endswith(".bin"):
            ruta_archivo = os.path.join(carpeta_base64, nombre_archivo)
            base64_a_imagen(ruta_archivo, os.path.splitext(nombre_archivo)[0], carpeta_salida)

if __name__ == "__main__":
    carpeta_imagenes = "./imgAnimals"  # Nombre de la carpeta con tus imágenes
    carpeta_base64 = "./binImgAnimals"  # Nombre de la carpeta para los archivos base64
    carpeta_recuperadas = "./binToOriginal"   # Nombre de la carpeta para las imágenes recuperadas

    # Convertir las imágenes a base64 y guardar en carpetas separadas
    procesar_imagenes(carpeta_imagenes, carpeta_base64)

    # Recuperar las imágenes desde los archivos base64
    recuperar_imagenes(carpeta_base64, carpeta_recuperadas)