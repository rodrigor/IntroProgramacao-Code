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
    cabecalho("CADASTRAR NOTAS")
    global nota1, nota2, nota3
    nota1 = float(input("Nota 1:"))
    nota2 = float(input("Nota 2:"))
    nota3 = float(input("Nota 3:"))


def calcular_media():
    cabecalho("CALCULAR MEDIA")
    media = (nota1+nota2+nota3)/3
    print("A média é:", media)


def exibir_menu():
    opcao = 0
    while opcao != 3:
        print("**************************")
        print("*  [1] Cadastrar notas   *")
        print("*  [2] Calcular média    *")
        print("*  [3] Sair              *")
        print("**************************")
        opcao = int(input("Digite a opção:"))

        if opcao == 1:
            ler_notas()
        elif opcao == 2:
            calcular_media()
        elif opcao == 3:
            print("até a próxima!")
        else:
            print("Opção inválida!")


nota1 = 0.0
nota2 = 0.0
nota3 = 0.0
exibir_menu()