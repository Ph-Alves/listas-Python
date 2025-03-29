numero = int(input("Digite um número: "))
passos = 0
numStr = numero

while (numero != 1):
  if (numero % 2 == 0):
    numero /= 2
  else:
    numero = numero * 3 + 1
  passos += 1

print(f"O número {numStr} se tornou 1 após {passos} passos.")