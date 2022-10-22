# Implemente em Python um algoritmo recursivo para o cálculo do fatorial n!, com n sendo um número inteiro. Fatoriais de números negativos são nulos. 

# Entrada: Um número inteiro n 
# Saída: O valor do fatorial n!
# Exceções para n < 0, retorne n! = 0

def fatorial(n):
    if n < 0:
        return 0 
    elif n == 0:
        return 1
    else:
        return n*fatorial(n-1)

print(fatorial(5))