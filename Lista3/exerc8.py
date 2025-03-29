n = int(input("Digite um número maior que 3: "))

if n <= 3:
  print("O número fornecido não é maior que 3.")

fib = [0, 1]

for i in range(2, n):
  fib.append(fib[i - 1] + fib[i - 2])

print(fib)
