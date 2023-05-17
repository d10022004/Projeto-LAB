import jogo as menu
while menu.estado_jogo == True:
    play = menu.menu()
import tabuleiro as tab
tab.tab(play)
