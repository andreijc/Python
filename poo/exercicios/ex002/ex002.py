class Gafanhoto:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.

    Para criar uma nova pessoa, use
    variavel = Gafonhoto(nome, idade)
    """
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self):
        return f"{self.nome} é gafanhote e tem {self.idade} anos de idade"

    def __getstate__(self):
        return f"Estado: nome = {self.nome} e idade = {self.idade}"
g1 = Gafanhoto(nome="Maria", idade= 17)

print(g1)
g1.aniversario()
print(g1)
print(g1.__dict__)
print(g1.__getstate__())

print(g1.__class__)
