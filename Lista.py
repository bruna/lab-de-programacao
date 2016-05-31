class No:
    def __init__(self, data):
        self.data = data
        self.nextNo = None
    def getData(self):
        return self.data
    def setData(self,data):
        self.data=data
    def getNextNo(self):
        return self.nextNo 
    def setNextNo(self,newNo):
        self.nextNo = newNo;

class Lista:
    def __init__(self):
        self.primNo = None
        self.ultNo = None
    def vazia(self):
        return self.PrimNo is None
    def __str__(self):
        if self.vazia():
            return "Lista esta vazia!"
        NoAtual = self.PrimNo
        string = "A lista é:"
        while NoAtual is not None:
            string += str(NoAtual.getData()) + " "
            NoAtual = NoAtual.ProxNo()
        return string
    def alterar(self, velho, novo):
        NoAtual = self.primNo
        if self.isEmpty():
            raise IndexError("Remocao de lista vazia!")
        else:
            while NoAtual is not None:
                if (NoAtual.getData() == velho):
                    NoAtual.setData(novo)
                    break
                elif NoAtual is None:
                    raise IndexError("valor nao encontrado")
        return "valor alterado com sucesso"
    def inserirComeco(self,valor):
        novoNo = No(valor)
        if self.isEmpty():
            self.primNo = self.ultNo = novoNo
        else:                   #Insersao para lista nao vazia
            novoNo.setNextNo(self.primNo)
            self.primNo = novoNo
    def inserirFim(self,valor):
        novoNo = No(valor)
        if self.isEmpty():
            self.primNo = self.ultNo = novoNo
        else:
            self.ultNo.setNextNo(novoNo)
            self.ultNo=novoNo
    def removerComeco(self):
        if self.isEmpty():
            raise IndexError("Remocao de uma Lista Vazia")
        primNoValor = self.primNode.getData()
        if self.primNo is self.ultNo:
            self.primNo = self.ultNode = None
        else:
            self.primNo = self.primNo.getNextNo()
        return primNoValor
    def removerFim(self):
        if self.isEmpty():
            raise IndexError("Remocao de lista vazia!")
        ultNoValor = self.ultNo.getData()
        if self.primNo is self.ultNo:
            self.primNo = self.ultNo = None
        else:
            NoAtual = self.primNo
            while NoAtual.getNextNo() is not self.ultNo:
                NoAtual = NoAtual.getNextNo()
            NoAtual.setNextNo(None)
            self.ultNo = NoAtual
        return ultNoValor

class Pilha(Lista):
    def empilhar(self,data):
        self.inserirComeco(data)
    def desimpilhar(self):
        return self.removerComeco()
    
