# Definir tamanho do tabuleiro de xadrez
fila = 3
colunas =10

# Função para localizar quadrados
def localizar_quadrados():
    quadrados = []
    quadrado=0
    for i in range(3):
        for j in range(10):
            quadrado = quadrado+1
            quadrados.append(quadrado)
    return quadrados

# Chamada da função para obter os quadrados
quadrados_xadrez = localizar_quadrados()

# Imprimir os quadrados

print(quadrados_xadrez)