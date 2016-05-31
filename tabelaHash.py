
from Lista import *


class elemento():
    def __init__(self, chave, valor):
        self._chave= chave
        self._valor = valor
        
    def __str__(self):
        chavii = self.getChave()
        valorii = self.getValor()
        chavii = str(chavii)
        valorii = str(valorii)
        elementstring = "a chave eh: "+ chavii +" o valor eh: "+ valorii
        return elementstring
    
    def getChave(self):
        return self._chave
    def setChave(self, chave):
        self._chave = chave
    def getValor(self):
        return self._valor
    def setValor(self, valor):
        self._valor = valor
        

class tabelaHash():
    def __init__(self, tamanho):
        self._tabela = [None]*tamanho
        
    def inserir(self, chave, valor):
        h= hash(chave)
        e=elemento(chave, valor)
        
        if(self._tabela[h] == None):
            listinha = List()
            listinha.insertAtBegin(e)
            self._tabela[h] =listinha
        else:
            self._tabela[h].insertAtBegin(e)
    
    
    def procurar(self, chave):
        h = hash(chave)
        if self._tabela[h]!=None:
            return self._tabela[h]
        else:
            return 0
    
    def __str__(self):
        str = ''
        for i in self._tabela:
            if i == None:
                str += "vazio"+ "\n"
            else:
                str += i.__str__() + "\n"
        return str
    
        
    def hash(self, chave):
        return chave%tamanho    
        
    def getTamanho(self):
        return self._tamanho
    def setTamanho(self, tamanho):
        self._tamanho = tamanho