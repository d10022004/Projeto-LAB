import jogo as menu
import tabuleiro as tab

while menu.estado_jogo == True:
    play = menu.menu()


tab.tab(play)