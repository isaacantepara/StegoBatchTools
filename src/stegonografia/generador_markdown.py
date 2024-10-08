import sys
import os
import random
from faker import Faker

# Configuramos Faker para que use un idioma específico, en este caso español
fake = Faker('es_ES')

# Función para generar archivos markdown con título y contenido aleatorio
# Función para generar archivos markdown con título y contenido aleatorio
def generar(ruta_salida, cantidad):
    for i in range(int(cantidad)):
        # Generar un título aleatorio
        titulo = fake.catch_phrase()

        # Generar párrafos de contenido aleatorio
        contenido = "\n\n".join([fake.paragraph(nb_sentences=random.randint(5, 10)) for _ in range(random.randint(2, 5))])

        # Crear nombre de archivo basado en el título y asegurar la extensión .md
        nombre_archivo = f"{titulo.replace(' ', '_').lower()}.md"
        # Reemplazar caracteres no válidos en el nombre del archivo
        nombre_archivo = nombre_archivo.replace(',', '').replace('..', '').replace('/', '_')

        # Generar un número aleatorio para el nombre de la carpeta
        nombre_carpeta = str(random.randint(1000, 9999))

        # Definir la ruta de la carpeta y crearla
        ruta_carpeta = os.path.join(ruta_salida, nombre_carpeta)
        os.makedirs(ruta_carpeta, exist_ok=True)

        # Definir la ruta completa del archivo dentro de la carpeta
        ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)

        # Escribir en el archivo .md
        with open(ruta_completa, 'w', encoding='utf-8') as f:
            f.write(f"# {titulo}\n\n")
            f.write(contenido)
        
        print(f"Archivo generado: {ruta_completa}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 script.py ruta_salida cantidad_archivos")
        sys.exit(1)

    ruta_salida = sys.argv[1]
    cantidad_archivos = sys.argv[2]


    if not os.path.exists(ruta_salida):
        os.makedirs(ruta_salida)

    # Generar los archivos MD
    generar(ruta_salida, cantidad_archivos)
