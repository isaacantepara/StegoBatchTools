# oculto

### Metadata DOCX

- exiftool file.docx

### codificacion/decodificar por carpeta

- python  codificarM_img.py <ruta_carpeta_imagenes> <ruta_carpeta_salida>
- python decodificarM_img.py <ruta_carpeta_codificada> <ruta_carpeta_decodificada>

### decodicicar un archivo

- python3 oneDeleteRuido.py file.null

### linux

- steghide (estenografia solo imagenes jpg y jpeg)

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
