import random

print("------------------------------------------------------------------------------")
print("                   Seja bem-vindo ao Jogo da Advinhação!!                     ")
print()
print(" Nesse jogo, você vai precisar advinhar o número secreto entre [1000 e 9999]. ")
print("          A partir da 5ª tentativa, o jogo vai te ajudar com dicas.           ")
print("------------------------------------------------------------------------------")
print()
input("<Aperte ENTER>".rjust(43))

jogar = 1
while jogar == 1:

    print()
    print("O JOGO COMEÇOU")

    codigoSecreto = random.randint(1000,9999)
    
    for contTentativa in range(1,11):
        print()

        print(f"--{contTentativa}ª TENTATIVA--".rjust(44))
        codigoTentativa = int(input("Digite sua tentativa: "))

        while 1000 > codigoTentativa or codigoTentativa > 9999:
            print("ERRO: Você inseriu um número inválido!")
            codigoTentativa=int(input("Digite novamente um número de quatro digitos: "))
        print()

        

        nDigitosCertos = 0

        print("Seu código é:", end=" ")
        for x in range(3,-1,-1):

            nCodigoTentativa = (codigoTentativa % (10**(x+1))) // 10**x             
            nCodigoSecreto = (codigoSecreto % (10**(x+1))) // 10**x

            if nCodigoTentativa == nCodigoSecreto: 
                print(nCodigoTentativa, end=' ')
                nDigitosCertos += 1
            else:
                print("_", end=" ")
        print()

        if nDigitosCertos > 0:
            print(f"Você acertou {nDigitosCertos} digitos nessa tentativa")
        else:
            print("Você não acertou nenhum digito nessa tentativa")
        print()

        if codigoSecreto == codigoTentativa:
                    print("PARABÉNS, você acertou o código!!!")
                    print(f"O código era: {codigoSecreto}")
                    print(f"Você acertou o código em: {contTentativa} tentativas")
                    print()
                    break
        
        if contTentativa == 10 and codigoTentativa != codigoSecreto:
            print("Número de tentativas excedidas :( ") 
            print("VOCÊ NÃO CONSEGEGIU ACERTAR.")
            print(f"O código era: {codigoSecreto}")
            break

        if contTentativa >= 5:
            print("Aqui vai uma dica:", end=" ")

            dicaEnviada = 0
            while dicaEnviada == 0:

                posicaoDica = random.randint(1,4)
                nCodigoTentativa = (codigoTentativa % (10**(posicaoDica))) // 10**(posicaoDica-1) 
                nCodigoSecreto = (codigoSecreto % (10**(posicaoDica))) // 10**(posicaoDica-1)

                if nCodigoTentativa != nCodigoSecreto:

                    tipoDica = random.randint(1,3)
                    dicaEnviada = 1

                    if tipoDica == 1:
                        if nCodigoSecreto % 2 == 0:
                            print(f"O {5-posicaoDica}° número é Par")
                            dica = "PAR"
                        else:
                            print(f"O {5-posicaoDica}° número é Ímpar")
                            dica = "ÍMPAR"

                    elif tipoDica == 2:
                        if nCodigoSecreto >= 5:
                            print(f"O {5-posicaoDica}° número é maior ou igual a 5")
                            dica = "(>=5)"
                        else:
                            print(f"O {5-posicaoDica}° número é menor que 5")
                            dica = "(<5)"

                    elif tipoDica == 3:
                        for x in range(3,-1,-1):
                            nCodigoTentativa = (codigoTentativa % (10**(x+1))) // 10**x 
                            if nCodigoTentativa == nCodigoSecreto:

                                print(f"Algum digito da sua tentativa se encontra na {x + 1}ª posição ")
                                dica = "Digito"
                                break
                        else:
                            print(f"Nenhum digito da sua tentativa aparece na {x + 1}ª posição")
                            dica = "X"
                    print()

                    for x in range(3,-1,-1):

                        nCodigoTentativa = (codigoTentativa % (10**(x+1))) // 10**x             
                        nCodigoSecreto = (codigoSecreto % (10**(x+1))) // 10**x

                        if nCodigoTentativa == nCodigoSecreto:
                            print(nCodigoTentativa, end=" ")

                        elif x + 1 == posicaoDica:
                            print(dica, end=" ")

                        else:
                            print("_", end=" ")
                    print()
                    print()
                    input("<Aperte ENTER>".rjust(43))


    print("Você quer jogar novamente? (1 = sim/0 = não) ")
    jogar = int(input(">")) 

    while not(jogar == 1) and not(jogar == 0):
        print()
        print("ERRO: Você inseriu um número inválido!")
        print("Você quer jogar novamente? (1 = sim/0 = não)")
        jogar = int(input(">"))
        
    if jogar == 0:
        print()
        print("Obrigado por jogar!!!")
        break