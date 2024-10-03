import base64
import os
import random
from PIL import Image
from cryptography.fernet import Fernet

def imagen_a_base64(ruta_imagen):
    """Convierte una imagen a base64."""
    with open(ruta_imagen, "rb") as imagen_archivo:
        imagen_binaria = imagen_archivo.read()
        return imagen_binaria  # No decodificamos a utf-8

def guardar_base64_con_ruido(imagen_binaria, nombre_archivo, carpeta_salida, cantidad_ruido=1024):
    """Guarda el string base64 en un archivo binario con ruido."""
    os.makedirs(carpeta_salida, exist_ok=True)  # Crea la carpeta si no existe
    ruta_archivo = os.path.join(carpeta_salida, nombre_archivo + ".imgbin")  # Añade la extensión ".imgbin"
    
    ruido = bytes(random.randint(0, 255) for _ in range(cantidad_ruido))
    datos_con_ruido = ruido + imagen_binaria + ruido
    
    with open(ruta_archivo, "wb") as archivo_binario:
        archivo_binario.write(datos_con_ruido)

def guardar_base64_cifrado(imagen_binaria, nombre_archivo, carpeta_salida, clave):
    """Guarda el string base64 en un archivo binario cifrado."""
    os.makedirs(carpeta_salida, exist_ok=True)  # Crea la carpeta si no existe
    ruta_archivo = os.path.join(carpeta_salida, nombre_archivo + ".enc")  # Añade la extensión ".enc"

    cipher_suite = Fernet(clave)
    imagen_cifrada = cipher_suite.encrypt(imagen_binaria)
    
    with open(ruta_archivo, "wb") as archivo_binario:
        archivo_binario.write(imagen_cifrada)

def base64_a_imagen(ruta_archivo_binario, nombre_archivo, carpeta_salida, cantidad_ruido=1024):
    """Convierte un string base64 a una imagen y elimina el ruido."""
    os.makedirs(carpeta_salida, exist_ok=True)
    ruta_archivo = os.path.join(carpeta_salida, nombre_archivo + ".png")  # Agrega extensión
    with open(ruta_archivo_binario, "rb") as archivo_binario:
        datos_con_ruido = archivo_binario.read()
        
        # Elimina el ruido
        imagen_binaria = datos_con_ruido[cantidad_ruido:-cantidad_ruido]
        
        with open(ruta_archivo, "wb") as imagen_archivo:
            imagen_archivo.write(imagen_binaria)

def base64_a_imagen_descifrado(ruta_archivo_binario, nombre_archivo, carpeta_salida, clave):
    """Convierte un string base64 cifrado a una imagen y la descifra."""
    os.makedirs(carpeta_salida, exist_ok=True)
    ruta_archivo = os.path.join(carpeta_salida, nombre_archivo + ".png")  # Agrega extensión
    with open(ruta_archivo_binario, "rb") as archivo_binario:
        imagen_cifrada = archivo_binario.read()
        
        # Descifra la imagen
        cipher_suite = Fernet(clave)
        imagen_descifrada = cipher_suite.decrypt(imagen_cifrada)
        
        with open(ruta_archivo, "wb") as imagen_archivo:
            imagen_archivo.write(imagen_descifrada)

def procesar_imagenes(carpeta_imagenes, carpeta_salida):
    """Procesa todas las imágenes de una carpeta."""
    for nombre_archivo in os.listdir(carpeta_imagenes):
        if nombre_archivo.endswith((".jpg", ".jpeg", ".png")):
            ruta_imagen = os.path.join(carpeta_imagenes, nombre_archivo)
            imagen_binaria = imagen_a_base64(ruta_imagen)
            guardar_base64_con_ruido(imagen_binaria, nombre_archivo, carpeta_salida)

def recuperar_imagenes(carpeta_base64, carpeta_salida):
    """Recupera imágenes desde los archivos base64."""
    for nombre_archivo in os.listdir(carpeta_base64):
        # Elimina la extensión de la imagen original
        nombre_archivo_sin_ext = os.path.splitext(nombre_archivo)[0]
        ruta_archivo = os.path.join(carpeta_base64, nombre_archivo)
        base64_a_imagen(ruta_archivo, nombre_archivo_sin_ext, carpeta_salida, cantidad_ruido=1024)

def cifrar_imagenes(carpeta_imagenes, carpeta_salida, clave):
    """Cifra las imágenes de una carpeta."""
    for nombre_archivo in os.listdir(carpeta_imagenes):
        if nombre_archivo.endswith((".jpg", ".jpeg", ".png")):
            ruta_imagen = os.path.join(carpeta_imagenes, nombre_archivo)
            imagen_binaria = imagen_a_base64(ruta_imagen)
            guardar_base64_cifrado(imagen_binaria, nombre_archivo, carpeta_salida, clave)

def descifrar_imagenes(carpeta_cifrada, carpeta_salida, clave):
    """Descifra las imágenes de una carpeta."""
    for nombre_archivo in os.listdir(carpeta_cifrada):
        if nombre_archivo.endswith(".enc"):
            ruta_archivo = os.path.join(carpeta_cifrada, nombre_archivo)
            base64_a_imagen_descifrado(ruta_archivo, os.path.splitext(nombre_archivo)[0], carpeta_salida, clave)

if __name__ == "__main__":
    carpeta_imagenes = "./imgAnimals"  # Nombre de la carpeta con tus imágenes
    carpeta_base64 = "./binImgAnimals"  # Nombre de la carpeta para los archivos base64
    carpeta_recuperadas = "./binToOriginal"   # Nombre de la carpeta para las imágenes recuperadas
    carpeta_cifradas = "./cifradas" # Nombre de la carpeta para las imágenes cifradas
    carpeta_descifradas = "./descifradas" # Nombre de la carpeta para las imágenes descifradas
    
    # Genera una clave secreta
    clave = Fernet.generate_key()
    
    # Imprime la clave
    print("Clave secreta:", clave.decode()) 

    # Convertir las imágenes a base64 y guardar en carpetas separadas
    procesar_imagenes(carpeta_imagenes, carpeta_base64)

    # Recuperar las imágenes desde los archivos base64
    recuperar_imagenes(carpeta_base64, carpeta_recuperadas)
    
    # Cifrar las imágenes
    cifrar_imagenes(carpeta_imagenes, carpeta_cifradas, clave)
    
    # Descifrar las imágenes
    descifrar_imagenes(carpeta_cifradas, carpeta_descifradas, clave)