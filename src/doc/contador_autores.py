import pandas as pd
from docx import Document
import os
import argparse

def comparar_documentos(ruta_carpeta_docx, excel_file, ruta_carpeta_salida):
    """Compara los documentos DOCX en una carpeta con un archivo Excel y actualiza las puntuaciones."""

    # Cargar el DataFrame desde el archivo Excel
    df = pd.read_excel(excel_file)

    # Crear una copia del DataFrame para evitar modificar el original
    df_updated = df.copy()

    # Iterar sobre cada archivo DOCX en la carpeta
    for filename in os.listdir(ruta_carpeta_docx):
        if filename.endswith(".docx"):
            # Construir la ruta completa al archivo DOCX
            file_path = os.path.join(ruta_carpeta_docx, filename)

            # Abrir el archivo DOCX
            doc = Document(file_path)

            # Obtener el autor del archivo
            author = doc.core_properties.author

            # Buscar el autor en el DataFrame
            matching_rows = df_updated[df_updated["name"] == author]

            # Si se encuentra el autor, aumentar su puntuación
            if not matching_rows.empty:
                df_updated.loc[df_updated["name"] == author, "score"] += 1

    # Guardar el DataFrame actualizado en un nuevo archivo Excel
    nombre_archivo_salida = "empleado_del_mes.xlsx"  # Nombre del archivo de salida
    ruta_completa_salida = os.path.join(ruta_carpeta_salida, nombre_archivo_salida)
    df_updated.to_excel(ruta_completa_salida, index=False)

if __name__ == "__main__":
    # Definir los argumentos del comando
    parser = argparse.ArgumentParser(description="Comparar documentos DOCX con un archivo Excel.")
    parser.add_argument("ruta_carpeta_docx", help="Ruta a la carpeta con los archivos DOCX")
    parser.add_argument("ruta_carpeta_salida", help="Ruta de la carpeta donde se guardará el archivo Excel")
    args = parser.parse_args()

    # Ruta al archivo Excel
    excel_file = "/home/pythonesso/Documents/zoo/data/password/empleado_del_mes.xlsx"

    # Ejecutar la función de comparación
    comparar_documentos(args.ruta_carpeta_docx, excel_file, args.ruta_carpeta_salida)