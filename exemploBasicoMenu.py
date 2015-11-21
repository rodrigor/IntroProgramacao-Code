# Exemplo básico de um menu...


continuar = True
while continuar:
    print(" **** MENU ****")
    print("  [1] Opção 1")
    print("  [2] Opção 2")
    print("  [3] SAIR")
    opcao = input("Digite uma opção:")
    if opcao == "1":
        print("Você escolheu a opção 1")
    elif opcao == "2":
        print("Você escolheu a opção 2")
    elif opcao == "3":
        continuar = False
    else:
        print("Opção inválida: ", opcao)
print("Até a próxima!")


def eh_numero(valor):
    """
    Retorna True se e'
    :param valor: tipo String para ser verificado se é um número
    :return:
    """

mes = input("Digite um mês:")
mes.isnumeric()