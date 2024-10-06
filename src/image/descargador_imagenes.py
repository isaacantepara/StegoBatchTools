import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import sys

# Lista de animales
animales = [
    'Lion', 'Asian Elephant', 'Giraffe', 'Tiger', 'Giant Panda',
    'Grevy\'s Zebra', 'Red Kangaroo', 'Hippopotamus', 'White Rhinoceros',
    'Bornean Orangutan', 'Nile Crocodile', 'American Flamingo', 'Emperor Penguin',
    'RedFox', 'Gray Wolf', 'Brown Bear', 'Burmese Python',
    'River Otter', 'Puma', 'Eagle Owl', 'Kestrel', 'Western Gorilla', 
    'Common Chimpanzee', 'Ring-tailed Lemur', 'Capuchin Monkey', 'Koala', 
    'Bottlenose Dolphin', 'Humpback Whale', 'Great White Shark', 
    'Loggerhead Sea Turtle', 'Boa Constrictor', 'Goanna', 'Green Iguana', 
    'Bullfrog', 'Common Toad', 'Monarch Butterfly', 'Honey Bee', 
    'Silkworm', 'Dung Beetle', 'Woodpecker', 'Bald Eagle', 
    'Peregrine Falcon', 'Herring Gull', 'Canada Goose', 'Mute Swan', 
    'Common Quail', 'Rock Dove', 'Indian Peafowl', 'Common Pheasant',
    'Domestic Dog', 'Domestic Cat', 'European Rabbit', 'Horse', 
    'Domestic Pig', 'Sheep', 'Goat', 'Donkey', 'Dromedary Camel',
    'Northern Elephant Seal', 'Harbor Seal', 'West Indian Manatee', 
    'Beaver', 'Gray Squirrel', 'House Mouse', 'European Hedgehog', 
    'Bat', 'Anna\'s Hummingbird', 'African Grey Parrot', 
    'Blue-and-yellow Macaw', 'Domestic Canary', 'Crayfish', 
    'American Lobster', 'Common Octopus', 'Giant Squid',
    'Jellyfish', 'Starfish', 'Goldfish', 'Hammerhead Shark',
    'Blue Whale', 'Bottlenose Dolphin', 'Seahorse', 'Red Coral',
    'Green Algae', 'Plankton', 'Bacteria', 'Mushroom',
    'Houseplant', 'Oak Tree', 'Rose'
]

# Configuración de Selenium en modo headless (sin abrir navegador)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ejecutar sin abrir la ventana del navegador
chrome_options.add_argument("--disable-gpu")  # Deshabilitar GPU para sistemas Windows
chrome_options.add_argument("--no-sandbox")  # Necesario para algunos entornos de CI
chrome_options.add_argument("--disable-dev-shm-usage")  # Evitar problemas de memoria en contenedores

# Ruta al chromedriver
webdriver_service = Service("./chromedriver")

# Función para descargar imagen de iNaturalist
def descargar_imagen(animal, carpeta_imagenes):
    try:
        # Navegar a iNaturalist y buscar el animal
        driver.get(f"https://ecuador.inaturalist.org/taxa/{animal}")

        # Obtener la primera imagen en la página
        imagen_elemento = driver.find_element(By.CSS_SELECTOR, ".photo-bg")
        style_attribute = imagen_elemento.get_attribute("style")

        # Extraer la URL de la imagen
        imagen_url = style_attribute.split("url(\"")[1].split("\");")[0]  
         # Reemplazar "small.jpg" o "small.jpeg" por "original.jpg"
        imagen_url_original = imagen_url.replace("small.jpg", "original.jpg") 
        imagen_url_original = imagen_url_original.replace("small.jpeg", "original.jpeg")# Reemplazar "small.jpg" por "original.jpg"

        # Descargar la imagen
        respuesta = requests.get(imagen_url_original)
        if respuesta.status_code == 200:
            # Guardar la imagen en la carpeta 'imagenes_animales'
            ruta_imagen = os.path.join(carpeta_imagenes, f"{animal.replace(' ', '_')}.jpg")
            with open(ruta_imagen, "wb") as archivo_imagen:
                archivo_imagen.write(respuesta.content)
            print(f"Imagen de {animal} descargada con éxito.")
        else:
            print(f"Error al descargar la imagen de {animal}.")
    except Exception as e:
        print(f"No se pudo descargar la imagen de {animal}: {e}")

# Obtener la carpeta desde los argumentos
if len(sys.argv) > 1:
    carpeta_imagenes = sys.argv[1] 
else:
    print("Debes proporcionar la ruta de la carpeta como argumento.")
    sys.exit(1)

# Validar que la carpeta existe
if not os.path.exists(carpeta_imagenes):
    print("La carpeta no existe. Por favor, ingresa una ruta válida.")
else:
    # Crear el directorio para almacenar las imágenes si no existe
    os.makedirs(carpeta_imagenes, exist_ok=True)

    # Inicializar el controlador de Chrome
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    # Descargar imágenes de todos los animales
    for animal in animales:
        descargar_imagen(animal, carpeta_imagenes)
        sleep(3)  # Espera 3 segundos antes de pasar al siguiente animal

    # Cerrar el navegador
    driver.quit()