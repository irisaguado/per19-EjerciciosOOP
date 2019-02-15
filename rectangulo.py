class Rectangulo():
    def __init__(self, base, altura):
         self.base = base
         self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        return area

    def calcular_perimetro(self):
        perimetro = self.base*2 + self.altura*2
        return perimetro

class PruebaRectangulo(Rectangulo):
    def __init__(self, base, altura):
        super().__init__(base, altura)

rectangulo1 = PruebaRectangulo(5,3)
print('El área del rectángulo1 es', rectangulo1.calcular_area(), 'y su perímetro es ', rectangulo1.calcular_perimetro())

rectangulo2 = PruebaRectangulo(8,2)
print('El área del rectángulo1 es', rectangulo2.calcular_area(), 'y su perímetro es ', rectangulo2.calcular_perimetro())
