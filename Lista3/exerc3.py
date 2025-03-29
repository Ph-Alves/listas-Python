import random

print("Bem-vindo(a) ao jogo de adivinhação!! Você deve adivinhar um número de 0 a 100")
print("Lembre-se, você tem 10 tentativas!")
numeroAleatorio = random.randint(1, 100)

tentativas = 0
palpite = 0

while (tentativas != 10):
  palpite = int(input("Qual o seu palpite? "))
  if (palpite < numeroAleatorio):
    print("Você errou! O número é maior.")
  elif (palpite > numeroAleatorio):
    print("Você errou! O número é menor.")

  tentativas += 1
  
  if (palpite == numeroAleatorio):
    print("Parabéns!! Você acertou!")
    break
  elif (tentativas == 10):
    print("Você perdeu! O número era:", numeroAleatorio)
    break

