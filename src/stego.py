from docx import Document
from PyPDF2 import PdfReader, PdfWriter
import os
import subprocess

# Definir las rutas de las carpetas
ruta_docx = "/home/pythonesso/Documents/zoo/informes_zoologico"  # Ajusta la ruta
ruta_bin = "/home/pythonesso/Documents/zoo/binImgAnimals"  # Ajusta la ruta
ruta_salida = "/home/pythonesso/Documents/zoo/informes_zoologico_stego"  # Ruta para la carpeta de salida

# Crear la carpeta de salida si no existe
if not os.path.exists(ruta_salida):
    os.makedirs(ruta_salida)

# Obtener las listas de archivos
archivos_docx = [f for f in os.listdir(ruta_docx) if f.endswith(".docx")]
archivos_bin = [f for f in os.listdir(ruta_bin) if f.endswith(".bin")]

# Lista para almacenar los archivos DOCX con esteganografía
archivos_stego = []

# Iterar sobre los archivos BIN
for archivo_bin in archivos_bin:
    # Leer el contenido del archivo BIN
    with open(os.path.join(ruta_bin, archivo_bin), "rb") as f:
        contenido_bin = f.read()

    # Verificar si hay archivos DOCX disponibles
    if archivos_docx:
        # Seleccionar el siguiente archivo DOCX
        archivo_docx = archivos_docx.pop(0)

        # Convertir DOCX a PDF
        nombre_archivo_pdf = os.path.splitext(archivo_docx)[0] + ".pdf"
        ruta_archivo_pdf = os.path.join(ruta_salida, nombre_archivo_pdf)
        comando_conversion = f"libreoffice --headless --convert-to pdf --outdir {ruta_salida} {os.path.join(ruta_docx, archivo_docx)}"
        subprocess.call(comando_conversion.split())

        # Aplicar esteganografía con Outguess (se puede reemplazar por Steghide, etc.)
        nombre_archivo_stego = nombre_archivo_pdf.replace(".pdf", "_stego.pdf")
        ruta_archivo_stego = os.path.join(ruta_salida, nombre_archivo_stego)

        #TODO:ERROR NO PROCESA EL COMANDO, EN SI ES PORQUE NO HAY HERRAMIENTA QUE APLIQUE ESTEGO EN PDF, SI HAY, PERO ES UN WINDOS OPENPUFF 
        comando_stego = f"outguess -r \"{ruta_archivo_pdf}\" -d \"{os.path.join(ruta_bin, archivo_bin)}\" \"{ruta_archivo_stego}\""
        
        
        subprocess.call(comando_stego.split())
        # Agregar el archivo PDF a la lista de archivos con esteganografía
        archivos_stego.append(nombre_archivo_stego)

# Mostrar mensaje si no hay más archivos DOCX
if not archivos_docx:
    print("No hay más archivos DOCX disponibles para aplicar esteganografía.")

# Imprimir los archivos PDF con esteganografía
print("Archivos PDF con esteganografía en la carpeta:", ruta_salida)
for archivo in archivos_stego:
    print(archivo)