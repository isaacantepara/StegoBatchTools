import base64
import os
import random
import sys

def imagen(ruta_imagen):
    """Convierte una imagen a base64."""
    with open(ruta_imagen, "rb") as imagen_archivo:
        imagen_binaria = imagen_archivo.read()
        return imagen_binaria  # No decodificamos a utf-8

def obtener_nombre_imagen(ruta_imagen):
    """Obtiene las primeras tres letras del nombre de la imagen."""
    nombre_archivo = os.path.basename(ruta_imagen)  # Extrae el nombre del archivo con la extensión
    nombre_sin_extension = os.path.splitext(nombre_archivo)[0]  # Elimina la extensión
    return nombre_sin_extension[:3]  # Devuelve las primeras tres letras

def ruido(imagen_binaria, carpeta_salida, folder, nombre_imagen, cantidad_ruido=1024):
    """Guarda el string base64 en un archivo binario con ruido."""
    os.makedirs(carpeta_salida, exist_ok=True)  # Crea la carpeta si no existe
    numero_random = str(random.randint(1000, 9999))  # Número aleatorio
    nombre_final = nombre_imagen + numero_random  # Combina las tres letras con el número

    # Definir la ruta de la carpeta y crearla si folder es True
    if folder:
        carpeta_salida = os.path.join(carpeta_salida, nombre_final)
        os.makedirs(carpeta_salida, exist_ok=True)

    ruta_archivo = os.path.join(carpeta_salida, nombre_final + ".null")  # Extensión ".null"
    ruido = bytes(random.randint(0, 255) for _ in range(cantidad_ruido))
    datos_con_ruido = ruido + imagen_binaria + ruido
    
    with open(ruta_archivo, "wb") as archivo_binario:
        archivo_binario.write(datos_con_ruido)
        return ruta_archivo

def procesar_imagen(ruta_imagen, carpeta_salida, folder, cantidad_ruido):
    """Procesa una única imagen."""
    imagen_binaria = imagen(ruta_imagen)
    nombre_imagen = obtener_nombre_imagen(ruta_imagen)
    print(ruido(imagen_binaria, carpeta_salida, isfolder(folder), nombre_imagen, cantidad_ruido))

def isfolder(folder):
    return folder == "-y"

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Uso: python codificarM_img.py <ruta_imagen> <ruta_carpeta_salida> <isfolder> <cantidad_ruido>")
        sys.exit(1)

    ruta_imagen = sys.argv[1]
    carpeta_salida = sys.argv[2]
    folder = sys.argv[3]
    cantidad_ruido = int(sys.argv[4])

    # Procesar una imagen única con el número de ruido especificado
    procesar_imagen(ruta_imagen, carpeta_salida, folder, cantidad_ruido)
