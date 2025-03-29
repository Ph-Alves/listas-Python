def criptografar(numero):
    numero_str = str(numero).zfill(4)
    digitos = [int(d) for d in numero_str]

    digitos = [(d + 7) % 10 for d in digitos]

    digitos[0], digitos[2] = digitos[2], digitos[0]
    digitos[1], digitos[3] = digitos[3], digitos[1]

    return "".join(map(str, digitos))

def descriptografar(numero):
    numero_str = str(numero).zfill(4)
    digitos = [int(d) for d in numero_str]

    digitos[0], digitos[2] = digitos[2], digitos[0]
    digitos[1], digitos[3] = digitos[3], digitos[1]

    digitos = [(d + 10 - 7) % 10 for d in digitos]

    return "".join(map(str, digitos))

numero_original = input("Digite um número de 4 dígitos para criptografar: ")

if len(numero_original) != 4 or not numero_original.isdigit():
    print("Erro: Digite um número válido de 4 dígitos.")
else:
    numero_criptografado = criptografar(numero_original)
    print(f"Número criptografado: {numero_criptografado}")

    numero_descriptografado = descriptografar(numero_criptografado)
    print(f"Número descriptografado: {numero_descriptografado}")
