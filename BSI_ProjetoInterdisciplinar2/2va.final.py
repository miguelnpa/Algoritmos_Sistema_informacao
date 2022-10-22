import time

caminhos = []

arquivo = input("digite o nome do arquivo: ")
# arquivo = "matriz4.txt"

f = open(arquivo, "r")
caminhos = []
for line in f:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    caminhos.append(line_list)
caminhos.pop(0)    
f.close

def vizinho_mais_proximo(caminhos):
    
    dicionarioC = {}
    dicionario_inteiro = {}

    for i in caminhos:
        for x in i:
            if x != "0" and x!= "R":
                dicionarioC[x] = caminhos.index(i), i.index(x)
    for i in caminhos:  
        for x in i:            
            if x != "0":
                dicionario_inteiro[x] = caminhos.index(i), i.index(x)
    

    pontos = list(dicionarioC.keys())

    linha_atual = dicionario_inteiro["R"][0]
    coluna_atual = dicionario_inteiro["R"][1]
    
    melhor_custo = float("inf")
    remover_ponto = ''
    total = 0
    rota = ''
    for i in range(len(pontos)):
        melhor_custo = float("inf")
        for x in pontos:
            custo = abs(linha_atual - dicionarioC[x][0]) + abs(coluna_atual - dicionarioC[x][1])
            if melhor_custo > custo:
                melhor_custo = custo
                remover_ponto = x
            else:
                melhor_custo = melhor_custo
        rota = rota + remover_ponto
        linha_atual = dicionarioC[remover_ponto][0]
        coluna_atual = dicionarioC[remover_ponto][1]
        total = total + melhor_custo
        pontos.remove(remover_ponto)
    
    custo = abs(linha_atual - dicionario_inteiro["R"][0]) + abs(coluna_atual - dicionario_inteiro["R"][1])
    rota = "R" + rota + "R"
    total = total + custo

    print(f"A Rota é: {rota}")
    print(f"O custo total da rota foi de: {total}")


vizinho_mais_proximo(caminhos)

