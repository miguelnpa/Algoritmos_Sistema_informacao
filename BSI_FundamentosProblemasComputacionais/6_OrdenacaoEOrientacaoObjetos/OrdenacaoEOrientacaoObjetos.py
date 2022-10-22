
class Livro:
    codigo = None
    nome = None
    autor = None
    __qtdeAlugueis = 0

    def __init__(self, codigo, nome, autor):
        self.codigo = codigo
        self.nome = nome
        self.autor = autor
        

        
    def incrementaAluguel(self):
        self.__qtdeAlugueis += 1
    def getQtdeAlugueis(self):
        return self.__qtdeAlugueis

class Biblioteca:
    alugados = []
    disponiveis = []

    def inserir(self, livro):
        self.disponiveis.append(livro)

    def alugar(self, livro):
        ok = True
        mensagem = None
        if livro in self.disponiveis:
            for i in self.disponiveis:
                if i == livro:
                    i.incrementaAluguel()
                    self.alugados.append(i)
                    self.disponiveis.remove(i)
                    break
        elif livro in self.alugados:
            ok = False
            mensagem = "O livro ja esta alugado, infelizmente voce nao podera alugar"
        else:
            ok = False
            mensagem = "O livro nao existe"
        return (ok, mensagem)

    def devolver(self, codLivro):
        ok = True
        mensagem = None
        for livro in self.alugados:
            if livro.codigo == codLivro:
                self.disponiveis.append(livro)
                self.alugados.remove(livro)
                break
        else:
            ok = False
            mensagem = "O livro nao esta alugado"
        return (ok, mensagem)

    def livroMaisAlugado(self):
        ok = True
        mensagem = None
        maior = 0
        nome = None
        for livro in self.disponiveis:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        for livro in self.alugados:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        if maior == 0:
            ok = False
            mensagem = "Nenhum livro foi alugado ainda"
        else:
            mensagem = "O livro mais alugado e: %s (%d alugueis)"%(nome, maior)
            return (ok, mensagem)

    def bubbleSort(self,lista):
        troca = True
        while troca:
            troca = False
            for i in range(len(lista) - 1):
                if lista[i].nome > lista[i + 1].nome:
                    chave = lista[i]
                    lista[i] = lista[i + 1]
                    lista[i + 1] = chave
                    troca = True
        return lista

    def mesclarListas(self,disponiveis,alugados):
        i = j = 0
        todosLivros = []
        while (i < len(disponiveis) and j < len(alugados)):
            if (disponiveis[i].nome <= alugados[j].nome):
                todosLivros.append(disponiveis[i])
                i = i + 1
            else:
                todosLivros.append(alugados[j])
                j = j + 1
        while (i < len(disponiveis)):
            todosLivros.append(disponiveis[i])
            i = i + 1
        while(j < len(alugados)):
            todosLivros.append(alugados[j])
            j = j + 1
        return todosLivros

    def livrosOrdenadosPeloNome(self):
        disponiveis = self.bubbleSort(self.disponiveis)
        alugados = self.bubbleSort(self.alugados)
        livrosEmOrdem = self.mesclarListas(disponiveis,alugados)
        return livrosEmOrdem

biblioteca = Biblioteca()

entrada = input()
entrada = entrada.split(",")

quantidadeLivros = int(entrada.pop(0))

for i in range(quantidadeLivros):
    codigo = entrada.pop(0)
    nomeLivro = entrada.pop(0)
    autor = entrada.pop(0)
    livro = Livro(codigo,nomeLivro,autor)
    biblioteca.inserir(livro)

livrosEmOrdem = biblioteca.livrosOrdenadosPeloNome()
codigoEmOrdem = []

for i in livrosEmOrdem:
    codigoEmOrdem.append(str(i.codigo))

saida = " ".join(codigoEmOrdem)
print(saida)