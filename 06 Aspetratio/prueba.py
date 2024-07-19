import math

# Resolución de pantalla
width = 1920
height = 1080

# Calcular el máximo común divisor
gcd = math.gcd(width, height)

# Calcular la proporción más simple
aspect_ratio_width = width // gcd
aspect_ratio_height = height // gcd

print(f"La proporción es {aspect_ratio_width}:{aspect_ratio_height}")