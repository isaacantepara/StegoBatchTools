import base64
import os
import sys
from PIL import Image

def imagen_(ruta_archivo_binario, nombre_archivo, carpeta_salida, cantidad_ruido=1024):
    """Convierte un string base64 a una imagen y elimina el ruido."""
    ruta_archivo = os.path.join(carpeta_salida, nombre_archivo + ".jpeg")  # Agrega extensión
    with open(ruta_archivo_binario, "rb") as archivo_binario:
        datos_con_ruido = archivo_binario.read()
        
        # Elimina el ruido
        imagen_binaria = datos_con_ruido[cantidad_ruido:-cantidad_ruido]
        
        with open(ruta_archivo, "wb") as imagen_archivo:
            imagen_archivo.write(imagen_binaria)

def recuperar(ruta_archivo_base64, nombre_archivo, cantidad_ruido=1024):
    """Recupera una imagen desde un archivo base64."""
    imagen_(ruta_archivo_base64, nombre_archivo, ".", cantidad_ruido)  # Guarda en la ruta actual

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 test.py <ruta_archivo_base64>")
        sys.exit(1)

    ruta_archivo_base64 = sys.argv[1]
    nombre_archivo = os.path.splitext(os.path.basename(ruta_archivo_base64))[0]

    # Recuperar la imagen desde el archivo base64
    recuperar(ruta_archivo_base64, nombre_archivo)