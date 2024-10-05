import base64
import os
import random
from PIL import Image

def imagen_a_base64(ruta_imagen):
    """Convierte una imagen a base64."""
    with open(ruta_imagen, "rb") as imagen_archivo:
        imagen_binaria = imagen_archivo.read()
        return imagen_binaria  # No decodificamos a utf-8

def ruido(imagen_binaria, nombre_archivo, carpeta_salida, cantidad_ruido=1024):
    """Guarda el string base64 en un archivo binario con ruido."""
    os.makedirs(carpeta_salida, exist_ok=True)  # Crea la carpeta si no existe
    ruta_archivo = os.path.join(carpeta_salida, nombre_archivo + ".null")  # Añade la extensión ".imgbin"
    
    ruido = bytes(random.randint(0, 255) for _ in range(cantidad_ruido))
    datos_con_ruido = ruido + imagen_binaria + ruido
    
    with open(ruta_archivo, "wb") as archivo_binario:
        archivo_binario.write(datos_con_ruido)



def procesar_imagenes(carpeta_imagenes, carpeta_salida):
    """Procesa todas las imágenes de una carpeta."""
    for nombre_archivo in os.listdir(carpeta_imagenes):
        if nombre_archivo.endswith((".jpg", ".jpeg", ".png")):
            ruta_imagen = os.path.join(carpeta_imagenes, nombre_archivo)
            imagen_binaria = imagen_a_base64(ruta_imagen)
            ruido(imagen_binaria, nombre_archivo.split(".")[0]  , carpeta_salida)



if __name__ == "__main__":
    carpeta_imagenes = "../data/img"  # Nombre de la carpeta con tus imágenes
    carpeta_base64 = "../pendriver/codificar"  # Nombre de la carpeta para los archivos base64
    # Convertir las imágenes a base64 y guardar en carpetas separadas
    procesar_imagenes(carpeta_imagenes, carpeta_base64)