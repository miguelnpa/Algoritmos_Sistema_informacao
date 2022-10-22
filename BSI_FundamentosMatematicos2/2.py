# Implemente um algoritmo recursivo para o cálculo da exponenecia a^n, com a sem um número qualquer ( positivo, negativo ou zero) e com expoente inteiro n >= 0. Observe com atenção o caso 0 ^ 0 que não pode ser calculado.

# Entrada: Uma base a que pode ser qualquer número ( inclusive negativo) Um expoente inteiro n>= 0
# Saída: O valor da exponencial a ^ n
# Exceções: Para o caso de 0^0 informe que é "impossível calcular"

def exponen(a,b):
    if a == b == 0:
        return "Impossível calcular"
    if b < 0:
        return "Expoente negativo não permitido"
    elif b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * exponen(a,b-1) 

print(exponen(0,0))