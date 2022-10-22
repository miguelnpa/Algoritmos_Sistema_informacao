# Implemente um algoritmo recursivo para busca linear em uma lista de números quaiquer. 

# Entrada: Uma lista de números.
        #   Dois índices i ( início da lista) e j ( fim da lista)
        # Um número x que será procurado na lista ( ele não precisa estar na lista)

# Saída: A posição do número x, caso ele esteja na lista, ou -1 se ele não estiver.
# Exceções: Quando a lista for vazia, retorne -1 para qualquer valor de x.

lista = [1,2,3,4,5,6]
lista2 = []
def busca_linear_recur(lista, inicioLista , fimLista, encontrar):
    if lista == []:
        return -1
    elif not list:
        return -1
    if lista[inicioLista] == encontrar:
        return "posição: %d" %(inicioLista)
    elif inicioLista == fimLista:
        return -1
    else:
        return busca_linear_recur(lista, inicioLista + 1, fimLista, encontrar)
print(busca_linear_recur(lista, 0, 5, 3))