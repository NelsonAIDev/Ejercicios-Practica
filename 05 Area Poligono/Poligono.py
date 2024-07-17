"""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
"""

class Polygon:
    def area(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def calcular_area(poligono):
    return poligono.area()


triangle = Triangle(base=5, height=10)
square = Square(side=4)
rectangle = Rectangle(width=3, height=7)

print(f"El área del triángulo es: {calcular_area(triangle)}")
print(f"El área del cuadrado es: {calcular_area(square)}")
print(f"El área del rectángulo es: {calcular_area(rectangle)}")