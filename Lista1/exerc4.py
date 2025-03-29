Torre1 = [5,4,3,2,1]
Torre2 = []
Torre3 = []

def recursMover(torre1, torre2, torre3, disco):
  if disco == 1:
    print("Mover disco 1 de Torre", torre1, "para Torre", torre3)
    torre3.append(torre1.pop())
    print("Torre 1:" + str(Torre1))
    print("Torre 2:" + str(Torre2))
    print("Torre 3:" + str(Torre3))
  else:
    recursMover(torre1, torre3, torre2, disco-1)
    print("Mover disco", disco, "de Torre", torre1, "para Torre", torre3)
    torre3.append(torre1.pop())
    recursMover(torre2, torre1, torre3, disco-1)

print("Bem vindo(a) ao problema da torre de hanoi! Você deve mover os discos para a terceira torre usando uma torre auxiliar")
print("Torre 1:" + str(Torre1))
print("Torre 2:" + str(Torre2))
print("Torre 3:" + str(Torre3))

recursMover(Torre1, Torre2, Torre3, len(Torre1))