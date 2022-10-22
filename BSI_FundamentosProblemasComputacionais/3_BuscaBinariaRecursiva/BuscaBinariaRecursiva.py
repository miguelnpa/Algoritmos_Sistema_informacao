from math import floor

lista = []
string = input()
for i in string.split(" "):
    if i == '':
        continue
    else:
        lista.append(int(i))
buscado = lista.pop(0)
contador = 0

def buscaBinaria(buscado, lista):
    posicao = len(lista)//2
    global contador
    if posicao == 0 and lista[posicao] != buscado:
        contador += 1
        return contador 
    if lista[posicao] == buscado:
        contador += 1
        return contador
    if buscado > lista[posicao] and posicao != 0:
        contador += 1
        return buscaBinaria(buscado, lista[posicao + 1:])
    if buscado < lista[posicao] and posicao != 0:
        contador += 1
        return buscaBinaria(buscado, lista[:posicao]) 

print(buscaBinaria(buscado, lista))
