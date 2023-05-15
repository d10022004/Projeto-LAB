import jogo as menu
import tabuleiro as tab


play = menu.menu()
if play != {}:
    tab.jogar(play)