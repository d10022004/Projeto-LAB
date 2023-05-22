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
                ladobranco += 1
            else:
                print("bastao", j, "-> Lado de madeira")
                ladomadeira = ladomadeira + 1

        if ladobranco == 0:
            print("Mova 5 quadrados e ganha uma jogada extra")
            peao[i] += 5
        elif ladobranco == 1:
            print("Mova 1 quadrado e ganha uma jogada extra")
            peao[i] += 1
        elif ladobranco == 2:
            print("Mova 2 quadrados ")
            peao[i] += 2
        elif ladobranco == 3:
            print("Mova 3 quadrados ")
            peao[i] += 3
        elif ladobranco == 4:
            print("Mova 4 quadrados e ganha uma jogada extra")
            peao[i] += 4

        if peao[i] == 26 and ladobranco == 1:
            peao[i] += 5
            print("Peão", i+1, "esta fora de jogo")  # 1 ponto para o jogador
        elif peao[i] == 27 and ladobranco == 4:
            peao[i] += 5
            print("Peão", i+1, "esta fora de jogo")  # 1 ponto para o jogador
        elif peao[i] == 27:
            peao[i] -= 12
        elif peao[i] == 28 and ladobranco == 3:
            print("Peão", i+1, "esta fora de jogo")  # 1 ponto para o jogador
        elif peao[i] == 29 and ladobranco == 2:
            print("Peão", i+1, "esta fora de jogo")  # 1 ponto para o jogador
        elif peao[i] == 30 and ladobranco >= 1:
            print("Peão", i+1, "esta fora de jogo")  # 1 ponto para o jogador

        ladobranco = 0

    print(peao)