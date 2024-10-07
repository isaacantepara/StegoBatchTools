import pandas as pd
import os
import hashlib

def hash256(ruta_archivo):
    try:
        df = pd.read_excel(ruta_archivo)

        # Verificar si el archivo contiene las columnas 'name' y 'score'
        if 'name' in df.columns and 'score' in df.columns:

            # Concatenar los puntajes en un solo string
            puntajes_string = ''.join(str(x) for x in df['score'].tolist())

            # Calcular el hash SHA256 del string
            hash_object = hashlib.sha256(puntajes_string.encode())
            hash_hex = hash_object.hexdigest()

            # Guardar el hash en un archivo .txt
            with open("master_password.txt", "w") as file:
                file.write(hash_hex)

            print("calculado y guardado.")

    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no se encontró.")
    except pd.errors.EmptyDataError:
        print(f"El archivo {ruta_archivo} está vacío.")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        ruta_archivo = sys.argv[1]
        hash256(ruta_archivo)