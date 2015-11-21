# Resolução da prova1: Solução 01
# Prof. Rodrigo Rebouças

# [Duas listas, sem função, sem validação]
# Nesta solução usamos duas listas para armazenar, separadamente,
# o nome do aluno e sua média

opcao = -1
alunos = []
medias = []

while opcao != 0:
    print("*** MENU ***")
    print("[1] Cadastrar aluno")
    print("[2] Listar alunos")
    print("[3] Maior média?")
    print("[4] Menor média?")
    print("[5] Média dos alunos?")
    print("[6] Buscar alunos")
    print("[0] Sair")
    print("*************")
    opcao = int(input("Digite sua opção:"))
    if opcao == 1:
        print("")
        print("** 1-Cadastrar Aluno")
        nome = input("Nome:")
        media = float(input("Média:"))
        alunos.append(nome)
        medias.append(media)

    elif opcao == 2:
        print("")
        print("** 2-Listar Alunos")
        for i in range(len(alunos)):
            print(alunos[i], ":", medias[i])

    elif opcao == 3:
        print('')
        print('** 3-Maior Média')
        indiceMaior = 0
        for i in range(len(medias)):
            if medias[i] > medias[indiceMaior]:
                indiceMaior = i
            print("medias[indiceMaior]:", medias[indiceMaior])
        print(alunos[indiceMaior], ":", medias[indiceMaior])

    elif opcao == 4:
        print("")
        print("** 4-Menor Média")
        indiceMenor = 0
        for i in range(len(medias)):
            if medias[i] < medias[indiceMenor]:
                indiceMenor = i
        print(alunos[indiceMenor], ":", medias[indiceMenor])

    elif opcao == 5:
        print("")
        print("** 5-Média dos alunos")
        soma = 0
        for nota in medias:
            soma += nota
        media = soma / len(medias)
        print("A média dos alunos é:", media)

    elif opcao == 6:
        print("")
        print("** 6-Buscar alunos")
        nome = input("Nome do aluno:")
        indiceAluno = -1
        for i in range(len(alunos)):
            if (alunos[i] == nome):
                indiceAluno = i
                break
        if indiceAluno != -1:
            print("Aluno encontrado:", alunos[indiceAluno], ", média:", medias[indiceAluno])
        else:
            print("Aluno não encontrado:", nome)
