#NAO APARECE NADA DO FICHEIRO DAS REGRAS, NEM NOMES
import os
import tkinter as tk
import random
import regras as re

def tab(jogadores):
    print (jogadores)
    botao_bastao = None

    def hist_poicoes(row, col):
        print("Posicao celula clicada:", row, col)

    def rodar_batoes():
        nonlocal botao_bastao
        bastoes = [random.choice(["Branco", "Preto"]) for _ in range(4)]
    
        contador_branco = bastoes.count("Branco")
        contador_preto = bastoes.count("Preto")
    
        label_branco.config(text=f"Branco: {contador_branco}")
        label_preto.config(text=f"Preto: {contador_preto}")

    def aumentar_tamanho_fonte():
        jogador1_label.config(font=("Arial", 16))
        jogador2_label.config(font=("Arial", 16))
        label_branco.config(font=("Arial", 14))
        label_preto.config(font=("Arial", 14))
        botao_bastao.config(font=("Arial", 14))
        
#    def atualizar_nomes_jogadores():
#        jogador1_label.config(text=jogador1)
#        jogador2_label.config(text=jogador2)

    window = tk.Tk()
    window.geometry("800x400")
    window.title("Tabuleiro")

    board = tk.Frame(window)
    board.pack()

    cells = []
    for row in range(3):
        row_cells = []
        for col in range(10):
            cell = tk.Button(board, text="", width=10, height=5, command = lambda r = row, c = col: hist_poicoes(r, c))
            if (row + col) % 2 == 0:
                cell.configure(bg='#8B4513')
            else:
                cell.configure(bg='#D2B48C')
            cell.grid(row=row, column=col)
            row_cells.append(cell)
        cells.append(row_cells)

    white_piece = tk.PhotoImage(file = "white_piece.png")
    black_piece = tk.PhotoImage(file = "black_piece.png")

    for row in range(3):
        for col in range(10):
            if (row + col) % 2 != 0:
                cells[row][col].config(image= white_piece if row == 0 else black_piece)
            
    tabuleiro = tk.Frame(window, bg='White')
    tabuleiro.pack(fill=tk.BOTH, expand=True)

    # Jogadores e função de rodar bastões
    jogadores_e_bastoes = tk.Frame(window)
    jogadores_e_bastoes.pack()

    jogador1_label = tk.Label(jogadores_e_bastoes, text="Jogador 1")
    jogador1_label.pack(side=tk.LEFT)

    jogador2_label = tk.Label(jogadores_e_bastoes, text="Jogador 2")
    jogador2_label.pack(side=tk.RIGHT)

#    atualizar_nomes_jogadores()

    counter_frame = tk.Frame(window)
    counter_frame.pack()

    label_branco = tk.Label(counter_frame, text="Branco: 0")
    label_branco.pack(side=tk.LEFT, padx=5)

    label_preto = tk.Label(counter_frame, text="Preto: 0")
    label_preto.pack(side=tk.LEFT, padx=5)

    botao_bastao = tk.Button(jogadores_e_bastoes, text="Rodar Bastões", command=rodar_batoes)
    botao_bastao.pack()

    aumentar_tamanho_fonte()
#    obter_nomes_jogadores()
    
    window.mainloop()
#    re.verificar_vitoria()

