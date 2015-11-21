def imc(peso, altura):
    return peso / altura ** 2

alt = float(input("Digite sua altura:"))
pes = float(input("Digite seu peso:"))
print("Seu IMC é", imc(pes, alt))
