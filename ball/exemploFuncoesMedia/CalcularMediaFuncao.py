def calc_media(a, b, c):
    return (a + b + c) / 3


def titulo(texto):
    tam = 20
    print("*" * tam)
    print(centralizar(texto, tam))
    print("*" * tam)


def centralizar(texto, tam):
    margem = int((tam - len(texto)) / 2)
    espaco = " " * margem
    return espaco + texto + espaco


def valor_valido(valor, min, max):
    if valor > max or valor < min:
        return False
    return True


def ler_entrada(msg):
    while True:
        entrada = float(input(msg))
        if valor_valido(entrada, 0, 10):
            return entrada
        else:
            print("Entrada inválida!")


titulo("Bem vindo")

titulo("Calculador de Media")
nota1 = ler_entrada("Digite a nota 1:")
nota2 = ler_entrada("Digite a nota 2:")
nota3 = ler_entrada("Digite a nota 3:")

media = calc_media(nota1, nota2, nota3)
print("A média é:", media)
