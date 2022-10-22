def cosseno():
    x = float(input())
    numerador1 = 1
    numerador2 = 1
    denominador = 1
    total = 0
    for i in range(51):
        if i%2==0 :
            numerador1 = 1
        else: 
            numerador1 = -1
        
        if i == 0:
            numerador2 = 1
        else:
            numerador2 = numerador2*x*x
        if i == 0:
            denominador = 1
        else:
            denominador = denominador*(2*i)*((2*i) - 1)

        total = ((numerador1*numerador2) / denominador ) + total

    return print(total) 

cosseno()


    