# Universidade Federal da Paraíba
# Departamento de Ciências Exatas
# Introdução à Programação
# Prof.: Rodrigo Rebouças de Almeida
#        http://rodrigor.dcx.ufpb.br
#
#
#  Exemplo básico de um menu, com uso de funções


def cabecalho(titulo):
    TAM = 30
    print("*" * (TAM+2))
    margem = (TAM - len(titulo)) // 2
    print("*", end="")
    print(" " * margem, end="")
    print(titulo, end="")
    print(" " * margem, end="")
    if len(titulo) % 2 != 0:
        print(" ", end="")
    print("*")
    print("*" * (TAM+2))


def ler_notas():
    notas = []
    notas.append(float(input("Nota 1:")))
    notas.append(float(input("Nota 2:")))
    notas.append(float(input("Nota 3:")))
    return notas


def calcular_media(valores) -> float:
    total = 0.0
    quant = len(valores)
    for i in range(quant):
        total += valores[i]
    return total / quant


def exibir_menu():
    opcao = 0
    notas = []
    while opcao != 3:
        print("**************************")
        print("*  [1] Cadastrar notas   *")
        print("*  [2] Calcular média    *")
        print("*  [3] Sair              *")
        print("**************************")
        opcao = int(input("Digite a opção:"))

        if opcao == 1:
            cabecalho("CADASTRAR NOTAS")
            notas = ler_notas()
        elif opcao == 2:
            cabecalho("CALCULAR MEDIA")
            print("A média é:", calcular_media(notas))
        elif opcao == 3:
            print("até a próxima!")
        else:
            print("Opção inválida!")


exibir_menu()