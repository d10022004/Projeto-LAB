import pygame
import tkinter as tk
pygame.init()

#janela = pygame.display.set_mode((800,600))
#pygame.display.set_caption("SENET em Python")

#janela_aberta = True
#while janela_aberta: 

#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            janela_aberta = False

#pygame.quit()


def handle_click(row, col):
    print("Clique na celula:", row, col)

window = tk.Tk()
window.geometry("800x400")
window.title("Tabuleiro")

board = tk.Frame(window)
board.pack()

cells = []
for row in range(3):
    row_cells = []
    for col in range(10):
        cell = tk.Button(board, text="", width=10, height=5, command=lambda r=row, c=col: handle_click(r, c))
        if(row + col) % 2 == 0:
            cell.configure(bg = '#8B4513')
        else :
            cell.configure(bg = '#D2B48C')
        cell.grid(row=row, column=col)
        row_cells.append(cell)
    cells.append(row_cells)

    tabuleiro = tk.Frame(window, bg='Black') #PARA MUDAR A COR DO FUNDO DEBAIXO DO TABULEIRO
    tabuleiro.pack(fill=tk.BOTH, expand=True)
    
window.mainloop()
