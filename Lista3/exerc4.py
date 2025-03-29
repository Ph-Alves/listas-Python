from unidecode import unidecode

palavra = input("Digite um palíndromo: ")
palavraLimpa = "".join(char.lower() for char in unidecode(palavra) if char.isalnum())
inverso = "".join(reversed(palavraLimpa))

print(palavraLimpa)
print(inverso)

if palavraLimpa == inverso:
  print("A palavra é um palíndromo.")
else:
  print("A palavra não é um palíndromo.")