from rich import print
from rich.panel import Panel

# Criação da classe Produto

class Produto:
    """
    Cria um produto, que recebe nome e preço e pode mostar a etiqueta
    """

    def __init__(self, nome=str, preco=float):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):

        etiq = Panel(f"{self.nome} \n {self.preco:,.2f}", title=self.nome, width=50)
        print(etiq)

p1 = Produto("Iphone", 10)

p1.etiqueta()