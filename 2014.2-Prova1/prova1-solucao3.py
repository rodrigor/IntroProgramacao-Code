# Resolução da prova1: Solução 01
# Prof. Rodrigo Rebouças

# [Uma lista, com função, sem validação]
# Nesta solução usamos uma lista para armazenar
# o nome e a média do aluno e usamos funções. O nome do aluno
# fica armazenado na primeira posição de cada elemento
# e a média do aluno fica armazenado na segunda posição


def menu():
    """
    Exibe um menu contendo várias opções
    """
    opcoes = ['1', '2', '3', '4', '5', '6', '0']
    textos = ['Cadastrar aluno',
              'Listar alunos',
              'Maior média?',
              'Menor média?',
              'Média dos alunos?',
              'Buscar alunos',
              'Sair']

    print("*** MENU ***")
    for i in range(len(opcoes)):
        print("[{0}] {1}".format(opcoes[i], textos[i]))
    print("*************")
    while True:
        opcao = input("Digite sua opção:")
        if opcao in opcoes:
            return opcao
        else:
            print("> ERRO: Entrada inválida")


def titulo(texto):
    print("")
    print("** {0}".format(texto))


NOME = 0  # Variável que representa a posiçao do nome em cada elemento da lista
MEDIA = 1  # Variável que representa a posição da média em cada elemento da lista

opcao = -1
alunos = []


def cadastrarAluno():
    global nome, media
    titulo("1-Cadastrar Aluno")
    nome = input("Nome:")
    media = float(input("Média:"))
    alunos.append([nome, media])


def listar_alunos():
    global aluno
    titulo("2-Listar Alunos")
    for aluno in alunos:
        print(alunos[NOME], ":", alunos[MEDIA])


def maior_media():
    global i
    titulo('3-Maior Média')
    indiceMaior = 0
    for i in range(len(alunos)):
        if alunos[i][MEDIA] > alunos[indiceMaior][MEDIA]:
            indiceMaior = i
    print(alunos[indiceMaior][NOME], ":", alunos[indiceMaior][MEDIA])


def menor_media():
    global i
    titulo('4-Menor Média')
    indiceMenor = 0
    for i in range(len(alunos)):
        if alunos[i][MEDIA] < alunos[indiceMenor][MEDIA]:
            indiceMenor = i
    print(alunos[indiceMenor][NOME], ":", alunos[indiceMenor][MEDIA])


def media_alunos():
    global aluno, media
    titulo('5-Média dos alunos')
    soma = 0
    for aluno in alunos:
        soma += aluno[MEDIA]
    media = soma / len(alunos)
    print("A média dos alunos é:", media)


def buscar_alunos():
    global nome, i
    titulo('** 6-Buscar alunos')
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


while opcao != 0:
    opcao = int(menu())
    if opcao == 1:
        cadastrarAluno()

    elif opcao == 2:
        listar_alunos()

    elif opcao == 3:
        maior_media()

    elif opcao == 4:
        menor_media()

    elif opcao == 5:
        media_alunos()

    elif opcao == 6:
        buscar_alunos()

print('> Até a próxima!')