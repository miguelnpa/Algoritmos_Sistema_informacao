# Início do código
import time

def forca_bruta():
    caminhos = []
    custo = 0
    linha = 0
    controle = 0
    coluna = 0
    melhor_custo = float('inf')
    melhor_rota = ''
    dicionarioC = {}
    dicionario_inteiro = {}
    rota = []
    rota_real = []

    def leitura_arquivo():
        # arquivo = input("digite o nome do arquivo: ")
        arquivo = "matriz2.txt"
        f = open(arquivo, "r")
        for linha in f:
            linha_cortada = linha.strip()
            lista_linha = linha_cortada.split()
            caminhos.append(lista_linha)
        caminhos.pop(0)    
        f.close
        return caminhos
        # lista = [[0,0,0,0,D], [R,0,0,0,A] ... ]
# Nesse passo, estou gerando um dicionário usando cada letra com Key e as linhas e colunas como posição de distância.
    def salva_coordenadas_incompleta(caminhos):
        for i in caminhos:
            for x in i:
                if x != "0" and x!= "R":
                    dicionarioC[x] = caminhos.index(i), i.index(x)
        return dicionarioC

    def salva_coordenadas_completa(caminhos):
        for i in caminhos:  
            for x in i:            
                if x != "0":
                    dicionario_inteiro[x] = caminhos.index(i), i.index(x)
        return dicionario_inteiro

#Nesse passo eu fiz uma permutação com os caminhos possíveis da rota      
    
    def permutations(elementos):
        if len(elementos) <= 1:
            yield elementos
            return
        for perm in permutations(elementos[1:]):
            for i in range(len(elementos)):
                yield perm[:i] + elementos[0:1] + perm[i:]
    
    matriz = leitura_arquivo()
    coordenadas_incompleta = salva_coordenadas_incompleta(matriz)
    coordenadas_completa = salva_coordenadas_completa(matriz)
    # print(f"coordenada completa: {coordenadas_completa}")
    l = list(permutations(tuple(coordenadas_incompleta.keys())))

    for i in l:
        rota.append(list(i))
# Nesse passo eu adicionei o ponto de início e de fim da rota como sendo R

    for i in rota:
        rota_real.append(['R'] + i + ['R'])
# Nesse passo eu vou começar a calcular o melhor caminho possível

    linha_atual = coordenadas_completa["R"][0]
    coluna_atual = coordenadas_completa["R"][1]
    # calculo =  | linha1 - linha 2 | + | col1 - col2  | 
    # dicionario = {"D": (0, 4), ... }

    # lista = [[0,0,0,0,D], [R,0,0,0,A] ... ]
    for i in rota_real:
        custo = 0
        linha = 0
        coluna = 0 
        for x in i:
            controle = 0
            while (controle <= 1):
                if controle == 0:
                    linha = abs(linha_atual - coordenadas_completa[x][controle])
                    linha_atual = coordenadas_completa[x][controle]
                elif controle == 1:
                    coluna = abs(coluna_atual - coordenadas_completa[x][controle])
                    coluna_atual = coordenadas_completa[x][controle]
                controle += 1
            custo = custo + linha + coluna
        if (melhor_custo > custo):
            melhor_custo = custo
            melhor_rota = i
        else:
            melhor_custo = melhor_custo

    return print(melhor_custo) , print(" ".join(melhor_rota))

forca_bruta()
