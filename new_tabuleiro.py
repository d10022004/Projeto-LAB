import os
import tkinter as tk
import random

def handle_click(row, col):
    print("Clique na celula:", row, col)

def rodar_batoes():
    bastoes = [random.choice(["Branco", "Preto"]) for _ in range(4)]
    
    contador_branco = bastoes.count("Branco")
    contador_preto = bastoes.count("Preto")
    
    white_label.config(text=f"Branco: {contador_branco}")
    black_label.config(text=f"Preto: {contador_preto}")

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
        if (row + col) % 2 == 0:
            cell.configure(bg='#8B4513')
        else:
            cell.configure(bg='#D2B48C')
        cell.grid(row=row, column=col)
        row_cells.append(cell)
    cells.append(row_cells)

tabuleiro = tk.Frame(window, bg='White')
tabuleiro.pack(fill=tk.BOTH, expand=True)

# Jogadores e função de rodar bastões
players_and_sticks = tk.Frame(window)
players_and_sticks.pack()

player1_label = tk.Label(players_and_sticks, text="Jogador 1")
player1_label.pack(side=tk.LEFT)

player2_label = tk.Label(players_and_sticks, text="Jogador 2")
player2_label.pack(side=tk.RIGHT)

counter_frame = tk.Frame(window)
counter_frame.pack()

white_label = tk.Label(counter_frame, text="Branco: 0")
white_label.pack(side=tk.LEFT, padx=5)

black_label = tk.Label(counter_frame, text="Preto: 0")
black_label.pack(side=tk.LEFT, padx=5)

stick_button = tk.Button(players_and_sticks, text="Rodar Bastões", command=rodar_batoes)
stick_button.pack()

window.mainloop()
