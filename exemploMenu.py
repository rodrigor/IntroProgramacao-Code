# Universidade Federal da Paraíba
# Departamento de Ciências Exatas
# Introdução à Programação
# Prof.: Rodrigo Rebouças de Almeida
#        http://rodrigor.dcx.ufpb.br
#
#
#  Exemplo básico de um menu, sem uso de funções

nota1 = 0.0
nota2 = 0.0
nota3 = 0.0
opcao = 0
while opcao != 3:
    print("**************************")
    print("*  [1] Cadastrar notas   *")
    print("*  [2] Calcular média    *")
    print("*  [3] Sair              *")
    print("**************************")
    opcao = int(input("Digite a opção:"))

    if opcao == 1:
        print("**************************")
        print("*     CADASTRAR NOTAS    *")
        print("**************************")
        nota1 = float(input("Nota 1:"))
        nota2 = float(input("Nota 2:"))
        nota3 = float(input("Nota 3:"))
    elif opcao == 2:
        print("**************************")
        print("*     CALCULAR MÉDIA     *")
        print("**************************")
        media = (nota1+nota2+nota3)/3
        print("A média é:", media)
    elif opcao == 3:
        print("FIM: Até a próxima!")
    else:
        print("Opção inválida!")
