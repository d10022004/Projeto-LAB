#NAO APARECE NADA DO FICHEIRO DAS REGRAS

import os
import tkinter as tk
import random
import keyboard #IMPORT DE KEYBOARD PARA O MACRO
import regras as re
import pygame

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

def tab(jogadores):
    botao_bastao = None
    janela_pausa = None
    lancamento = 0
    
    def hist_poicoes(row, col):
        print("Posicao celula clicada:", row, col)

    def verifica(): 
        global resultado
        if resultado == 0:
            print ("OLA")    
    
    def rodar_batoes():
        bastoes = [random.choice(["Branco", "Preto"]) for _ in range(4)]
    
        contador_branco = bastoes.count("Branco")
        contador_preto = bastoes.count("Preto")   
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
    
    window = tk.Tk()
    window.geometry("800x400")
    window.title("Tabuleiro")
    
    board = tk.Frame(window)
    board.pack()
    def jogar ():
        botao_com.destroy()
        def ola():
            botao_lan.destroy()
            bastao_preto, bastao_branco, resultado  = re.regras()
            label_branco.config(text=f"Branco: {bastao_branco}") 
            label_preto.config(text=f"Preto: {bastao_preto}") 
            print (bastao_preto, bastao_branco, resultado)
        em_jogo = True
        p=0
        while em_jogo == True:
            for p in range(2):
                if p==0:   
                    botao_lan = tk.Button(jogadores_e_bastoes, text = "RODAR", command = ola)
                    botao_lan.config(font = ("Arial", 16))
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
    ########################################################################3
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
                cell.configure(image = image1, width=75, height=80) 
            if cell_number == 26:
                cell.configure(image = image2, width=75, height=80)
            if cell_number == 27:
                cell.configure(image = image3, width=75, height=80)
            if cell_number == 28:
                cell.configure(image = image4, width=75, height=80)
            if cell_number == 29:
                cell.configure(image = image5, width=75, height=80)
            if cell_number == 30:
                cell.configure(image = image6, width=75, height=80)
            cells.append(cell_number)
        print (cells)



    tabuleiro = tk.Frame(window, bg = 'White')
    tabuleiro.pack(fill=tk.BOTH, expand = True)
   
    
    white_piece = tk.PhotoImage(file = "white_piece.png")
    black_piece = tk.PhotoImage(file = "black_piece.png")
    def move_button(button, new_position):
        """Move o botão para uma nova posição."""
        button.grid(row=new_position // 10, column=new_position % 10)


    lambda_functions = []
    k=1
    for row in range(1):
        row_celub = []
        row_celup = []
        for col in range(10):
            # Primeiro criamos o botão sem especificar a função command
            celu = tk.Button(board, text = "", width = 20, height = 20)
            x_elemento = dicionario[k][0]
            y_elemento = dicionario[k][1]
            celu.place(x = x_elemento, y=y_elemento)
        
            button_positions[celu] = k  # Armazena a posição do botão no dicionário button_positions

            if (row + col) % 2 == 0:
                celu.configure(image = white_piece)
                row_celub.append(celu)
            else:
                celu.configure(image = black_piece)
                row_celup.append(celu)
            
            # Cria a função lambda e adiciona-a à lista lambda_functions
            lambda_functions.append((celu, lambda button=celu, new_position=k+4: move_button(button, new_position)))
            
            k +=1

    # Agora atribuímos as funções lambda aos botões
    for button, func in lambda_functions:
        button.configure(command=func)

            

    
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
    window.mainloop()
tab ({'nome1': 'dsgfdaf', 'nome2': 'BOT'})