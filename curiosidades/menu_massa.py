"""
Universidade Federal da Paraíba
Departamento de Ciências Exatas
Disciplina: Introdução à Programação
Professor: Rodrigo Rebouças de Almeida
           http://rodrigor.dcx.ufpb.br

Este programa mostra o uso de funções para construir um
menu genérico, que utiliza caracteres ASCII especiais para
fazer as bordas.

Data: 17/05/2015
"""


def eh_par(num):
    return num % 2 == 0


def maior_len(lista):
    maior = 0
    for texto in lista:
        if len(texto) > maior:
            maior = len(texto)
    return maior


def centralizar(texto, tam):
    tam_margem = (tam - len(texto)) // 2
    margem_esq = " " * tam_margem
    margem_dir = margem_esq
    if not eh_par(tam) or not eh_par(len(texto)):
        margem_dir += " "
    return margem_esq+texto+margem_dir


def esquerda(texto, tam, margem = 0):
    tam_margem_dir = tam - (len(texto)+margem)
    margem_esq = " " * margem
    margem_dir = " " * tam_margem_dir
    return margem_esq+texto+margem_dir


def print_menu(titulo, opcoes = []):
    margem = 3
    tam = maior_len(opcoes)
    if len(titulo) > tam:
        tam = len(titulo)
    tam += (margem * 2)

    print()
    print()
    print('╔', end="")
    print('═' * tam, end="")
    print('╗')

    print('║', end="")
    print(centralizar(titulo,tam), end="")
    print('║')

    if len(opcoes) != 0:
        print('╟', end="")
        print('─' * tam, end="")
        print('╢')
        for opcao in opcoes:
            print('║', end="")
            print(esquerda(opcao,tam,margem), end="")
            print('║')

    print('╚', end="")
    print('═' * tam, end="")
    print('╝')


titulo = "Exemplo Menu"
opcoes = ["[1] Opção 1", "[2] Opção 2", "[x] Sair"]

continuar = True
while continuar:
    print_menu(titulo,opcoes)
    opcao = input("Opção:")
    if opcao.lower() == "x":
        print("Até a próxima!")
        continuar = False
    elif opcao == "1":
        print("Você escolheu a opção 1")
    elif opcao == "2":
        print("Você escolheu a opção 2")
    else:
        print(">> Opção inválida: ", opcao)
