import base64
import os
from PIL import Image

def imagen_a_base64(ruta_imagen):
    """Convierte una imagen a base64."""
    with open(ruta_imagen, "rb") as imagen_archivo:
        imagen_binaria = imagen_archivo.read()
        base64_string = base64.b64encode(imagen_binaria).decode("utf-8")
        return base64_string

def guardar_base64(base64_string, nombre_archivo, carpeta_salida):
    """Guarda el string base64 en un archivo txt."""
    os.makedirs(carpeta_salida, exist_ok=True)  # Crea la carpeta si no existe
    ruta_archivo = os.path.join(carpeta_salida, nombre_archivo + ".txt")
    with open(ruta_archivo, "w") as archivo_txt:
        archivo_txt.write(base64_string)

def base64_a_imagen(base64_string, nombre_archivo, carpeta_salida):
    """Convierte un string base64 a una imagen."""
    os.makedirs(carpeta_salida, exist_ok=True)
    ruta_archivo = os.path.join(carpeta_salida, nombre_archivo + ".png")
    imagen_binaria = base64.b64decode(base64_string)
    with open(ruta_archivo, "wb") as imagen_archivo:
        imagen_archivo.write(imagen_binaria)

def procesar_imagenes(carpeta_imagenes, carpeta_salida):
    """Procesa todas las imágenes de una carpeta."""
    for nombre_archivo in os.listdir(carpeta_imagenes):
        if nombre_archivo.endswith((".jpg", ".jpeg", ".png")):
            ruta_imagen = os.path.join(carpeta_imagenes, nombre_archivo)
            base64_string = imagen_a_base64(ruta_imagen)
            # Guarda el archivo en la carpeta base64 directamente
            guardar_base64(base64_string, nombre_archivo, carpeta_salida) 

def recuperar_imagenes(carpeta_base64, carpeta_salida):
    """Recupera imágenes desde los archivos base64."""
    for nombre_archivo in os.listdir(carpeta_base64):
        if nombre_archivo.endswith(".txt"):
            ruta_archivo = os.path.join(carpeta_base64, nombre_archivo)
            with open(ruta_archivo, "r") as archivo_txt:
                base64_string = archivo_txt.read()
                nombre_imagen = os.path.splitext(nombre_archivo)[0]
                base64_a_imagen(base64_string, nombre_imagen, carpeta_salida)

if __name__ == "__main__":
    carpeta_imagenes = "./imgAnimals"  # Nombre de la carpeta con tus imágenes
    carpeta_base64 = "./base64ImgAnimals"  # Nombre de la carpeta para los archivos base64
    carpeta_recuperadas = "./base64ToOriginal"  # Nombre de la carpeta para las imágenes recuperadas

    # Convertir las imágenes a base64 y guardar en carpetas separadas
    procesar_imagenes(carpeta_imagenes, carpeta_base64)

    # Recuperar las imágenes desde los archivos base64
    recuperar_imagenes(carpeta_base64, carpeta_recuperadas)