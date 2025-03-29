from unidecode import unidecode
from collections import Counter

primeiraFrase = input("Digite uma frase: ")
segundaFrase = input("Digite outra frase: ")

pFraseLimpa = "".join(char.lower() for char in unidecode(primeiraFrase) if char.isalnum())
sFraseLimpa = "".join(char.lower() for char in unidecode(segundaFrase) if char.isalnum())

if Counter(pFraseLimpa) == Counter(sFraseLimpa):
  print("As duas frases são anagramas")