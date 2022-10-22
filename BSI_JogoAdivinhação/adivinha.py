import random

print("TENTE ADIVINHAR O NÚMERO DE 0 A 10:")
aleatorio = random.randrange(11)
# aleatorio = 5
tentativas = 0
rodando = True
while rodando == True:
    chute = int(input("Digite o número: "))
    if chute == aleatorio:
        print("Você acertou!")
        rodando = False
    elif chute < aleatorio:
        print("O número é maior do que o seu!")
        tentativas = tentativas + 1
    elif chute > aleatorio: 
        print("O número é menor do que o seu!")
        tentativas = tentativas + 1
    if tentativas == 3:
        print("Acabou suas chances!")
        print("Tente outra vez")
        rodando = False