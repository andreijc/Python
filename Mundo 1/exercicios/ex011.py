# Cada 2 m² precisa de 1L de tinta

largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))

area_parede = largura*altura

print(f"Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area_parede}\n Para pintar essa parede, você precisará de {area_parede/2}")