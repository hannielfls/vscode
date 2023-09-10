# Solicita ao usuário os três lados do triângulo
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

# Verifica se os lados podem formar um triângulo
if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
    # Verifica o tipo de triângulo
    if lado1 == lado2 == lado3:
        print("O triângulo é equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo é isósceles")
    else:
        print("O triângulo é escaleno")
else:
    print("Os valores informados não podem formar um triângulo")