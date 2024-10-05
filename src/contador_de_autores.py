import pandas as pd
from docx import Document
import os

# Ruta al archivo Excel
excel_file = "../data/password/empleado_del_mes.xlsx"

# Ruta a la carpeta con los archivos DOCX
docx_folder = "../pendriver/informes"

# Nombre del archivo de salida
output_file = "../pendriver/empleado_del_mes.xlsx"

# Cargar el DataFrame desde el archivo Excel
df = pd.read_excel(excel_file)

# Crear una copia del DataFrame para evitar modificar el original
df_updated = df.copy()

# Iterar sobre cada archivo DOCX en la carpeta
for filename in os.listdir(docx_folder):
    if filename.endswith(".docx"):
        # Construir la ruta completa al archivo DOCX
        file_path = os.path.join(docx_folder, filename)

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
df_updated.to_excel(output_file, index=False)