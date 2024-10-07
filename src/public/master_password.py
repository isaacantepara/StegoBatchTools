import pandas as pd
import os
from cryptography.fernet import Fernet

def codeaes256(ruta_archivo):
    try:
        df = pd.read_excel(ruta_archivo)

        # Verificar si el archivo contiene las columnas 'name' y 'score'
        if 'name' in df.columns and 'score' in df.columns:

            # Concatenar los puntajes en un solo string
            puntajes_string = ''.join(str(x) for x in df['score'].tolist())

            # Generar una clave aleatoria y cifrar el string
            key = Fernet.generate_key()
            f = Fernet(key)
            cifrado = f.encrypt(puntajes_string.encode())

            # Guardar la clave cifrada en un archivo .txt
            with open("password.txt", "wb") as file:
                file.write(key)

            print("Clave cifrada guardada.")

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
        codeaes256(ruta_archivo)