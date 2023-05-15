import pygame

def jogar(jogadores):
    pygame.init()

    BRANCO = (255, 255, 255)
    PRETO = (0, 0, 0)
    CINZA = (200, 200, 200)
    VERDE = (0, 255, 0)
    FUNDO = (235, 199, 158)
    janela = pygame.display.set_mode((1600, 600))
    janela.fill(FUNDO) 
    pygame.display.flip()
    estado = True
    while estado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = False
        
    pygame.display.update()
    
