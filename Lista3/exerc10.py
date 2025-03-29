palavras = input("Digite uma lista de palavras separadas por espaço: ").split()
termo = input("Digite o termo a ser buscado: ")

encontrado = False
for i in range(len(palavras)):
  if palavras[i] == termo:
    print(f"A palavra '{termo}' foi encontrada no índice {i}.")
    encontrado = True
    break

if not encontrado:
  print(f"A palavra '{termo}' não foi encontrada.")
