frase = input("Digite uma frase: ")
vogais = "aeiou"
contador = 0

for letra in frase.lower():
  if letra in vogais:
    contador += 1

print(contador)