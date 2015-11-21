def linha(tam):
  print(" ",end="")
  for i in range(tam):
    print("-",end="")
  print(" ")
  
def textoCentralizado(texto,tam):
  print("|",end="")
  margem = int((tam - len(texto)) / 2)
  for d in range(margem):
    print(" ",end="")
  print(texto,end="")
  for e in range(margem):
    print(" ",end="")
  if (len(texto) % 2) != 0: # para o caso de texto com números ímpares de caracteres
    print(" ",end="")
  print("|")


nome = input("Digite o texto:")
tam=80
linha(tam)
textoCentralizado(nome,tam)
linha(tam)
