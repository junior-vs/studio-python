print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativa = 5
rodada = 0
while(rodada <= total_de_tentativa):
    print("Tentativa {} de {}".format(rodada, total_de_tentativa))
    chute_str = input("Digite o seu número: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto

    if(acertou):
        print("Parabéns! Você acertou!")
        break
    else:
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")
    rodada = rodada + 1

print("Fim do jogo")