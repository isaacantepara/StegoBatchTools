import sys
import os
from PIL import Image

def duplicar_pixeles(carpeta_imagenes, carpeta_salida):
    """
    Duplica la cantidad de píxeles en todas las imágenes de una carpeta.

    Args:
        carpeta_imagenes: La ruta de la carpeta con las imágenes originales.
        carpeta_salida: La ruta de la carpeta donde se guardarán las imágenes duplicadas.
    """
    try:
        # Crear la carpeta de salida si no existe
        os.makedirs(carpeta_salida, exist_ok=True)

        # 1. Itera sobre todos los archivos en la carpeta de imágenes
        for nombre_archivo in os.listdir(carpeta_imagenes):
            ruta_imagen = os.path.join(carpeta_imagenes, nombre_archivo)

            # Verifica si es un archivo de imagen (extensiones comunes)
            if nombre_archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                # Carga la imagen
                image = Image.open(ruta_imagen)

                # Obtiene el tamaño original
                ancho_original, alto_original = image.size

                # Calcula el nuevo tamaño (el doble)
                nuevo_ancho = ancho_original * 10
                nuevo_alto = alto_original * 10
                nuevo_tamano = (nuevo_ancho, nuevo_alto)

                # Cambia el tamaño de la imagen
                image_duplicada = image.resize(nuevo_tamano)

                # Combina la carpeta de salida con el nombre del archivo
                ruta_salida_completa = os.path.join(carpeta_salida, nombre_archivo)

                # Guarda la imagen duplicada
                image_duplicada.save(ruta_salida_completa)
                print(f"Imagen duplicada y guardada en: {ruta_salida_completa}")
            else:
                print(f"'{nombre_archivo}' no es un archivo de imagen y será omitido.")

    except FileNotFoundError:
        print(f"Error: La carpeta '{carpeta_imagenes}' no se encontró.")
    except Exception as e:
        print(f"Error al procesar las imágenes: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python aumentar_pixeles.py <carpeta_imagenes> <carpeta_salida>")
        sys.exit(1)

    # Argumentos desde la línea de comandos
    carpeta_imagenes = sys.argv[1]  # Ruta de la carpeta con las imágenes originales
    carpeta_salida = sys.argv[2]     # Ruta de la carpeta donde se guardarán las imágenes duplicadas

    duplicar_pixeles(carpeta_imagenes, carpeta_salida)
