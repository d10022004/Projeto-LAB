import random
random.seed()

bastão = 0
ladobranco = 0
ladomadeira = 0
peao = [0, 0]

def regras():
    global ladobranco  
    global ladomadeira
    for i in range(2):
        for j in range(1, 5):
            bastão = random.randint(0, 2)
            if bastão == 1:
                print("bastao", j, "-> Lado branco")
                ladobranco = ladobranco + 1
                
        
            else:
                print("bastao", j, "-> Lado de madeira")
                ladomadeira = ladomadeira + 1
                
    
        
        if ladobranco == 0:
            print("  *saiu 0 lados brancos")
            print("  *sairam 5 lados de madeira")
            print("Mova 5 quadrados e ganha uma jogada extra\n")
            peao[i] += 5
        elif ladobranco == 1:
            print("  *saiu 1 lado branco")
            print("  *sairam 4 lados de madeira")
            print("Mova 1 quadrado e ganha uma jogada extra\n")
            peao[i] += 1
        elif ladobranco == 2:
            print("  *sairam 2 lados brancos")
            print("  *sairam 2 lados de madeira")
            print("Mova 2 quadrados\n")
            peao[i] += 2
        elif ladobranco == 3:
            print("  *sairam 3 lados brancos")
            print("  *sairam 2 lados de madeira")
            print("Mova 3 quadrados\n")
            peao[i] += 3
        elif ladobranco == 4:
            print("  *saiu 1 lado de madeira\n")
            print("Mova 4 quadrados e ganha uma jogada extra")
            peao[i] += 4

        if peao[i] == 26 and ladobranco == 1:
            peao[i] += 5
            print("Peão", i+1, "esta fora de jogo\n")  # 1 ponto para o jogador
        elif peao[i] == 27 and ladobranco == 4:
            peao[i] += 5
            print("Peão", i+1, "esta fora de jogo\n")  # 1 ponto para o jogador
        elif peao[i] == 27:
            peao[i] -= 12
        elif peao[i] == 28 and ladobranco == 3:
            print("Peão", i+1, "esta fora de jogo\n")  # 1 ponto para o jogador
        elif peao[i] == 29 and ladobranco == 2:
            print("Peão", i+1, "esta fora de jogo\n")  # 1 ponto para o jogador
        elif peao[i] == 30 and ladobranco >= 1:
            print("Peão", i+1, "esta fora de jogo\n")  # 1 ponto para o jogador

        ladobranco = 0
    
    print(peao)
    #print("sairam", ladobranco, "bastoes com lado branco")
    #print("sairam", ladomadeira, "bastoes com lado de madeira")

regras()