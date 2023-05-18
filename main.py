import jogo as menu
while menu.estado_jogo == True:
    play = menu.menu()
print (play)
import tabuleiro as tab
tab.tab(play)
