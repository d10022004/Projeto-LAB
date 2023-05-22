#NAO APARECE NADA DO FICHEIRO DAS REGRAS

import os
import tkinter as tk
import random
import keyboard #IMPORT DE KEYBOARD PARA O MACRO
import regras as re

def tab(jogadores):
    botao_bastao = None
    janela_pausa = None
    
    def hist_poicoes(row, col):
        print("Posicao celula clicada:", row, col)

    
    
    def rodar_batoes():
        bastoes = [random.choice(["Branco", "Preto"]) for _ in range(4)]
    
        contador_branco = bastoes.count("Branco")
        contador_preto = bastoes.count("Preto")
        """_summary_
        """    
        label_branco.config(text=f"Branco: {contador_branco}")
        label_preto.config(text=f"Preto: {contador_preto}")
    
    def aumentar_tamanho_fonte():
        jogador1_label.config(font = ("Arial", 16))
        jogador2_label.config(font = ("Arial", 16))
        label_branco.config(font = ("Arial", 14))
        label_preto.config(font = ("Arial", 14))
        botao_com.config(font = ("Arial", 14))

    def abrir_menu_pausa():
        nonlocal janela_pausa
        janela_pausa = tk.Toplevel(window)
        janela_pausa.title("Menu de Pausa")

        guardar_botao = tk.Button(janela_pausa, text = "Guardar Jogo", command = guardar_jogo)
        guardar_botao.pack(pady=15)

        sair_botao = tk.Button(janela_pausa, text = "Sair do Jogo", command = sair_jogo)
        sair_botao.pack(pady=15)

    def guardar_jogo():
        print("Jogo salvo!")

    def sair_jogo():
        print("Jogo encerrado.")
        window.destroy()

    def atalho_menu_pausa():
        abrir_menu_pausa()

#   keyboard.on_press_key("esc", atalho_menu_pausa) TENTATIVA DE MACRO ATRAVES DE TECLADO
    
    window = tk.Tk()
    window.geometry("800x400")
    window.title("Tabuleiro")
    
    board = tk.Frame(window)
    board.pack()
    def jogar ():
        def jogar_com_dois():
            def ola():
                bastao_preto, bastao_branco, resultado  = re.regras()
                label_branco.config(text=f"Branco: {bastao_branco}") 
                label_preto.config(text=f"Preto: {bastao_preto}") 
                print (bastao_preto, bastao_branco, resultado)
            em_jogo = True
            i=0
            for i in range(2):
                while em_jogo == True:
                    botao_lan = tk.Button(jogadores_e_bastoes, text = "RODAR", command = ola)
                    botao_lan.pack()
                    botao_lan.config(font = ("Arial", 14))
                    em_jogo = False
        
        botao_com.destroy()
        numjog=1
        if numjog ==1:
            jogar_com_dois()
        
        
    cells = []
    cell_number = 1
    for row in range(3):
        row_cells = []
        for col in range(10):
            cell = tk.Button(board, text="", width=10, height=5, command=lambda r=row, c=col: hist_poicoes(r, c))
            if (row + col) % 2 == 0:
                cell.configure(bg='#8B4513')
            else:
                cell.configure(bg='#D2B48C')
            cell.grid(row=row, column=col)
            row_cells.append(cell)
            if row == 0:
                if col == 0:
                    i=0
                cell_number = i+1  
                i += 1
            elif row==1:
                if col == 0:
                    i=0
                aux = 20
                cell_number = aux - i  
                i += 1
            elif row==2:
                if col == 0:
                    i=0
                aux = 21
                cell_number = aux + i
                i += 1
            cells.append(cell_number)
    print (cells)


    tabuleiro = tk.Frame(window, bg = 'White')
    tabuleiro.pack(fill=tk.BOTH, expand = True)
   
    
    white_piece = tk.PhotoImage(file = "white_piece.png")
    black_piece = tk.PhotoImage(file = "black_piece.png")

    celu = []
    for row in range(1):
        row_celu = []
        for col in range(10):
            celu = tk.Button(board, text = "", width = 20, height = 20, command = lambda r=row, c=col: hist_poicoes(r, c))
            if (row + col) % 2 == 0:
                celu.configure(image = white_piece)
            else:
                celu.configure(image = black_piece)
            celu.grid(row = row, column=col)
            row_celu.append(cell)
        cells.append(row_celu)

    
    #Jogadores e função de rodar bastões
    
    jogadores_e_bastoes = tk.Frame(window)
    jogadores_e_bastoes.pack()
    
    jogador1_label = tk.Label(jogadores_e_bastoes, text = jogadores['nome1'])
    jogador1_label.pack(side = tk.LEFT)
    
    jogador2_label = tk.Label(jogadores_e_bastoes, text = jogadores['nome2'])
    jogador2_label.pack(side = tk.RIGHT)
    
    counter_frame = tk.Frame(window)
    counter_frame.pack()
    
    label_branco = tk.Label(counter_frame, text = "Branco: 0")
    label_branco.pack(side = tk.LEFT, padx = 5)
    
    label_preto= tk.Label(counter_frame, text = "Preto: 0")
    label_preto.pack(side = tk.LEFT, padx = 5)
    
    botao_com = tk.Button(jogadores_e_bastoes, text = "JOGAR?", command = jogar)
    botao_com.pack()

    pausa_botao = tk.Button(window, text = "Pausa", command = abrir_menu_pausa)
    pausa_botao.pack(pady=10)
    
    #keyboard.add_hotkey('esc', atalho_menu_pausa)

    aumentar_tamanho_fonte()
<<<<<<< HEAD
    window.mainloop()

    
tab({'nome1': 'fdfgwsef', 'nome2': 'BOT'})
=======
    window.mainloop()
>>>>>>> 5ee2c08a481e3d1deef5d04248a8bb7a662de1da
