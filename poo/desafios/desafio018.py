from rich import print
from rich.panel import Panel
from rich.traceback import install

install()

class Churrasco:
    """
    Cria um churrasco e tem cmo entrada  nome e o umero de pessoas e tem o metodode analisar e retornar a quantidade de carne nescessaria em kg e o custo com base no numero de pessoas
    """

    def __init__(self, nome=str, quant=int):
        self.nome = nome
        self.quant = quant

    def analisar(self):
        # Calculo da quantidade em Kg de carne nescessaria
        carN = self.quant * 0.4
        # Calculo do dinheiro nescessario
        din_N = carN * 82.40
        din_P = din_N / self.quant

        resul = Panel(f"Analisando o [green]{self.nome}[/] com [cyan]{self.quant} convidados[/] \n Cada participante comerá 0,4Kg e cada Kg custa R$82,40 \nRecomendo [cyan]recomendo comprar {carN:,.2f}Kg[/] de carne \nO custo total será de [green]R${din_N:,.2f}[/] \nCada pessoa pagará [yellow]R${din_P:,.2f} para participar [/]", title=self.nome)

        print(resul)

chu1 = Churrasco("Jai morreu!!!!!", 12)

chu1.analisar()