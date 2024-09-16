import math

def calcular_area():
    print("Escolha a forma geométrica:")
    print("1. Retângulo")
    print("2. Triângulo")
    print("3. Círculo")
    escolha = input("Digite o número da forma: ")

    if escolha == "1":
        base = float(input("Digite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        area = base * altura
        print("A área do retângulo é:", area)

    elif escolha == "2":
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        area = (base * altura) / 2
        print("A área do triângulo é:", area)

    elif escolha == "3":
        raio = float(input("Digite o raio do círculo: "))
        area = math.pi * raio * raio
        print("A área do círculo é:", area)

    else:
        print("Opção inválida!")

# Chama diretamente a função sem a necessidade de "main"
calcular_area()
