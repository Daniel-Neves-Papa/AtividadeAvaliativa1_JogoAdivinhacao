import random

#JOGO ADIVINHAÇÃO - ATIVADE AVALIATIVA 01

#TELA INICIAL
print("                ---Seja bem-vindo ao Jogo da Advinhação!!---                  ")

print(" Nesse jogo, você vai precisar advinhar o número secreto entre [1000 e 9999]. ")
print("             A partir da 5ª tentativa, o jogo ajudara com dicas.              ")

print()

#COMEÇAR O JOGO - LOOP WHILE

jogar = int(input("Você quer jogar? (1 = sim/0 = não) ")) #Pergunta se o jogador quer jogar o jogo, podemos trocar por aperte enter para jogar, ja que ele abriu o jogo

while jogar == 1:
    print("Jogando")
    contTentativa = 0
    codigoSecreto = random.randint(1000,9999)
    print(codigoSecreto)
    for i in range(1,11): #Quantidade de tentativas do usuário
        
        contTentativa += 1
    
#GERAR NÚMERO ALEATÓRIO

        print()
        print(f"--{contTentativa}ª TENTATIVA--")
        codigoTentativa=int(input("Digite um número de quatro digitos: "))

        while 1000 > codigoTentativa or codigoTentativa > 9999: #Verificando se o número é válido, se não for, pede o input novamente.
            print("ERRO: Você inseriu um número inválido!")
            codigoTentativa=int(input("Digite novamente um número de quatro digitos "))

    #TENTATIVAS:

        for x in range(3,-1,-1): #SEPARANDO O NÚMERO EM 4 DIGITOS

            #Divide o número por 10000 (10^4) e pega o resto, depois divide por 1000 (10^3), definindo a variável como o primeiro dígito e assim por diante.
            nCodigoTentativa = (codigoTentativa % (10**(x+1))) // 10**x             
            nCodigoSecreto = (codigoSecreto % (10**(x+1))) // 10**x
            
            if nCodigoTentativa == nCodigoSecreto: #Imprime na tela os números que o jogador acertou, EXEMPLO: 1 _ 3 _
                print(nCodigoTentativa, end=' ')
            else:
                print("_", end=" ")

        print("")
    jogar = int(input("Você quer jogar novamente? (1 = sim/0 = não)"))
    
              
#DICAS