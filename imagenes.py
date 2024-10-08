import requests
from bs4 import BeautifulSoup
import os
from PIL import Image
from io import BytesIO
import time

output_dir = "/media/pythonesso/G6-OCULTO"
os.makedirs(output_dir, exist_ok=True)

animales = [
    ('León', 'Lion'),
    ('Elefante Asiático', 'Asian Elephant'),
    ('Jirafa', 'Giraffe'),
    ('Tigre', 'Tiger'),
    ('Panda Gigante', 'Giant Panda'),
    ('Cebra de Grevy', 'Grevy\'s Zebra'),
    ('Canguro Rojo', 'Red Kangaroo'),
    ('Hipopótamo', 'Hippopotamus'),
    ('Rinoceronte Blanco', 'White Rhinoceros'),
    ('Orangután de Borneo', 'Bornean Orangutan'),
    ('Cocodrilo del Nilo', 'Nile Crocodile'),
    ('Flamenco Americano', 'American Flamingo'),
    ('Pingüino Emperador', 'Emperor Penguin'),
    ('Zorro Rojo', 'Red Fox'),
    ('Lobo Gris', 'Gray Wolf'),
    ('Oso Pardo', 'Brown Bear'),
    ('Pitón Birmana', 'Burmese Python'),
    ('Nutria de Río', 'River Otter'),
    ('Puma', 'Puma'),
    ('Búho Real', 'Eagle Owl'),
    ('Cernícalo', 'Kestrel'),
    ('Gorila Occidental', 'Western Gorilla'),
    ('Chimpancé Común', 'Common Chimpanzee'),
    ('Lémur de Cola Anillada', 'Ring-tailed Lemur'),
    ('Mono Capuchino', 'Capuchin Monkey'),
    ('Koala', 'Koala'),
    ('Delfín Mular', 'Bottlenose Dolphin'),
    ('Ballena Jorobada', 'Humpback Whale'),
    ('Tiburón Blanco', 'Great White Shark'),
    ('Tortuga Boba', 'Loggerhead Sea Turtle'),
    ('Boa Constrictora', 'Boa Constrictor'),
    ('Goanna', 'Goanna'),
    ('Iguana Verde', 'Green Iguana'),
    ('Rana Toro', 'Bullfrog'),
    ('Sapo Común', 'Common Toad'),
    ('Mariposa Monarca', 'Monarch Butterfly'),
    ('Abeja', 'Honey Bee'),
    ('Gusano de Seda', 'Silkworm'),
    ('Escarabajo Pelotero', 'Dung Beetle'),
    ('Pájaro Carpintero', 'Woodpecker'),
    ('Águila Calva', 'Bald Eagle'),
    ('Halcón Peregrino', 'Peregrine Falcon'),
    ('Gaviota', 'Herring Gull'),
    ('Ganso Canadiense', 'Canada Goose'),
    ('Cisne Mudo', 'Mute Swan'),
    ('Codorniz Común', 'Common Quail'),
    ('Paloma Bravía', 'Rock Dove'),
    ('Pavo Real', 'Indian Peafowl'),
    ('Faisán Común', 'Common Pheasant'),
    ('Perro Doméstico', 'Domestic Dog'),
    ('Gato Doméstico', 'Domestic Cat'),
    ('Conejo Europeo', 'European Rabbit'),
    ('Caballo', 'Horse'),
    ('Cerdo Doméstico', 'Domestic Pig'),
    ('Oveja', 'Sheep'),
    ('Cabra', 'Goat'),
    ('Burro', 'Donkey'),
    ('Camello Dromedario', 'Dromedary Camel'),
    ('Foca Elefante del Norte', 'Northern Elephant Seal'),
    ('Foca Común', 'Harbor Seal'),
    ('Manatí del Caribe', 'West Indian Manatee'),
    ('Castor', 'Beaver'),
    ('Ardilla Gris', 'Gray Squirrel'),
    ('Ratón Casero', 'House Mouse'),
    ('Erizo Europeo', 'European Hedgehog'),
    ('Murciélago', 'Bat'),
    ('Colibrí de Ana', 'Anna\'s Hummingbird'),
    ('Loro Gris Africano', 'African Grey Parrot'),
    ('Guacamayo Azul y Amarillo', 'Blue-and-yellow Macaw'),
    ('Canario Doméstico', 'Domestic Canary'),
    ('Cangrejo de Río', 'Crayfish'),
    ('Langosta Americana', 'American Lobster'),
    ('Pulpo Común', 'Common Octopus'),
    ('Calamar Gigante', 'Giant Squid'),
    ('Medusa', 'Jellyfish'),
    ('Estrella de Mar', 'Starfish'),
    ('Pez Dorado', 'Goldfish'),
    ('Tiburón Martillo', 'Hammerhead Shark'),
    ('Ballena Azul', 'Blue Whale'),
    ('Caballito de Mar', 'Seahorse'),
    ('Coral Rojo', 'Red Coral'),
    ('Alga Verde', 'Green Algae'),
    ('Plancton', 'Plankton'),
    ('Bacteria', 'Bacteria'),
    ('Seta', 'Mushroom'),
    ('Planta de Interior', 'Houseplant'),
    ('Roble', 'Oak Tree'),
    ('Rosa', 'Rose')
]

def is_image_valid(image_data):
    try:
        size_in_mb = len(image_data) / (1024 * 1024)  
        if size_in_mb == 0:
            print(f"Tamaño de archivo {size_in_mb:.2f}MB es inválido")
            return False

        image = Image.open(BytesIO(image_data))
        image.verify()  
        image = Image.open(BytesIO(image_data))  
        return True
    except Exception as e:
        print(f"Error al verificar la imagen: {e}")
        return False

def download_image(url, file_name):
    try:
        img_data = requests.get(url, timeout=10).content
        if is_image_valid(img_data):
            with open(file_name, 'wb') as handler:
                handler.write(img_data)
            print(f"Imagen guardada como {file_name}")
        else:
            print(f"La imagen de {file_name} no cumple los criterios o está corrupta.")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la imagen {file_name}: {e}")

def search_bing(animal, idioma, retries=3, num_results=10):
    search_url = f"https://www.bing.com/images/search?q={animal.replace(' ', '+')}&qft=+filterui:imagesize-large&form=HDRSC2"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    for attempt in range(retries):
        try:
            response = requests.get(search_url, headers=headers, timeout=10)
            response.raise_for_status() 
            soup = BeautifulSoup(response.text, 'html.parser')

            image_tags = soup.find_all('a', class_='iusc', limit=num_results)  
            if image_tags:
                for i, image_tag in enumerate(image_tags):
                    m = image_tag.get('m')
                    if m:
                        try:
                            image_url = m.split('"murl":"')[1].split('"')[0]
                            file_name = os.path.join(output_dir, f"{animal.replace(' ', '_')}_{idioma}_{i}.jpg")
                            download_image(image_url, file_name)
                            return True
                        except IndexError:
                            print(f"No se pudo extraer la URL de la imagen para {animal}.")
            else:
                print(f"No se encontraron imágenes para {animal} en {idioma}.")
        except requests.exceptions.RequestException as e:
            print(f"Error al buscar imágenes de {animal}: {e}")
            if attempt < retries - 1:
                print(f"Reintentando... (Intento {attempt + 1}/{retries})")
                time.sleep(2)  
            else:
                print(f"Error definitivo al buscar imágenes de {animal} en {idioma}")
    return False

for animal_es, animal_en in animales:
    print(f"Buscando imágenes de {animal_es}...")
    if not search_bing(animal_es, 'es'):  
        print(f"No se encontraron imágenes adecuadas para {animal_es}. Intentando en inglés...")
        search_bing(animal_en, 'en')  
    time.sleep(1)  
