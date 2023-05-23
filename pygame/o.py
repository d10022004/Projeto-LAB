import tkinter as tk

def criar_tabuleiro():
    janela = tk.Tk()
    janela.geometry("800x400")  # Define as dimensões da janela
    
    # Cria o tabuleiro
    tabuleiro = tk.Frame(janela, bg='Black')
    tabuleiro.pack(fill=tk.BOTH, expand=True)
    
    # Cria as células do tabuleiro
    for i in range(3):
        for j in range(10):
            celula = tk.Frame(tabuleiro, bg='GoldenRod')
            celula.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
            tabuleiro.grid_columnconfigure(j, weight=1)
            tabuleiro.grid_rowconfigure(i, weight=1)
    
    janela.mainloop()

# Chama a função para criar o tabuleiro
criar_tabuleiro()
