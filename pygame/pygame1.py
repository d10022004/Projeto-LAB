from tkinter import *

janela = Tk()
janela.title("SENET")
def iniciarjogo():
    print ("ola")

def carregajogo():
    print ("OLA AGAIN")
def sair():
    return 0

texto_op = Label(janela, text="\t\tMENU\t\t\t\n")
texto_op.grid (column=0, row=0)

iniciarjogo = Button (janela, text="Iniciar jogo", command=iniciarjogo())
iniciarjogo.grid (column=0, row=1)
carregarjogo = Button (janela, text="Carregar jogo", command=carregajogo())
carregarjogo.grid (column=0, row=3)
sair = Button (janela, text="Sair",command = sair())
sair.grid (column=0, row=4)
janela.mainloop()
