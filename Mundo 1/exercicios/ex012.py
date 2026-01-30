preço = float(input("Qual é o preço do produto? R$"))

desconto = float(input("Quantos % de desconto?: "))/100

preço_des = preço*(1-desconto)

print(f"O produto que custava R${preço:,.2f} na promoção de {desconto*100:,.2f}% vai custar R${preço_des:,.2f}")