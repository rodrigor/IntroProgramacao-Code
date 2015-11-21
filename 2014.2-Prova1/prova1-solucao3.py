# Resolução da prova1: Solução 01
# Prof. Rodrigo Rebouças

# [Uma lista, com função, sem validação]
# Nesta solução usamos uma lista para armazenar
# o nome e a média do aluno e usamos funções. O nome do aluno
# fica armazenado na primeira posição de cada elemento
# e a média do aluno fica armazenado na segunda posição


def menu():
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



NOME = 0 # Variável que representa a posiçao do nome em cada elemento da lista
MEDIA = 1 # Variável que representa a posição da média em cada elemento da lista

opcao = -1
alunos = []
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
        alunos.append([nome,media])

    elif opcao == 2:
        print("")
        print("** 2-Listar Alunos")
        for aluno in alunos:
            print(alunos[NOME], ":", alunos[MEDIA])

    elif opcao == 3:
        print('')
        print('** 3-Maior Média')
        indiceMaior = 0
        for i in range(len(alunos)):
            if alunos[i][MEDIA] > alunos[indiceMaior][MEDIA]:
                indiceMaior = i
        print(alunos[indiceMaior][NOME], ":", alunos[indiceMaior][MEDIA])

    elif opcao == 4:
        print("")
        print("** 4-Menor Média")
        indiceMenor = 0
        for i in range(len(alunos)):
            if alunos[i][MEDIA] < alunos[indiceMenor][MEDIA]:
                indiceMenor = i
        print(alunos[indiceMenor][NOME], ":", alunos[indiceMenor][MEDIA])

    elif opcao == 5:
        print("")
        print("** 5-Média dos alunos")
        soma = 0
        for aluno in alunos:
            soma += aluno[MEDIA]
        media = soma / len(alunos)
        print("A média dos alunos é:", media)

    elif opcao == 6:
        print("")
        print("** 6-Buscar alunos")
        nome = input("Nome do aluno:")
        indiceAluno = -1
        for i in range(len(alunos)):
            if alunos[i][NOME] == nome:
                indiceAluno = i
                break
        if indiceAluno != -1:
            print("Aluno encontrado:", alunos[indiceAluno][NOME], ", média:", alunos[indiceAluno][MEDIA])
        else:
            print("Aluno não encontrado:", nome)
