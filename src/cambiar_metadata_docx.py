from docx import Document
from datetime import datetime
import os
import time
import random
import subprocess

def modificar_metadatos(archivo, autores):
 
    """Modifica los metadatos de un archivo DOCX."""
    doc = Document(archivo)
    print(archivo)

    # Elegir un autor aleatorio
    autor_seleccionado = random.choice(autores)
    line = autor_seleccionado.split(" ") 
    nombre_completo = f"{line[0]}_{line[1]}"

    # Convertir la cadena de texto a un objeto datetime
    anio = f"{line[-1][0]}{line[-1][1]}{line[-1][2]}{line[-1][3]}"
    target_datetime = datetime.strptime(f"{anio}:03:21 12:00:00", "%Y:%m:%d %H:%M:%S")


    # Establecer el autor en el documento
    doc.core_properties.author = nombre_completo

     # Establecer metadatos con el objeto datetime
    doc.core_properties.created = target_datetime
    doc.core_properties.modified = target_datetime

    doc.core_properties.description = "lil" 



    # Guardar los cambios
    doc.save(archivo)

    # Actualizar las fechas del archivo con el timestamp
    timestamp = int(time.mktime(target_datetime.timetuple()))
    os.utime(archivo, (timestamp, timestamp))

    # Modificar la fecha del nodo del archivo con exiftool
    '''subprocess.run(["exiftool",
                     "-FileInodeChangeDate=" + target_datetime.strftime("%Y:%m:%d %H:%M:%S"),
                     archivo])

    # Modificar la fecha de Zip Modify Date con exiftool
    subprocess.run(["exiftool",
                     "-ZipModifyDate=" + target_datetime.strftime("%Y:%m:%d %H:%M:%S"),
                     archivo])'''



# Leer la lista de autores desde el archivo txt
with open("../data/password/registros_captura.txt", "r") as f:
    autores = f.readlines()


# Carpeta con los archivos DOCX
carpeta_docx = "../mierda/informes_zoologico"  # Reemplaza con la ruta de tu carpeta

# Iterar sobre los archivos DOCX en la carpeta
for archivo in os.listdir(carpeta_docx):
    if archivo.endswith(".docx"):
        ruta_archivo = os.path.join(carpeta_docx, archivo)
        modificar_metadatos(ruta_archivo, autores)