class Cuenta():
    def __init__(self, n_cuenta, saldo_dispo):
        self.n_cuenta = n_cuenta
        self.saldo_dispo = saldo_dispo

    def ingresos(self, ingreso):
        self.saldo_dispo += ingreso
        return self.saldo_dispo

    def transferencias(self, transferencia):
        self.saldo_dispo -= transferencia
        if self.saldo_dispo < 0:
            print('Tras la transferencia estás en números rojos!!')
        return self.saldo_dispo

c1 = Cuenta(458963, 700)
print('Tu saldo despues de la transferencia es de', c1.transferencias(800),'euros')
print('Después del ingreso tu saldo es de',c1.ingresos(500), 'euros')
