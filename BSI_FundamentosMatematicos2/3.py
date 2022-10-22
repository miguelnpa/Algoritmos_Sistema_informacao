# Implemente um algoritmo recursivo para o cálculo da exponencial modular a ^ n mod m, com a sendo um número inteiro qualquer ( positivo, negativo ou zero), com expoente inteiro n >= 0 e com módulo inteiro m >= 2.
# Entrada: Uma base a que pode ser qualquer número inteiro ( inclusive negativo)
        #   Um expoente inteiro n>= 0
        #   Um módulo inteiro m >= 2
# Saída: O valor da exponencial modular a^2 mod m 
# Exceções: Para o caso 0^0 mod m, informe que é "Impossível calcular". Para o caso m <= 1, informe que é "Impossível calcular". 

from math import floor


def expmod(a, n, m):
    if a == n == 0:
        return "Impossível calcular"
    if m <= 1:
        return "Impossível calcular"
    if n == 0:
        return 1
    if n % 2 == 0:
        return ((expmod(a, n /2 , m)) ** 2) % m
    else:
        return (((expmod(a, floor(n/2), m)**2) % m) * (a % m)) % m

print(expmod( 7, 3 , 3))