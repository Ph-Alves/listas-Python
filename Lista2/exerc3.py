# d1,2 = raiz(x − x )2 + (y − y )2
import math as mt

x1 = int(input("digite X1: "))
x2 = int(input("digite X2: "))
y1 = int(input("digite Y1: "))
y2 = int(input("digite Y2: "))

d1 = mt.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))

print("distância entre os pontos é: ", d1)