import tkinter as tk
import random

def tab(jogador1, jogador2):
    print(jogador1, jogador2)
    botao_bastao = None

    def hist_posicoes(row, col, jogador):
        print("Posicao celula clicada:", row, col)
        print("Jogador:", jogador)

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

    def atualizar_nomes_jogadores():
        jogador1_label.config(text=jogador1)
        jogador2_label.config(text=jogador2)

    window = tk.Tk()
    window.geometry("800x400")
    window.title("Tabuleiro")

    board = tk.Frame(window)
    board.pack()

    cells = []
    for row in range(3):
        row_cells = []
        for col in range(10):
            if row == 0:
                if (col + 1) % 2 != 0:
                    cell = tk.Button(board, text="", width=10, height=5, command=lambda r=row, c=col: hist_posicoes(r, c, jogador1))
                    cell.configure(bg='#D2B48C')
                    cell.grid(row=row, column=col)
                    row_cells.append(cell)
                else:
                    cell = tk.Button(board, text="", width=10, height=5, command=lambda r=row, c=col: hist_posicoes(r, c, jogador2))
                    cell.configure(bg='#8B4513')
                    cell.grid(row=row, column=col)
                    row_cells.append(cell)
            else:
                cell = tk.Button(board, text="", width=10, height=5, command=lambda r=row, c=col: hist_posicoes(r, c, ""))
                if (row + col) % 2 == 0:
                    cell.configure(bg='#8B4513')
                else:
                    cell.configure(bg='#D2B48C')
                cell.grid(row=row, column=col)
                row_cells.append(cell)
        cells.append(row_cells)

    white_piece = tk.PhotoImage(file="white_piece.png")
    black_piece = tk.PhotoImage(file="black_piece.png")

    cells[0][0].config(image=white_piece)
    cells[0][2].config(image=white_piece)
    cells[0][4].config(image=white_piece)
    cells[0][6].config(image=white_piece)
    cells[0][8].config(image=white_piece)

    cells[0][1].config(image=black_piece)
    cells[0][3].config(image=black_piece)
    cells[0][5].config(image=black_piece)
    cells[0][7].config(image=black_piece)
    cells[0][9].config(image=black_piece)

    tabuleiro = tk.Frame(window, bg='White')
    tabuleiro.pack(fill=tk.BOTH, expand=True)

    jogadores_e_bastoes = tk.Frame(window)
    jogadores_e_bastoes.pack()

    jogador1_label = tk.Label(jogadores_e_bastoes, text="Jogador 1")
    jogador1_label.pack(side=tk.LEFT)

    jogador2_label = tk.Label(jogadores_e_bastoes, text="Jogador 2")
    jogador2_label.pack(side=tk.RIGHT)

    counter_frame = tk.Frame(window)
    counter_frame.pack()

    label_branco = tk.Label(counter_frame, text="Branco: 0")
    label_branco.pack(side=tk.LEFT, padx=5)

    label_preto = tk.Label(counter_frame, text="Preto: 0")
    label_preto.pack(side=tk.LEFT, padx=5)

    botao_bastao = tk.Button(jogadores_e_bastoes, text="Rodar Bastões", command=rodar_batoes)
    botao_bastao.pack(side=tk.RIGHT)

    aumentar_tamanho_fonte()

    window.mainloop()

tab("Jogador 1", "Jogador 2")
