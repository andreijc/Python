class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saque e depositos
    """

    def __init__(self, id=int, titular = str, saldo = 0):
        self.id = id
        self.titular = titular
        self.saldo = saldo
        print(f"Conta {self.id} criada com suceso. Saldo atual de R${self.id:,.2f}")

    def __str__(self):
        return f"A conte {self.id} de {self.titular} tem R${self.saldo:.2f}"
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de {valor:.2f} autorizado na conta {self.id}")


    def sacar(self, valor=float):
        if valor > self.saldo:
            print(f"Saque de R${valor:,.2f} Negado na conta {self.id}")
        else:
            self.saldo -= valor
            print(f"Saque de {valor:,.2f} autorizado na conta {self.id}")


c1 = ContaBancaria(112, "Gustavo", 3000)
c1.depositar(500)
c1.sacar(2_000_000)

print(c1)