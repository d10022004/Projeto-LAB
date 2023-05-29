import pygame
import tkinter as tk
import random

random.seed()
estado_jogo = True
jogadores = []
jogadoresd = {}

def menu():
    global estado_jogo
    pygame.init()
    imagemfundo = pygame.image.load("imagemfundo.jpeg")
    compri = imagemfundo.get_width()
    larg = imagemfundo.get_height()
    janela = pygame.display.set_mode((compri - 1, larg - 1))
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

    # Render the title text and create a gradient background
    title_font = pygame.font.Font(None, 80)
    title_text = title_font.render("SENET", True, (255, 0 ,0))
    title_text_rect = title_text.get_rect(center=(compri // 2, larg // 2 - 80))
    gradient = pygame.Surface((title_text_rect.width, title_text_rect.height), pygame.SRCALPHA)
    pygame.draw.rect(gradient, (0, 0, 0, 50), gradient.get_rect())

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
                label = tk.Label(janela_nome2, text="  Introduza o seu nome:  ")
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
            label = tk.Label(janela_nome1, text="  Introduza o seu nome:  ")
            label.pack()
            entrada = tk.Entry(janela_nome1)
            entrada.pack()
            botao = tk.Button(janela_nome1, text="OK", command=lambda: segundoplay(entrada))
            botao.pack()
            label_nome = tk.Label(janela_nome1, text="")
            label_nome.pack()
            janela_nome1.mainloop()

        global estado_jogo
        estado_jogo = False
        janela_op = tk.Tk()
        janela_op.title("OPÇÕES")
        janela_op.geometry("200x200")
        botao = tk.Button(janela_op, text="OK", command=intrnome)
        botao.pack()
        janela_op.mainloop()

    def carregajogo():
        global estado_jogo
        estado_jogo = False

    def regrasjogo():
        global estado_jogo
        estado_jogo = False

    def sair():
        global estado_jogo
        estado_jogo = False

    while estado_jogo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado_jogo = False

        if estado_jogo:
            janela.blit(imagemfundo, (0, 0))

            # Blit the title text and gradient background
            janela.blit(gradient, title_text_rect)
            janela.blit(title_text, title_text_rect)

            criar_botao("NOVO JOGO", CINZA, VERDE, (250, 180), 220, 50, novojogo)
            criar_botao("CARREGA JOGO", CINZA, VERDE, (250, 240), 220, 50, carregajogo)
            criar_botao("REGRAS JOGO", CINZA, VERDE, (250, 300), 220, 50, regrasjogo)
            criar_botao("SAIR", CINZA, VERDE, (250, 360), 220, 50, sair)

        pygame.display.update()

    pygame.quit()

menu()