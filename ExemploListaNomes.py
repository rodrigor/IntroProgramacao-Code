
continua = True
nomes = []

while continua:
    nome = input("Digite o nome:")
    nomes.append(nome)
    opcaoInvalida = True
    opcao = ""
    while opcaoInvalida:
        opcao = input("Continua? [s/n]")
        if opcao == "s" or opcao == "n":
            opcaoInvalida = False
        else:
            print("Opção inválida!")
    if opcao == "n":
        continua = False

for n in nomes:
    print(n)
