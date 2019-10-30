#Dev by Joao Piga
class No(object):
    #definicao das variaveis utilziadas
    def __init__(self, aux, aux2, ant, prox):
        self.aux = int(aux)
        self.aux2 = aux2
        self.ant = ant
        self.prox = prox

class ListaDuplamenteEncadeada(object):
    cabeca = None
    rabo = None


#busca e percorre o texto digitado e printa na tela
def busca(listaTexto,listaCod,texto):
    j = 0
    for i in texto:
        for j in range(len(listaTexto)):
            if i == listaTexto[j]:
                print(listaCod[j], end='')
            
#acrescenta os nós
def acrescentar(self, aux, aux2):
    novo_no = No(aux,aux2, None, None)
    i = self.cabeca
    if self.cabeca is None:
        self.cabeca = novo_no
        self.rabo = novo_no
    else:
        if aux > int(self.cabeca.aux):
            novo_no.prox = self.cabeca
            self.cabeca.ant = novo_no
            self.cabeca = novo_no
        else:
            v = int(self.cabeca.aux)
            while aux < v or aux == v:
                if i == self.rabo:
                    i.prox = novo_no
                    novo_no.ant = i
                    self.rabo = novo_no
                    break
                else:
                    if i.prox is not None:
                        i = i.prox
                        v = int(i.aux)
            if aux > v:
                novo_no.prox = i
                novo_no.ant = i.ant
                i.ant.prox = novo_no
                i.ant = novo_no
                       

def criararvore(self, listaTexto, listaCod):
    if self.rabo.prox == None:
        self.rabo.aux = self.rabo.aux+self.rabo.ant.aux
        listaTexto.append(self.rabo.aux2)
        listaCod.append('1')
        listaTexto.append(self.rabo.ant.aux2)
        listaCod.append('0')
        self.rabo = self.rabo.ant
        self.rabo.prox.ant = self.rabo.aux2
        self.rabo.prox.prox = self.rabo.prox.aux2
        self.rabo = self.rabo.ant
        self.rabo.prox = self.rabo.prox.prox
        print('teste')
        i = 2
        j = i
        k = i
    while True:
        if self.rabo == self.cabeca:
            self.rabo.ant = self.rabo.aux2
            listaTexto.append(self.rabo.aux2)
            listaCod.append('0')
            for j in range(i):
                    listaCod[j] = '1' + listaCod[j]
            break
        else:
            a = self.rabo.ant.aux
            b = self.rabo.prox.aux
            if a > b:
                self.rabo.aux = self.rabo.aux+self.rabo.prox.aux
                listaTexto.append(self.rabo.aux2)
                listaCod.append('0')
                for o in range(i):
                    listaCod[o] = '1' + listaCod[o]
                i = i+1
                j = i+1
                self.rabo = self.rabo.ant
                self.rabo.prox.ant = self.rabo.prox.aux2
            else:
                novo_no = No(self.rabo.aux+self.rabo.ant.aux, None, self.rabo.aux2, self.rabo.ant.aux2)
                self.rabo = self.rabo.ant
                self.rabo.prox.ant = novo_no
                self.rabo.prox.aux = self.rabo.prox.aux+self.rabo.aux
                listaTexto.append(self.rabo.aux2)
                listaCod.append('00')
                listaTexto.append(self.rabo.prox.aux2)
                listaCod.append('01')
                for j in range(k):
                    listaCod[j] = '1' + listaCod[j]
                k = k+1
                self.rabo = self.rabo.ant
        
def percorrer(self):
    i = self.cabeca
    while i != self.rabo:
        i = i.prox
    
def comparar(self,aux2):
    no_atual = self.cabeca
    while no_atual is not None:
        if str(no_atual.aux2) == aux2:
            return True
            break
        else:
            no_atual = no_atual.prox  
    if no_atual is None:
        return False

def contador(texto):
    c = bool
    j = 0
    lista = ListaDuplamenteEncadeada()
    listaTexto = []
    listaCod = []
    for i in texto:
        c = comparar(lista,i)
        if c == False:
            acrescentar(lista,texto.count(i),i)
    criararvore(lista,listaTexto,listaCod)
    print('Tabela para comparação:')
    for j in range(len(listaCod)):
        print('|*|'+listaTexto[j]+'|*||*|'+listaCod[j]+'|*|')
        j = j+1
    print('Codigo comprimido:')
    busca(listaTexto,listaCod,texto)


texto = str(input('\ndigite a palavra: '))
print('Texto: |',texto,'| Comprimido: ')
contador(texto)