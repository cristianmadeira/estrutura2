class DequeDinamico:

    def __init__(self, limite):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        self.limite = limite

    def insere_na_esquerda(self, elemento):
        node = Node(elemento)
        if self.inicio is None:
            self.inicio = node
            self.fim = node
        else:
            node.proximo = self.inicio
            self.inicio = node
        self.tamanho = self.tamanho + 1
        return node

    def insere_na_direita(self, elemento):
        node = Node(elemento)
        if self.inicio is None:
            self.inicio = node

        else:
            node.anterior = self.fim
            self.fim.proximo = node
        self.fim = node
        self.tamanho = self.tamanho + 1
        return node

    def remove_na_esquerda(self):
        if self.inicio is not None:
            element = self.inicio
            self.inicio = element.proximo
            return element
        else:
            raise Exception('Lista Vazia!')

    def remove_na_direita(self):
        if self.fim is not None:
            element = self.fim
            self.fim = element.anterior
            return element
        else:
            raise Exception('Lista vazia!')

    def ordena(self):
        elements = self.all()
        for i in range(self.get_tamanho()-1):
            j = i + 1
            while j < self.tamanho:
                if elements[i] > elements[j]:
                    elements[i], elements[j] = self.troca(
                        elements[i], elements[j])
                j = j + 1
            i = i + 1
        return elements

    def troca(self, var1, var2):
        aux = var1
        var1 = var2
        var2 = aux
        return var1, var2

    def pesquisa(self, elemento):
        elements = self.ordena()
        esquerda = 0
        direita = self.get_tamanho() - 1
        while(esquerda <= direita):
            meio = int((direita + esquerda)/2)
            if elemento == elements[meio]:
                return elemento
            elif elemento < elements[meio]:
                direita = meio - 1
            else:
                esquerda = meio + 1
        raise Exception('Elemento não encontrado!')

    def get_tamanho(self):
        return self.tamanho

    def get_limite(self):
        return self.limite

    def is_vazia(self):
        return self.inicio is None

    def all(self):
        if self.inicio is None:
            raise Exception('Lista vazia!')
        else:
            elements = []
            element = self.inicio
            while element is not None:
                elements.append(element.conteudo)
                element = element.proximo
            return elements

    def get_ultimo_elemento(self):
        return self.fim

    def get_primeiro_elemento(self):
        return self.inicio


class Node:
    proximo = None
    anterior = None
    conteudo = None

    def __init__(self, valor):
        self.proximo = None
        self.anterior = None
        self.conteudo = valor

    def __str__(self):
        return str(self.conteudo)
