import random

#JOGO ADIVINHAÇÃO - ATIVADE AVALIATIVA 01

#TELA INICIAL

print("                ---Seja bem-vindo ao Jogo da Advinhação!!---                  ")
print()
print(" Nesse jogo, você vai precisar advinhar o número secreto entre [1000 e 9999]. ")
print("             A partir da 5ª tentativa, o jogo ajudara com dicas.              ")

print()

#COMEÇAR O JOGO - LOOP WHILE

print("Você quer jogar? (1 = sim/0 = não) ")
jogar = int(input(">")) #Pergunta se o jogador quer jogar o jogo, podemos trocar por aperte enter para jogar, ja que ele abriu o jogo

while jogar == 1:
    print("Jogando")

    #GERAR NÚMERO ALEATÓRIO

    codigoSecreto = random.randint(1000,9999)
    print(codigoSecreto)

    #TENTATIVAS:

    for contTentativa in range(1,11): #Quantidade de tentativas do usuário

        print()
        
        print(f"--{contTentativa}ª TENTATIVA--")
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

        for x in range(3,-1,-1): #SEPARANDO O NÚMERO EM 4 DIGITOS

            #Divide o número por 10000 (10^4) e pega o resto, depois divide por 1000 (10^3), definindo a variável como o primeiro dígito e assim por diante.

            nCodigoTentativa = (codigoTentativa % (10**(x+1))) // 10**x             
            nCodigoSecreto = (codigoSecreto % (10**(x+1))) // 10**x

            #EX: tentativa = 1234, x = 3, primeiro digito: numero % 10000 // 1000 -> 1234 % 10000 = 1234 -> 1234 // 1000 = 1

            if nCodigoTentativa == nCodigoSecreto: #Imprime na tela os números que o jogador acertou, EXEMPLO: 1 _ 3 _
                print(nCodigoTentativa, end=' ')
            else:
                print("_", end=" ")

        print()
        print()
        if contTentativa == 10 and codigoTentativa != codigoSecreto:
            print("Número de tentativas excedidas :( ") 
            print("VOCÊ NÃO CONSEGEGIU ACERTAR.")
            print(f"O código era: {codigoSecreto}")
            
        #DICAS:

        if contTentativa >= 5:

            dica = False

            while dica == False:

                posicaoDica = random.randint(1,4) # _ _ _ _

                #Define os digitos na (posicaoDica)ª posição da tentativa. EX: se a posição da dica == 3, ele vai achar o terceiro digito.

                nCodigoTentativa = (codigoTentativa % (10**(posicaoDica))) // 10**(posicaoDica-1) 
                nCodigoSecreto = (codigoSecreto % (10**(posicaoDica))) // 10**(posicaoDica-1)

                #EX: tentativa = 1234, posicaoDica = 1, ultimo digito: numero % 10**1 // 10 ** 0 -> 1234 % 10 = 4 -> 4 // 1 = 4

                if nCodigoTentativa != nCodigoSecreto:

                    tipoDica = random.randint(1,2) #Par/Impar ou <5/>=5
                    if tipoDica == 1:
                        if nCodigoSecreto % 2 == 0:
                            print(f"O {5-posicaoDica}° número é Par")
                            dica = True
                        else:
                            print(f"O {5-posicaoDica}° número é Ímpar")
                            dica = True
                    elif tipoDica == 2:
                        if nCodigoSecreto >= 5:
                            print(f"O {5-posicaoDica}° número é maior ou igual a 5")
                            dica = True
                        else:
                            print(f"O {5-posicaoDica}° número é menor que 5")
                            dica = True

    print("Você quer jogar? (1 = sim/0 = não) ")
    jogar = int(input(">")) #Jogar novamente: