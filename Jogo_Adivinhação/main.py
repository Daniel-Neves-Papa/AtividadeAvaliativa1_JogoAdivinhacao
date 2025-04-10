import random

#JOGO ADIVINHAÇÃO - ATIVADE AVALIATIVA 01

#TELA INICIAL

print("------------------------------------------------------------------------------")
print("                   Seja bem-vindo ao Jogo da Advinhação!!                     ")
print()
print(" Nesse jogo, você vai precisar advinhar o número secreto entre [1000 e 9999]. ")
print("          A partir da 5ª tentativa, o jogo vai te ajudar com dicas.           ")
print("------------------------------------------------------------------------------")
print()

#COMEÇAR O JOGO - LOOP WHILE

input("<Aperte ENTER>".rjust(43))

jogar = 1
while jogar == 1:
    print()
    print("O JOGO COMEÇOU")

    #GERAR NÚMERO ALEATÓRIO

    codigoSecreto = random.randint(1000,9999)
    print(codigoSecreto)

    #TENTATIVAS:

    for contTentativa in range(1,11): #Quantidade de tentativas do usuário

        print()
        
        print(f"--{contTentativa}ª TENTATIVA--".rjust(44))
        codigoTentativa = int(input("Digite sua tentativa: "))

        while 1000 > codigoTentativa or codigoTentativa > 9999: #Verificando se o número é válido, se não for, pede o input novamente.
            print("ERRO: Você inseriu um número inválido!")
            codigoTentativa=int(input("Digite novamente um número de quatro digitos: "))

        print()

        #Se o jogador acertar o código:

        if codigoSecreto == codigoTentativa:

            print("PARABÉNS, você acertou o código!!!")
            print(f"O código era: {codigoSecreto}")
            print(f"Você acertou o código em: {contTentativa} tentativas")
            print()
            break

        nAcertos = 0
        print("Seu código é:", end=" ")
        for x in range(3,-1,-1): #SEPARANDO O NÚMERO EM 4 DIGITOS

            nCodigoTentativa = (codigoTentativa % (10**(x+1))) // 10**x             
            nCodigoSecreto = (codigoSecreto % (10**(x+1))) // 10**x

            if nCodigoTentativa == nCodigoSecreto: #Imprime na tela os números que o jogador acertou, EXEMPLO: 1 _ 3 _
                print(nCodigoTentativa, end=' ')
                nAcertos += 1
            else:
                print("_", end=" ")
        print()
        if nAcertos > 0:
            print(f"Você acertou {nAcertos} digitos nessa tentativa")
        else:
            print("Você não acertou nenhum digito nessa tentativa")
        print()
        
        if contTentativa == 10 and codigoTentativa != codigoSecreto:
            print("Número de tentativas excedidas :( ") 
            print("VOCÊ NÃO CONSEGEGIU ACERTAR.")
            print(f"O código era: {codigoSecreto}")
            break
            
        #DICAS:

        if contTentativa >= 5:
            print("Aqui vai uma dica:", end=" ")
            dicaEnviada = 0

            while dicaEnviada == 0:

                posicaoDica = random.randint(1,4) # _ _ _ _

                nCodigoTentativa = (codigoTentativa % (10**(posicaoDica))) // 10**(posicaoDica-1) 
                nCodigoSecreto = (codigoSecreto % (10**(posicaoDica))) // 10**(posicaoDica-1)

                if nCodigoTentativa != nCodigoSecreto:

                    tipoDica = random.randint(1,3) #Par/Impar ou <5/>=5
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

                    elif tipoDica == 3:  #TIPO 3 - SE ALGUM NÚMERO DA TENTATIVA ESTAVA NO LUGAR ERRADO:
                        for x in range(3,-1,-1):
             
                            nCodigoTentativa = (codigoTentativa % (10**(x+1))) // 10**x 
                            
                            if nCodigoTentativa == nCodigoSecreto: #Se o nCódigo tentativa na posição X for igual ao número correto da posição da dica:
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
    jogar = int(input(">")) #Jogar novamente:
    
    while not(jogar == 1) and not(jogar == 0):
        print()
        print("ERRO: Você inseriu um número inválido!")
        print("Você quer jogar novamente? (1 = sim/0 = não)")
        jogar = int(input(">"))
    if jogar == 0:
        print()
        print("Obrigado por jogar!!!")
        break