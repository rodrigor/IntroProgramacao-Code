titulo = input("Digite o titulo:")
tamanho = int(input("Tamanho do titulo:"))

print("=" * tamanho)
margem = tamanho - len(titulo)
print(" " * margem, end="")
print(titulo)
print("=" * tamanho)
