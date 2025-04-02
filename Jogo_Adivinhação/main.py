import random

#JOGO ADIVINHAÇÃO 

#TELA INICIAL
print("---Seja bem-vindo ao Jogo da Advinhação!!---")

print("Nesse jogo, você vai precisar advinhar o número secreto entre [1000 e 9999], a partir da 5a tentativa, o jogo ajudara com dicas.")


#COMEÇAR O JOGO - LOOP WHILE

jogar = int(input("Você quer jogar? (1/0) (1 = sim) (0 = não)")) 

while jogar == 1:
    print("Jogando")
    contTentativa = 0
    codigoSecreto = random.randint(1000,9999)
    print(codigoSecreto)
    for i in range(1,11): #Quantidade de tentativas do usuário
        
        contTentativa += 1
    
#GERAR NÚMERO ALEATÓRIO

        
        codigoTentativa=int(input("Digite um numero entre 1000 e 9999: "))

        while 1000 > codigoTentativa or codigoTentativa > 9999: #VERIFICANDO SE O NÚMERO É VÁLIDO
            print("Número inválido")
            codigoTentativa=int(input("Digite um numero entre 1000 e 9999: "))

    #TENTATIVAS:
    
        print(f"Você está na tentativa: {contTentativa}")

        for x in range(3,-1,-1): #SEPARANDO O NÚMERO EM 4 DIGITOS

            nCodigoTentativa = (codigoTentativa % (10**(x+1))) // 10**x #DIVIDE A TENTATIVA PRIMEIRO POR 10000(10**4) E PEGA O RESTO, DEPOIS DIVIDE POR 1000
            nCodigoSecreto = (codigoSecreto % (10**(x+1))) // 10**x

            #print(x)
            #print(nCodigoTentativa)
            #print(nCodigoSecreto)
            
            if nCodigoTentativa == nCodigoSecreto:
                print(nCodigoTentativa, end=' ')
            else:
                print("_", end=" ")
        print("")
    jogar = int(input("Você quer jogar? (1/0)"))
    
              
#DICAS