# Implemente em Python um algoritmo recursivo para o cálculo MDC  de dois números inteiros a e b.

# Entrada: Dois números inteiros a e b
# Saída: O valor de mdc (a,b)
# Exceções: Para o caso em que a = 0 e b = 0, informe que o mdc é "indeterminado".

def mdc(a,b):
    if a == 0 and b == 0:
        return "Indeterminado"
    elif b == 0:
        return a
    else:
        return mdc(b,a%b)

print(mdc(98,66))