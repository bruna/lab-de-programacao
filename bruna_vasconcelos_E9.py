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
    def isEmpty(self):
        if self.primNo == None and self.ultNo == None:
            return True
        return False
    def inserirComeco(self,valor):
        novoNo = No(valor)
        if self.isEmpty():
            self.primNo = self.ultNo = novoNo
        else:
            novoNo.setNextNo(self.primNo)
            self.primNo = novoNo
    def removerFim(self):
        if self.isEmpty():
            return
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
    def imprime(self):
        ult = self.ultNo
        if self.isEmpty():
                fecha.write("0 ")
        if ult != None:
            string = ult.getData()+" " ##Apenas o primeiro de cada fila, que no caso vai ser o ultimo elemento
            fecha.write(string)
        return None

import sys
abre = open(sys.argv[1],"r")
fecha = open(sys.argv[2],"w")
numCasos = abre.readline()

for nCaso in range(int(numCasos)):
        qtComandos = abre.readline()
        caso = str(nCaso+1)
        fecha.write("Caso "+caso+":\n")
        preferencial = Lista()
        regular = Lista()            
        for i in range(int(qtComandos)):
                comando = abre.readline().split()
                if comando[0] == "I":
                        regular.imprime()
                        preferencial.imprime()
                        fecha.write("\n")
                elif comando[0] == "A":
                    if regular.isEmpty() == True:
                        preferencial.removerFim()
                    regular.removerFim()
                elif comando[0] == "B":
                    if preferencial.isEmpty() == True:
                        regular.removerFim()
                    preferencial.removerFim()                    
                else:
                    if len(comando) > 1:
                            codigoPessoa = comando[1]
                            if comando[0] == "p":
                                    preferencial.inserirComeco(codigoPessoa)
                            else:
                                    regular.inserirComeco(codigoPessoa)
        
abre.close()
fecha.close()
