from math import sqrt

print("Bem-vinde ao Contas de Segundo Grau Resolutor. \n O formato da equação é Ax²+Bx+C")
while True:
    ValorA = int(input("Digite o A"))
    ValorB = int(input("Digite o B"))
    ValorC = int(input("Digite o C"))

    Delta = (ValorB ** 2) - (4 * ValorA * ValorC)
    print(f"O Delta da equação é {Delta}.")

    if Delta < 0:
        print("O delta deu negativo! Como você sabe, não há resultados reais para essa equação!")
    else:
        resultado1 = (-ValorB + sqrt(Delta)) / (2 * ValorA)
        resultado2 = (-ValorB - sqrt(Delta)) / (2 * ValorA)
        print(f"As raízes são {resultado1} e {resultado2}.")
    repeticao = input("Deseja solucionar outra equação? (Digite sim ou nao)")
    if repeticao == "nao":
        print("Obrigada por usar o Contas de Segundo Grau Resolutor! Volte sempre.")
        break
    elif repeticao != "sim":
        print('Buguei!')
        repeticao = input("Deseja solucionar outra equação? (Digite sim ou nao)")
