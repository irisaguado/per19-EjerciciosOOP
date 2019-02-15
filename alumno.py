class Alumno():
    def __init__(self, matricula, nombre, nota1, nota2, nota3):
        self.matricula = matricula
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def get_matricula(self):
        return self.matricula

    def get_nombre(self):
        return self.nombre

    def get_notafinal(self):
        nota_final = round((self.nota1 + self.nota2 + self.nota3)/3,2)
        return nota_final

    def aprobado(self,nota_final):
        if nota_final >= 4.8:
            return '¡¡El alumno ha aprobado!!'
        else:
            return 'El alumno ha suspendido'


alumno1 = Alumno(45, 'Juan', 5, 8, 7)
print('El alumno', alumno1.get_nombre(), 'con nº de matricula', alumno1.get_matricula(), ', tiene una nota final de', alumno1.get_notafinal())
print(alumno1.aprobado(alumno1.get_notafinal()))
