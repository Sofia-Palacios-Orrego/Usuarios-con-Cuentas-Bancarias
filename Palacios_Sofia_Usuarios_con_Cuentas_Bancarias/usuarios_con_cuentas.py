class CuentaBancaria:
    cuentas = [] 

    def __init__(self, tasa_interes, balance=0): 
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas.append(self)   

    def mostrar_info_cuenta(self):
        return f"${self.balance}"

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
            return self

    def generar_interes(self):
        if self.balance > 0:
            interes_generado = self.balance * self.tasa_interes
            self.balance += interes_generado
            return self
        
    @classmethod
    def imprimir_todas_las_cuentas(cls):
        for cuenta in cls.cuentas:        
            print("Cuenta Bancaria:")
            cuenta.mostrar_info_cuenta()
            print("Tasa de interés:", cuenta.tasa_interes)
            print("------------------------")


class Usuario:
    def __init__(self, name):
        self.name = name
        self.cuenta = {
            "cuenta_1" : CuentaBancaria(.02,1000),
            "cuenta_2" : CuentaBancaria(.05,3000)
        }

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, Cuenta 1 Balance: {self.cuenta['cuenta_1'].mostrar_info_cuenta()}")
        print(f"Usuario: {self.name}, Cuenta 2 Balance: {self.cuenta['cuenta_2'].mostrar_info_cuenta()}")
        return self

    def transfer_dinero(self, other_user, account_origin, account_destination, amount):
        self.cuenta[account_origin].retiro(amount)
        other_user.cuenta[account_destination].deposito(amount)
        return self



sofia = Usuario("Sofia")
sofia.cuenta['cuenta_1'].deposito(100)
sofia.cuenta['cuenta_2'].deposito(500)
sofia.mostrar_balance_usuario()


ana = Usuario("Ana")
ana.mostrar_balance_usuario()

sofia.transfer_dinero(ana, "cuenta_1", "cuenta_1", 200)
sofia.mostrar_balance_usuario()
ana.mostrar_balance_usuario()