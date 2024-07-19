from PIL import Image
from urllib.request import urlopen, Request
from io import BytesIO
import math


def calcularProporcion(URL):
    # URL de la imagen
    imagenUrl = URL

    # Agregar un encabezado User-Agent a la solicitud
    req = Request(imagenUrl, headers={'User-Agent': 'Mozilla/5.0'})

    # Descargar la imagen
    u = urlopen(req)
    raw_data = u.read()
    u.close()

    # Abrir la imagen con PIL
    image = Image.open(BytesIO(raw_data))

    width , height = image.size

    gcd = math.gcd(width, height)

    # Calcular la proporción más simple
    aspect_ratio_width = width // gcd
    aspect_ratio_height = height // gcd

    print(image.size)
    print(f"La proporción es {aspect_ratio_width}:{aspect_ratio_height}")

#1:1
calcularProporcion("https://24ai.tech/es/wp-content/uploads/sites/5/2023/10/01_product_1_sdelat-izobrazhenie-1-1-2.jpg")
#16:9
calcularProporcion("https://images6.alphacoders.com/134/thumb-1920-1346530.jpeg")