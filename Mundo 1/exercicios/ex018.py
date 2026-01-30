from math import cos, sin, tan, radians

ang = float(input("Digite um ângulo que deseja: "))
rad = radians(ang)

print(f"O ângulo de {ang} tem o SENO de {sin(rad):.2f} \nO ângulo de {ang} tem como COSSENO de {cos(rad):.2f} \nO ângulo de {ang} tem a TANGENTE de {tan(rad):.2f}")