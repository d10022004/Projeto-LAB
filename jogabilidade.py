import regras as re
def jogar_com_dois():
    em_jogo = True
    i=0
    for i in range(2):
        while em_jogo == True:
            
            bastao_preto, bastao_branco, resultado  = re.regras()
            print (bastao_preto, bastao_branco, resultado)
            em_jogo = False
            
            
jogar_com_dois()
        