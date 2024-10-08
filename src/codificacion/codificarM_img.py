import base64
import os
import random
from PIL import Image
import sys
import random

def imagen(ruta_imagen):
    """Convierte una imagen a base64."""
    with open(ruta_imagen, "rb") as imagen_archivo:
        imagen_binaria = imagen_archivo.read()
        return imagen_binaria  # No decodificamos a utf-8

def ruido(imagen_binaria, carpeta_salida, folder, cantidad_ruido=1024):
    """Guarda el string base64 en un archivo binario con ruido."""
    os.makedirs(carpeta_salida, exist_ok=True)  # Crea la carpeta si no existe
    nombre_random = str(random.randint(1000, 9999))
 

    # Definir la ruta de la carpeta y crearla
    if(folder):
        carpeta_salida = os.path.join(carpeta_salida, nombre_random)
        os.makedirs(carpeta_salida, exist_ok=True)


    ruta_archivo = os.path.join(carpeta_salida, nombre_random + ".null")  # Añade la extensión ".imgbin"
    ruido = bytes(random.randint(0, 255) for _ in range(cantidad_ruido))
    datos_con_ruido = ruido + imagen_binaria + ruido
    
    with open(ruta_archivo, "wb") as archivo_binario:
        archivo_binario.write(datos_con_ruido)
        return ruta_archivo



def procesar_imagenes(carpeta_imagenes, carpeta_salida, folder):
    """Procesa todas las imágenes de una carpeta."""
    for nombre_archivo in os.listdir(carpeta_imagenes):
        if nombre_archivo.endswith((".jpg", ".jpeg", ".png")):
            ruta_imagen = os.path.join(carpeta_imagenes, nombre_archivo)
            imagen_binaria = imagen(ruta_imagen)
            print(ruido(imagen_binaria, carpeta_salida, isfolder(folder)))

def isfolder(folder):
    if(folder == "-y"):
        return True
    else:
        return False


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python  codificarM_img.py <ruta_carpeta_imagenes> <ruta_carpeta_salida> isfolder")
        sys.exit(1)

    carpeta_imagenes = sys.argv[1]
    carpeta_imagenes_codificadas = sys.argv[2]
    folder = sys.argv[3]

    # Convertir las imágenes a base64 y guardar en carpetas separadas
    procesar_imagenes(carpeta_imagenes, carpeta_imagenes_codificadas, folder)