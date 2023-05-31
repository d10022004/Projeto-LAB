import tkinter as tk


    

def exibir_vencedor(nome):
    def destroirjanelas():
        window_vencedor.destroy()
        window.destroy()
    
    window_vencedor = tk.Toplevel(window)
    window_vencedor.title("Vencedor")

    label_vencedor = tk.Label(window_vencedor, text=f"O jogador {nome} ganhou!")
    label_vencedor.pack(pady=50)

    button_fechar = tk.Button(window_vencedor, text="Fechar", command=destroirjanelas)
    button_fechar.pack()
    
        
window = tk.Tk()
window.title("Jogo")

# Aqui você pode adicionar outros elementos ou funcionalidades ao seu jogo...

# Exibindo o vencedor
exibir_vencedor("Leonardo")

# Iniciando o loop principal da janela
window.mainloop()






