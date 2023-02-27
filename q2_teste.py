def calcula_fib():
    # Calcula até a posição 60 na sequência de fibonacci
    fib = [0, 1]
    for i in range(60):
        prox = fib[i] + fib[i+1]
        fib.append(prox)

    return fib


# solicina um valor ao usuário
entrada = int(input("Insira um valor: "))


def verifica_entrada(valor):
    # verifica a condicional se o número informado pertence à sequencia de fib
    fib = calcula_fib()
    if valor in fib:
        return f'O número {entrada} pertence à sequência de fibonacci!'

    return f'O número {entrada}, não pertence à sequência de fibonacci'


print(verifica_entrada(entrada))
