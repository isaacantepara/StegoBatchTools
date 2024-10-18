# oculto
pyhton3 descargarM_img_docx.py descargarM_img_docx.py //se descarga todas las imagenes en el directorio actual
![Screenshot_20241018_181304](https://github.com/user-attachments/assets/078f8e19-e43e-4d30-acd3-2e5ddb8b141b)
![Screenshot_20241018_181744](https://github.com/user-attachments/assets/408a737f-3628-4353-91cf-87f6dbf61ab4)
![Screenshot_20241018_181858](https://github.com/user-attachments/assets/1752faed-58f9-4e82-89eb-386530f984c7)


### Generar markdown

- python3 script.py ruta_salida cantidad_archivos
- └─$ python3 generador_markdown.py /home/pythonesso/Documents/zoo/pendriver/md 2

### Comprension masiva carpetas a zips

- script.py ruta_con_todas_las_carpetas ruta_de_carpeta_zip_salida
- └─$ python3 compresionM_zip.py /home/pythonesso/Documents/zoo/pendriver/md /home/pythonesso/Documents/zoo/pendriver/zips

### Stegografia masiva de zips

- ./stegoM.sh /home/pythonesso/Documents/zoo/pendriver/zips /home/pythonesso/Documents/zoo/pendriver/imagenes


### Generar informes

- └─$ python3 generar_informes.py  ruta_carpeta

### Metadata DOCX

- └─$ python3 cambiar_metadata_docx.py /home/pythonesso/Documents/zoo/pendriver/informes /home/pythonesso/Documents/zoo/data/password/animales_capturados.xlsx  (CAMBIAR METADATA)
- exiftool file.docx

### Contador de autores

- contador_autores.py <arpeta con los archivos DOCX> <carpeta donde se guardará el archivo Excel>
- python3 contador_autores.py /home/pythonesso/Documents/zoo/pendriver/informes /home/pythonesso/Documents/zoo/pendriver

### codificacion/decodificar por carpeta

- python  codificarM_img.py <ruta_carpeta_imagenes> <ruta_carpeta_salida> <isfolder>
- └─$ python  codificarM_img.py /home/pythonesso/Documents/zoo/pendriver/imagenes /home/pythonesso/Documents/zoo/pendriver/c -y

- python decodificarM_img.py <ruta_carpeta_codificada> <ruta_carpeta_decodificada>

### decodicicar un archivo

- python3 oneDeleteRuido.py file.null

### descargar imagenes de un docx

- └─$ python3 descargarM_img_docx.py ruta_file.docx

### ofuscación

- └─$ pyarmor gen -O output_folder file.py **SEGURIDAD ALTA**
    - Te da como resultado una carpta en el cual la necesitas para ejecutar ese scirp, pero no necesitas instalar dependencias ya que todo esta ahi
    - es dificil de decifrar el script aun para un experto
    - necesitas llevar la carpeta de salida a cualquier lugar si quieres ejecutar el script su ejecucion es:
        - > python script.py (si estas dentro del directorio, su no pones toda la ruta)
- └─$ python -m compileall file.py (creacion de .pyc) **SEGURIDAD BAJA**
    - lo que hace es compilar el script / descompilar( https://pylingual.io/ )
    - te da como resulta un carpeta __pycache__ en donde se encuentra el script.py que quieres hacer ofuscacion
    - dentro de esa carpeta hay un arhvio .cpython-312.pyc, los numero son la version de py
    - la razon por la que te da la version de py esporque la necesitas para poder ejecutar el pyc en esa version,
    ya que ese pyc contien todas las dependencias
    - la ejecucion del script.cpython-312.pyc es:
        - > python3 script.cpython-312.pyc

### stegografia (linux)

- steghide embed -ef /home/pythonesso/Documents/decode_.zip -cf /home/pythonesso/Documents/zoo/pendriver/imagenes/River_Otter.jpeg  -sf stegohideResultZip.jpeg
    - la imagen tiene que 4 veces mas grande que el zip porque
- steghide extract -sf stegohideResultZip.jpeg 
