

def ler_continua():
    opcao = ""
    while True:
        opcao = input("Continua? [s/n]")
        if opcao == "s":
            return True
        elif opcao == "n":
            return False
        else:
            print("Opção inválida!")


continua = True
nomes = []

while continua:
    nome = input("Digite o nome:")
    nomes.append(nome)
    continua = ler_continua()

for n in nomes:
    print(n)
