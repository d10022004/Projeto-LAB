import pygame
import tkinter as tk

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

def fechar_janela():
    pygame.quit()


estado_jogo = True
while estado_jogo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            estado_jogo = False
    def novojogo():
        def mostrar_nome():
            nome = entrada.get()
            janela_jogo.destroy()
            print(nome)
            fechar_janela()

        janela_jogo = tk.Tk()
        janela_jogo.title("Introduza o nome")

        label = tk.Label(janela_jogo, text="Digite seu nome:")
        label.pack()
        entrada = tk.Entry(janela_jogo)
        entrada.pack()
        botao = tk.Button(janela_jogo, text="Mostrar nome", command=mostrar_nome)
        botao.pack()
        label_nome = tk.Label(janela_jogo, text="")
        label_nome.pack()

        janela_jogo.mainloop()
    def carregajogo():
        print("CARREGA JOGO")

    def sair():
        global estado_jogo
        estado_jogo = False
        
    janela.blit(imagemfundo, (0, 0))
    criar_botao("NOVO JOGO", CINZA, VERDE, (250, 180), 220, 50, novojogo)
    criar_botao("CARREGA JOGO", CINZA, VERDE, (250, 240), 220, 50, carregajogo)
    criar_botao("REGRAS JOGO", CINZA, VERDE, (250, 300), 220, 50, carregajogo)
    criar_botao("SAIR", CINZA, VERDE, (250, 360), 220, 50, sair)
    pygame.display.update()








