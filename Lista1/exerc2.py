n = int(input("Digite o número que quer elevar ao quadrado: "))
soma = 0;
impar = 1;

for i in range(n):
  soma += impar;
  impar += 2;

print("O quadrado do número é: " + str(soma))