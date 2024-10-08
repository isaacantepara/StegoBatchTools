import os
import zipfile
import sys

def zip_directories_in_folder(input_folder, output_folder):
    # Verifica si el directorio de origen existe
    if not os.path.isdir(input_folder):
        print(f"El directorio '{input_folder}' no existe.")
        return

    # Crea la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Recorre todas las carpetas dentro del directorio de origen
    for root, dirs, files in os.walk(input_folder):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            zip_filename = os.path.join(output_folder, f"{dir_name}.zip")
            
            # Crear archivo zip para la carpeta
            with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
                # Recorre todos los archivos dentro de la carpeta
                for folder_root, _, folder_files in os.walk(dir_path):
                    for file in folder_files:
                        file_path = os.path.join(folder_root, file)
                        # Agrega los archivos al zip, preservando la estructura
                        zipf.write(file_path, os.path.relpath(file_path, dir_path))
            
            print(f"Carpeta '{dir_name}' comprimida en '{zip_filename}'.")

if __name__ == "__main__":
    # Verifica si se han pasado los argumentos necesarios
    if len(sys.argv) != 3:
        print("Uso: python3 script.py ruta_con_todas_las_carpetas ruta_de_carpeta_zip_salida")
        sys.exit(1)

    # Obtén los argumentos de la línea de comandos
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    # Ejecuta el algoritmo
    zip_directories_in_folder(input_folder, output_folder)
