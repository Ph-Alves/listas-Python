N = int(input("Digite um número para encontrar todos os primos até ele: "))

if N < 2:
    print("Não há números primos até", N)
else:
    primos = [True] * (N + 1)
    primos[0] = primos[1] = False

    for i in range(2, int(N**0.5) + 1):
        if primos[i]:
            for j in range(i * i, N + 1, i):
                primos[j] = False

    resultado = []
    for i in range(len(primos)):
        if primos[i]:
            resultado.append(i)

    print("Números primos até", N, ":", resultado)