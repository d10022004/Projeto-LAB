import tkinter as tk

class Calculadora:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Calculadora")

        # Entrada
        self.entrada = tk.Entry(self.janela, width=35, borderwidth=5)
        self.entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Botões
        self.botao_1 = self.criar_botao("1", 1, 0)
        self.botao_2 = self.criar_botao("2", 1, 1)
        self.botao_3 = self.criar_botao("3", 1, 2)
        self.botao_4 = self.criar_botao("4", 2, 0)
        self.botao_5 = self.criar_botao("5", 2, 1)
        self.botao_6 = self.criar_botao("6", 2, 2)
        self.botao_7 = self.criar_botao("7", 3, 0)
        self.botao_8 = self.criar_botao("8", 3, 1)
        self.botao_9 = self.criar_botao("9", 3, 2)
        self.botao_0 = self.criar_botao("0", 4, 1)

        self.botao_somar = self.criar_botao("+", 1, 3)
        self.botao_subtrair = self.criar_botao("-", 2, 3)
        self.botao_multiplicar = self.criar_botao("*", 3, 3)
        self.botao_dividir = self.criar_botao("/", 4, 3)

        self.botao_limpar = self.criar_botao("C", 4, 0)
        self.botao_igual = self.criar_botao("=", 4, 2)

    def criar_botao(self, texto, linha, coluna):
        botao = tk.Button(self.janela, text=texto, padx=40, pady=20, command=lambda: self.clicar_botao(texto))
        botao.grid(row=linha, column=coluna)
        return botao

    def clicar_botao(self, texto):
        if texto == "C":
            self.entrada.delete(0, tk.END)
        elif texto == "=":
            resultado = eval(self.entrada.get())
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, resultado)
        else:
            self.entrada.insert(tk.END, texto)

    def iniciar(self):
        self.janela.mainloop()

# Cria a calculadora
calculadora = Calculadora()

# Inicia a calculadora
calculadora.iniciar()
