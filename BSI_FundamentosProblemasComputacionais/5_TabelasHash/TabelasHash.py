string = input()
lista_string = []


lista_string = string.split()

for i in range(len(lista_string)):
    lista_string[i] = int(lista_string[i])

QTDE_CONTAINERS = lista_string.pop(0)
TAM_CONTAINER = lista_string.pop(0)
QTDE_INSERCOES = lista_string.pop(0)        

controle = 0
lista_Hash = [None]*TAM_CONTAINER*QTDE_CONTAINERS

for i in range(QTDE_INSERCOES):
    alocacao = (lista_string[i] % QTDE_CONTAINERS) * 3
    if lista_Hash[alocacao] == None:
        lista_Hash[alocacao] = lista_string[i]
    else:
        controle = 0
        while controle < TAM_CONTAINER:
            if lista_Hash[alocacao] != None:
                alocacao = alocacao + 1
                controle += 1
            else:
                lista_Hash[alocacao] = lista_string[i]
                break
saida = ''
saida_string = ''
for i in lista_string[QTDE_INSERCOES:]:
    comparacoes = 0
    alocacao = i % QTDE_CONTAINERS * 3
    if lista_Hash[alocacao] == i:
        comparacoes = comparacoes + 1
    elif lista_Hash[alocacao] == None:
        comparacoes = comparacoes + 1
    else:
        controle = 0
        while controle < TAM_CONTAINER:
            if lista_Hash[alocacao] != i:
                alocacao = alocacao + 1
                comparacoes = comparacoes + 1
                controle += 1
            else:
                
                comparacoes += 1
                break
    saida = saida + f"{comparacoes}" + " "
saida_string += saida
saida_string = saida_string.strip()
print(saida_string)