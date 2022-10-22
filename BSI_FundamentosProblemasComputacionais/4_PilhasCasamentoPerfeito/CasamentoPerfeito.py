entrada = input()

abre = "([{"
fecha = ")]}"
tudo = "([{}])"

def casamento(entrada):
    contador1 = 0
    contador2 = 0
    pilha = []
    for elemento in entrada:
        if elemento in tudo:
            if elemento in abre:
                contador1 += 1
                pilha.append(elemento)
            elif elemento in fecha:
                contador2 += 1
                if len(pilha) > 0:
                    tira = pilha.pop()
                    if elemento == ")" and tira == "(":
                        continue
                    elif elemento == "]" and tira == "[":
                        continue
                    elif elemento == "}" and tira == "{":
                        continue
                    else:
                        break
    if len(pilha) == 0 and contador1 == contador2:
        return "casamento perfeito"
    else:
        return "casamento imperfeito"

print(casamento(entrada))