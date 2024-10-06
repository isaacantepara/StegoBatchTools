import sys
from PIL import Image

def duplicar_pixeles(ruta_imagen, ruta_salida):
    """
    Duplica la cantidad de píxeles en una imagen.

    Args:
        ruta_imagen: La ruta de la imagen original.
        ruta_salida: La ruta donde se guardará la imagen duplicada.
    """

    try:
        # 1. Carga la imagen
        image = Image.open(ruta_imagen)

        # 2. Obtén el tamaño original
        ancho_original, alto_original = image.size

        # 3. Calcula el nuevo tamaño (el doble)
        nuevo_ancho = ancho_original * 20
        nuevo_alto = alto_original * 20
        nuevo_tamano = (nuevo_ancho, nuevo_alto)

        # 4. Cambia el tamaño de la imagen
        image_duplicada = image.resize(nuevo_tamano)

        # 5. Guarda la imagen duplicada
        image_duplicada.save(ruta_salida)
        print(f"Imagen duplicada y guardada en: {ruta_salida}")

    except FileNotFoundError:
        print(f"Error: La imagen '{ruta_imagen}' no se encontró.")
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python pixel.py <ruta_imagen>")
        sys.exit(1)

    ruta_imagen = sys.argv[1]
    ruta_salida = "imagen_duplicada_pixel.jpeg"  # Puedes cambiar el nombre del archivo aquí

    duplicar_pixeles(ruta_imagen, ruta_salida)