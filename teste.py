import tkinter as tk
i=25
def mover_botao():
    global i
    ola = 1
    i = i+10
    # Move o botão para a coordenada (50, 50)
    botao.place(x=ola*i, y=ola*i)

# Cria a janela principal
window = tk.Tk()
window.geometry("400x400")
window.title("Mover Botão")

# Cria o botão inicial na coordenada (30, 20)
botao = tk.Button(window, text="Botão")
botao.place(x=30, y=20)

# Botão para mover o botão
botao_mover = tk.Button(window, text="Mover Botão", command=mover_botao)
botao_mover.pack(pady=10)

# Inicia a aplicação
window.mainloop()