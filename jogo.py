import pygame
import tkinter as tk
estado_jogo = True
jogadores = []
jogadoresd = {}
def menu():
    global estado_jogo
    pygame.init()
    imagemfundo = pygame.image.load("imagemfundo.jpeg")
    compri = imagemfundo.get_width()
    larg = imagemfundo.get_height()
    janela = pygame.display.set_mode((compri, larg))
    BRANCO = (255, 255, 255)
    PRETO = (0, 0, 0)
    CINZA = (200, 200, 200)
    VERDE = (0, 255, 0)

    def criar_botao(texto, cor_normal, cor_hover, posicao, largura, altura, acao):
        retangulo = pygame.Rect(posicao[0], posicao[1], largura, altura)

        cor = cor_normal
        mouse_pos = pygame.mouse.get_pos()
        if retangulo.collidepoint(mouse_pos):
            cor = cor_hover
            if pygame.mouse.get_pressed()[0] == 1:
                acao()

        pygame.draw.rect(janela, cor, retangulo)
        texto_surface = pygame.font.Font(None, 40).render(texto, True, PRETO)
        texto_rect = texto_surface.get_rect(center=retangulo.center)
        janela.blit(texto_surface, texto_rect)
        
        

    def novojogo():
        def intrnome():
            def segundoplay(entrada):
                def fechar():
                    jogadoresd['nome2'] = entrada.get()
                    jogadores.append(jogadoresd)
                    janela_nome2.destroy()
                    global estado_jogo
                    estado_jogo = False
                    

                jogadoresd['nome1'] = entrada.get()

                janela_nome1.destroy()
                janela_nome2 = tk.Tk()
                janela_nome2.title("JOGADOR 2")
                janela_nome2.geometry("400x200")
                label = tk.Label(janela_nome2, text="  Digite seu nome:  ")
                label.pack()
                entrada = tk.Entry(janela_nome2)
                entrada.pack()
                botao = tk.Button(janela_nome2, text="   OK   ", command=fechar)
                botao.pack()
                label_nome = tk.Label(janela_nome2, text="")
                label_nome.pack()
                janela_nome2.mainloop()
            janela_op.destroy()
            janela_nome1 = tk.Tk()
            janela_nome1.title("JOGADOR 1")
            janela_nome1.geometry("400x200")
            label = tk.Label(janela_nome1, text="  Digite seu nome:  ")
            label.pack()
            entrada = tk.Entry(janela_nome1)
            entrada.pack()
            botao = tk.Button(janela_nome1, text="OK", command=lambda: segundoplay(entrada))
            botao.pack()
            label_nome = tk.Label(janela_nome1, text="")
            label_nome.pack()
            janela_nome1.mainloop()

        def intrnomeind():
            def fecharind(entrada):
                jogadoresd['nome1'] = entrada.get()
                jogadores.append(jogadoresd)
                janela_nomeind.destroy()
                jogadoresd['nome2'] = 'BOOT'
                global estado_jogo
                estado_jogo = False
                
            janela_nomeind = tk.Tk()
            janela_nomeind.title("JOGADOR 1")
            janela_nomeind.geometry("400x200")
            label = tk.Label(janela_nomeind, text="  Digite seu nome:  ")
            label.pack()
            entrada = tk.Entry(janela_nomeind)
            entrada.pack()
            botao = tk.Button(janela_nomeind, text="OK", command=lambda: fecharind(entrada))
            botao.pack()
            label_nome = tk.Label(janela_nomeind, text="")
            label_nome.pack()
            janela_nomeind.mainloop()

        janela_op = tk.Tk()
        janela_op.title("Introduza opção")
        janela_op.geometry("400x200")
        labelop1 = tk.Label(janela_op, text="  Qual prefere?  ")
        labelop1.pack()
        botao1 = tk.Button(janela_op, text="   1 VS 1   ", command=intrnome)
        botao1.pack()
        botao2 = tk.Button(janela_op, text="  1 VS BOT  ", command=intrnomeind)
        botao2.pack()
        janela_op.mainloop()

      #  return dadosjogadores
    def carregajogo():
        print("CARREGA JOGO")

    def regrasjogo():
        janela_regras = tk.Tk()
        janela_regras.title ("Regras SENET")
        janela_regras.geometry ("700x600")
        janela_regras.configure (bg = 'peru')
        frase1 = tk.Label (janela_regras, text="O jogo utiliza quatro varas de arremesso que têm a forma de meio cilindro, com a \n superfície arredondada pintada de preto e a superfície plana pintada de branco. O objetivo do \n jogo é lançar as varas e contar o número de brancos obtidos. Um resultado de nenhum é \ncontado como cinco, permitindo ao jogador avançar 5 casas e ter uma jogada extra. Se o \n resultado do lançamento for quatro ou um, o jogador avança o número de casas correspondente e ganha uma jogada extra. No caso de sair dois ou três, o jogador realiza um \n movimento e passa a vez ao adversário. Se não houver nenhum movimento legal disponível, o \n jogador perde a vez.\n")
        frase1.pack()
        frase2 = tk.Label (janela_regras, text = "")
        botaoregra = tk.Button(janela_regras, text="          OK          ")
        botaoregra.pack ()
        janela_regras.mainloop()
        
        
    def sair():
        global estado_jogo
        estado_jogo = False
    
    while estado_jogo == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado_jogo = False
           
        if estado_jogo == True:
            janela.blit(imagemfundo, (0, 0))
            criar_botao("NOVO JOGO", CINZA, VERDE, (250, 180), 220, 50, novojogo)
            criar_botao("CARREGA JOGO", CINZA, VERDE, (250, 240), 220, 50, carregajogo)
            criar_botao("REGRAS JOGO", CINZA, VERDE, (250, 300), 220, 50, regrasjogo)
            criar_botao("SAIR", CINZA, VERDE, (250, 360), 220, 50, sair)
        pygame.display.update()
    return jogadores
        







