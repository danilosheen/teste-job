estado = ['SP', 'RJ', 'MG', 'ES', 'Outros']
faturamento = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]


def calcula_total(lista_faturamento):
    valor_total = 0
    for i in lista_faturamento:
        valor_total += i
    return valor_total


def calcula_porcentagem(valor, total):
    return (valor*100)/total


valor_total = calcula_total(faturamento)

for i in range(len(estado)):
    porcentagem = calcula_porcentagem(faturamento[i], valor_total)
    print(f'A porcentagem de {estado[i]} é de {porcentagem}%')
