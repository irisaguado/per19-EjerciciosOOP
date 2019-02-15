class Contador():
    def __init__(self, num):
        self.num = num

    def incrementar(self, cantidad):
        self.num = self.num + cantidad
        return self.num

    def disminuir(self, cantidad):
        self.num = self.num - cantidad
        return self.num

c1 = Contador(5)
print('El contador marca:', c1.incrementar(2))
print('El contador marca:', c1.disminuir(4))




class Contador1():
    def __init__(self, num = None):
        self.num = num
        if num is None:
            self.num = 0
        else:
            self.num

    def incrementar(self, cantidad):
        self.num = self.num + cantidad
        return self.num

    def disminuir(self, cantidad):
        self.num = self.num - cantidad
        return self.num

c2 = Contador1()
print('El contador1 marca:', c2.incrementar(9))
print('El contador1 marca:', c2.disminuir(4))
