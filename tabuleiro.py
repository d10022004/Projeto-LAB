import os
import tkinter as tk
import random
import regras as re
import pygame

resultado = 0
#definir coordenadas para celulas num tabuleiro
button_positions = {}
matriz = []
h=1
###############define coordenadas celulas ######################################
dicionario = {}
lar=55
com=60
for h in range (1, 31):
    if h <=10:
        dicionario [h] = lar/2, com/2
        if h<10:
            lar +=160
    if h> 10 and h <= 20:
        com = 220
        dicionario [h] = lar/2, com/2
        if h<20:
            lar -= 160
    if h > 20 and h <= 30:
        com = 390
        dicionario [h] = lar/2, com/2
        lar += 160
##################################################################################

class Piece:
    def __init__(self, player):
        self.player = player

jogador1 = "Jogador1"
jogador2 = "Jogador2"

white_pieces = [Piece(player=jogador1) for _ in range(10)]
black_pieces = [Piece(player=jogador2) for _ in range(10)]
                
def move_piece(button):
    global white_pieces, black_pieces

    for piece in white_pieces:
        if piece.player == jogador1 and button["image"] == white_pieces:
            print("Jogador 1 moved a white piece")
            return

    for piece in black_pieces:
        if piece.player == jogador2 and button["image"] == black_pieces:
            print("Jogador 2 moved a black piece")
            return

    print("Unauthorized player attempted to move a piece")


def tab(jogadores):
    global resultado
    botao_bastao = None
    janela_pausa = None
    lancamento = 0
    
    def verifica(): 
        global resultado
        if resultado == 0:
            print ("OLA")    
    
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

    window = tk.Tk()
    window.geometry("800x400")
    window.title("Tabuleiro")
    
    board = tk.Frame(window)
    board.pack()

    #contador de peças brancas e pretas que sairam
    pecas_out_branco = 0
    pecas_out_preto = 0

    botao_lan = None

    def jogada():
        global botao_lan
        botao_lan.destroy()
        bastao_branco, bastao_preto, resultado  = re.regras()
        label_branco.config(text=f"Branco: {bastao_branco}") 
        label_preto.config(text=f"Preto: {bastao_preto}") 
        return resultado

    def jogar():
        botao_com.destroy()
        em_jogo = True
        p=0
        while em_jogo == True:
            for p in range(2):
                if p==0:   
                    global botao_lan
                    botao_lan = tk.Button(jogadores_e_bastoes, text = "RODAR", command = jogada)
                    botao_lan.config(font = ("Arial", 14))
                    botao_lan.pack()
                em_jogo = False  

        
        
        
    cells = []
    cell_number = 1
    
    ###################celulas especiais#####################################
    image1 = tk.PhotoImage(file = "senet.png")
    image2 = tk.PhotoImage(file = "senet1.png")
    image3 = tk.PhotoImage(file = "senet2.png")
    image4 = tk.PhotoImage(file = "senet3.png")
    image5 = tk.PhotoImage(file = "senet4.png")
    image6 = tk.PhotoImage(file = "senet5.png")
    #########################################################################
    ####################CRIAR CELULAS########################################
    for row in range(3):
        row_cells = []
        for col in range(10):
            cell = tk.Button(board, text="", width=10, height=5)
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
            if cell_number == 15:
                cell.configure(image=image2, width=75, height=80)
            if cell_number == 26:
                cell.configure(image=image3, width=75, height=80)
            if cell_number == 27:
                cell.configure(image=image4, width=75, height=80)
            if cell_number == 28:
                cell.configure(image=image1, width=75, height=80)
            if cell_number == 29:
                cell.configure(image=image5, width=75, height=80)
            if cell_number == 30:
                cell.configure(image=image6, width=75, height=80)
            cells.append(cell_number)

##########################################################################
    
    white_piece = tk.PhotoImage(file = "white_piece.png")
    black_piece = tk.PhotoImage(file = "black_piece.png")

    
    def move_button(button):
        if button_clickable[button]:
            current_position = button_positions[button]
            resultado = jogada()
            new_position = current_position + resultado
            button_positions[button] = new_position
            button.place(x=dicionario[new_position][0], y=dicionario[new_position][1])
            

            if new_position >= 30:
                button_clickable[button] = False
                if button["image"] == white_piece:
                    pecas_out_branco += 1
                    label_branco.config(text=f"Branco: {pecas_out_branco}")
                elif button["image"] == black_piece:
                    pecas_out_preto += 1
                    label_preto.config(text=f"Preto: {pecas_out_preto}")
            resultado =0

    global resultado
    button_clickable = {}
    lambda_functions = []
    k=1
    lambda_functions = []
    k = 1
    for row in range(1):
        for col in range(10):
            celu = tk.Button(board, text = "", width = 20, height = 20)
            x_elemento = dicionario[k][0]
            y_elemento = dicionario[k][1]
            celu.place(x = x_elemento, y=y_elemento)

            button_positions[celu] = k  
            button_clickable[celu] = True

            if (row + col) % 2 == 0:
                celu.configure(image = white_piece)
            else:
                celu.configure(image = black_piece)
            
        # Definir a função lambda
            lambda_functions.append((celu, lambda button=celu: move_button(button)))
            k += 1
    print (button_positions)
    # Agora atribuímos as funções lambda aos botões
    for button, func in lambda_functions:
        button.configure(command=func)

            

    
###########################TELA###################################################
    jogadores_e_bastoes = tk.Frame(window)
    jogadores_e_bastoes.pack()
    
    jogador1_label = tk.Label(jogadores_e_bastoes, text=f"{jogadores['nome1']} (Pontuação: {pecas_out_branco})")
    jogador1_label.pack(side = tk.LEFT, padx = (10, 290))
    
    jogador2_label = tk.Label(jogadores_e_bastoes, text=f"{jogadores['nome2']} (Pontuação: {pecas_out_preto})")
    jogador2_label.pack(side = tk.RIGHT, padx = (290, 10))
    
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
    window.mainloop()
###############################################################################################


tab({'nome1' : "DAVID", 'nome2' : "Fidalgo"})