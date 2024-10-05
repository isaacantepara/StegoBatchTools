from docx import Document

def extraer_archivo_bin_de_docx(ruta_archivo_docx):
    """
    Extrae el archivo binario oculto en un archivo DOCX.

    Args:
        ruta_archivo_docx (str): La ruta al archivo DOCX.

    Returns:
        bytes: El archivo binario extraído.
    """

    documento = Document(ruta_archivo_docx)

    informacion_oculta = []
    for parrafo in documento.paragraphs:
        for run in parrafo.runs:
            # Obtener el tamaño de fuente en puntos por carácter
            tamanio_fuente = run.font.ptc
            # Calcular el espacio entre caracteres (aproximación)
            espacio_entre_caracteres = tamanio_fuente / 1000  # Suponiendo que 1 punto equivale a 1000 unidades de espacio
            # Convertir el espacio entre caracteres a binario
            binario = bin(int(espacio_entre_caracteres))[2:].zfill(8)
            informacion_oculta.extend(binario[-3:])

    # Combinar los bits para formar bloques de bytes
    bloques_bytes = [informacion_oculta[i:i+8] for i in range(0, len(informacion_oculta), 8)]
    # Convertir cada bloque de bytes a su valor original
    datos_extraidos = bytes([int(bloque, 2) for bloque in bloques_bytes])

    return datos_extraidos

# Ejemplo de uso
ruta_archivo_docx = "../pendriver/informes_stego/Informe_Brown_Bear_12_10bit.jpg.bin_stego.docx"
archivo_bin = extraer_archivo_bin_de_docx(ruta_archivo_docx)

# Guardar el archivo binario extraído
with open("archivo_extraido.bin", "wb") as f:
    f.write(archivo_bin)

print("Archivo binario extraído con éxito.")