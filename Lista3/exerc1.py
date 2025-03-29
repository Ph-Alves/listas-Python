num = int(input("Digite um número: "))
somaPar = 0

for i in range(0, num):
  if (i % 2) == 0:
    somaPar += i;

print("Soma dos números pares: " + str(somaPar))