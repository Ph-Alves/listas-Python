start = int(input("Digite o valor inicial do intervalo: "))
end = int(input("Digite o valor final do intervalo: "))

print(f"Números de Armstrong no intervalo de {start} a {end}:")
for num in range(start, end + 1):
  num_str = str(num)
  num_digits = len(num_str)
  
  sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
  
  if sum_of_powers == num:
    print(num)