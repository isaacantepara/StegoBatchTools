import os
import sys
from docx import Document

def extract_images_from_docx(docx_path):
    doc = Document(docx_path)
    image_count = 0

    for rel in doc.part.rels.values():
        if "image" in rel.target_part.content_type:
            image_data = rel.target_part.blob
            image_filename = f'img{image_count}.jpeg'
            
            with open(image_filename, 'wb') as f:
                f.write(image_data)
            
            print(f"Imagen guardada: {image_filename}")
            image_count += 1

    print(f"Se han extraído {image_count} imágenes.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <ruta_de_docx>")
        sys.exit(1)

    docx_path = sys.argv[1]

    if not docx_path.endswith(".docx"):
        print("Error al procesar")
        sys.exit(1)
    
    extract_images_from_docx(docx_path)