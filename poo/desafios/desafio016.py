from rich import print

class Funcionario:
    """
    Criar uma funcionario com o setor, nome e fa com que ele se apresente
    """

    def __init__(self, nome=str, setor=str):
        self.nome = nome
        self.setor = setor

    def Apresentar(self):
        print(f"Meu nome é [blue]{self.nome}[/] e trabalho no [red] {self.setor} [/]")
    
f1 = Funcionario("Claudia", "Finaceiro")

f1.Apresentar()