from rich import print
from rich.table import Table

tabela = Table(title="Tabela de preços")

tabela.add_column("Nome", style="red")
tabela.add_column("Valor", style="blue")

tabela.add_row("Lápis", "1.50")
tabela.add_row("Borracha", "4.0")
tabela.add_row("Grafite", "5.5")
print(tabela)