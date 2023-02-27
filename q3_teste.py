import json


def busca_dados() -> list:
    with open('dados.json', 'r', encoding='utf8') as arquivo:
        dados_convert = json.load(arquivo)
    return dados_convert


def cria_lista_de_valores(lista) -> list:
    valores = []
    for chave in lista:
        valores.append(chave['valor'])
    return valores


def removendo_zeros(lista) -> list:
    try:
        while True:
            lista.remove(0)
    except ValueError:
        pass

    return lista


dados = busca_dados()
lista_de_valores = cria_lista_de_valores(dados)
lista_sem_zeros = removendo_zeros(lista_de_valores)

menor_faturamento = min(lista_sem_zeros)
maior_faturamento = max(lista_sem_zeros)


# calculando média do faturamento
def calcula_media_faturamento():
    soma_faturamento = 0
    for i in lista_sem_zeros:
        soma_faturamento += i
    faturamento_medio = soma_faturamento / len(lista_sem_zeros)
    return faturamento_medio


faturamento_medio = calcula_media_faturamento()

# somatório de dias que superam o faturamento médio
dias_que_superam_media = 0
for i in lista_sem_zeros:
    if i >= faturamento_medio:
        dias_que_superam_media += 1
    continue

print(f'O menor faturamento foi de: {menor_faturamento}')
print(f'O maior faturamento foi de: {maior_faturamento}')
print(f'A quantidade de dias que superam o faturamento médio é: {dias_que_superam_media}')

# alternativas de MIN e MAX

# menor = lista_sem_zeros[0]
# for i in lista_sem_zeros:
#     if i < menor:
#         menor = i

# print(menor)

# maior = lista_sem_zeros[0]
# for i in lista_sem_zeros:
#     if i > maior:
#         maior = i

# print(maior)
