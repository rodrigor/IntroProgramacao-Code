import random

segredo = random.randint(1,99)

aposta = 0
tentativas = 0

QUANT_TENTATIVAS=6

print("Eu tenho um segredo...")
print("É um número de 1 a 99.")
print("Lhe darei",QUANT_TENTATIVAS,"chances para descobrir o número!")

while aposta != segredo and tentativas < QUANT_TENTATIVAS:
    aposta = int(input("Informe um número: "))
    if aposta < segredo:
        print("Número muito pequeno!")
    elif aposta > segredo:
        print("Número muito grande!")
    tentativas = tentativas + 1

if aposta == segredo:
    print("Parabéns! Você descobriu o número secreto!")
else:
    print("Sua chance acabou!")
    print("O número que pensei foi:",segredo)
