def suc(n):
  return n + 1 if n > 0 else 0
  
def pred(n):
  return n - 1 if n > 0 else 0

def recursFunc (num1, num2):
  if num2 == 0:
    return num1
  return recursFunc(suc(num1), pred(num2))

resultado = recursFunc(8, 2)

print("O resultado da função recursiva é:", resultado)