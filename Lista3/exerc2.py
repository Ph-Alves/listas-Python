lado = int(input("Digite o tamanho do lado do quadrado: "))

for linha in range(lado):
    for coluna in range(lado):
      if linha == 0 or coluna == 0 or coluna == lado - 1 or linha == lado - 1:
        print("*", end="")
      else:
        print(" ", end="")
    print()
