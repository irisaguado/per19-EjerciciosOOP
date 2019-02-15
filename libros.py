class Libro():
    def __init__(self, titulo, dia_prestamo, mes_prestamo):
        self.titulo = titulo
        self.dia_prestamo = dia_prestamo
        self.mes_prestamo = mes_prestamo

    def prestamo(self):
        return self.dia_prestamo, self.mes_prestamo

    def devolucion(self):
        mes_devolucion = self.mes_prestamo + 1
        if mes_devolucion > 12:
            mes_devolucion -= 12
        return self.dia_prestamo, mes_devolucion


l = Libro('Don Quijote de la Mancha', 14, 12)
print('El libro',l.titulo, 'fue prestado el',l.prestamo())
print('Debes devolver el libro el', l.devolucion())
