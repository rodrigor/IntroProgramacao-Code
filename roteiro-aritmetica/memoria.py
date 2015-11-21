import random
import time


# Imprime várias linhas em branco para limpar a tela do terminal
def limpar_tela():
    for i in range(50):
        print()


def imprimir(tab):
    """
    Imprime o tabuleiro na tela
    :param tab: lista que representa o tabuleiro exibido para o usuário
    """
    numeros = ""
    saida = ""
    n = 0
    for carta in tab:
        numeros += " {} ".format(n)
        n+=1
        saida += "[" + carta + "]"
    print(numeros)
    print(saida)


def fim_jogo(tab):
    """
    Define se é fim de jogo
    O fim do jogo acontece se nenhuma das posições do tabuleiro for vazia
    :param tab: lista que representa o tabuleiro exibido para o usuário
    :return: True, se nenhuma das posições do tabuleiro é vazia, False, caso contrário.
    """
    for carta in tab:
        if carta == VAZIO:
            return False
    return True


def mostrar_carta(posicoes, tab):
    """
    Mostra as cartas das posições na lista "posicoes"
    :param posicoes: lista de posições que devem ser exibidas
    :param tab: lista que representa o tabuleiro exibido para o usuário
    """
    saida = ""
    for i in range(len(tab)):
        c = ""
        if i in posicoes:
            c = cartas[i]
        else:
            c = tab[i]
        saida += "[" + c + "]"
    print(saida)


def montar_jogo():
    """
    Inicializa o tabuleiro que será exibido para o usuário
    e embaralha as cartas
    :return:
    """
    random.shuffle(cartas)
    for i in cartas:
        tabuleiro.append(VAZIO)


VAZIO = " "
cartas = ["A", "A", "B", "B", "C", "C", "D", "D", "E", "E"]
tabuleiro = []

montar_jogo()
imprimir(cartas)
while not fim_jogo(tabuleiro):
    limpar_tela()
    imprimir(tabuleiro)
    pos_1 = int(input("Digite uma posição:"))
    mostrar_carta([pos_1], tabuleiro)
    pos_2 = int(input("Digite uma posição:"))
    mostrar_carta([pos_1, pos_2], tabuleiro)
    if cartas[pos_1] == cartas[pos_2]:
        tabuleiro[pos_1] = cartas[pos_1]
        tabuleiro[pos_2] = cartas[pos_2]
    else:
        print("Memorize...")
        time.sleep(3)

print("FIM DE JOGO")


