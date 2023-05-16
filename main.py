import jogo as menu
import tabuleiro as tab

play = menu.menu()

def obter_nomes_jogadores():
    jogador1 = input("Digite o nome do Jogador 1: ")
    jogador2 = input("Digite o nome do Jogador 2: ")
    
    return jogador1, jogador2

nomes_jogadores = obter_nomes_jogadores()
tab.tab(*nomes_jogadores)
