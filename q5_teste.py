string = input('Digite uma string: ')


def inverter(txt):
    return txt[::-1]


print(inverter(string))

# solução alternativa

# string = input('Digite uma string: ')

# letras = []
# invertidas = []

# for i in string:
#     letras.append(i)

# # percorre a lista de letras de trás para frente
# for i in range(len(string)-1, -1, -1):
#     invertidas.append(letras[i])

# # junta as letras da lista de invertidas formando uma string
# palavra_invertida = ''.join(invertidas)

# print(palavra_invertida)
